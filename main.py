#bot.py

import os
from dotenv import load_dotenv, find_dotenv

import asyncio

import discord
from discord.ext import commands
from discord import app_commands

from pyppeteer import launch
from pyppeteer.errors import TimeoutError

import time
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="?", intents=intents)


now = datetime.now()
hour = now.hour
day = now.weekday()

@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running')
    
@bot.command(name='tooker')
async def tooker_menu(ctx, arg1):
    
    now = datetime.now()
    hour = now.hour
    day = now.weekday()
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/TookerHouseDining')
    
    try:
        subscription_modal_button = await page.xpath('//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')
        if subscription_modal_button:
            await asyncio.wait_for(subscription_modal_button[0].click(), timeout=10)
    except TimeoutError:
        pass

    try:
        cookie_banner_button = await page.xpath('//*[@id="onetrust-close-btn-container"]/button')
        if cookie_banner_button:
            await asyncio.wait_for(cookie_banner_button[0].click(), timeout=10)
    except TimeoutError:
        pass
    
    food_dict = {}
    
    async def scrape_food(xpath, key):
        try:
            food_element = await page.xpath(xpath)
            food_element = food_element[0]
            food_elements = await food_element.querySelectorAll('div.sc-eZkCL.hKoqlN > button > h3 > span')

            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
        
    requestedMeal = arg1.lower()
    
    if(requestedMeal == 'breakfast'):
        
        if(day == 5 or day == 6):
            await ctx.send("Today is a weekend which means Tooker dining does not serve Breakfast today, maybe try asking for Brunch instead.")
    
        else:
            
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Breakfast':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)

    
            await scrape_food('//*[@id="22794"]', 'Daily Root')
            await scrape_food('//*[@id="22792"]', 'Home Zone')
            await scrape_food('//*[@id="30185"]', 'True Balance')
            
            dailyRoot = food_dict['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            
            homeZone = food_dict['Home Zone']
            homeZone = ', '.join(homeZone)
            
            trueBalance = food_dict['True Balance']
            trueBalance = ', '.join(trueBalance)
            
            embed = discord.Embed(title='Tooker House Breakfast', description= 'Tooker House Breakfast Menu')
        
            embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
            
            try:
                embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Home Zone:", value=homeZone, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='True Balance:', value=trueBalance, inline=False)
            except:
                pass

            embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
            
    if(requestedMeal == 'lunch'):
        
        if(day == 5 or day == 6):
            await ctx.send("Today is a weekend which means Tooker dining does not serve Lunch today, maybe try asking for Brunch instead.")
    
        else:
            
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Lunch':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)

    
            await scrape_food('//*[@id="22794"]', 'Daily Root')
            await scrape_food('//*[@id="22792"]', 'Home Zone')
            await scrape_food('//*[@id="22793"]', 'Grill')
            await scrape_food('//*[@id="22796"]', 'Pizza')
            await scrape_food('//*[@id="22797"]', 'Soup')
            await scrape_food('//*[@id="30185"]', 'True Balance')
            
            dailyRoot = food_dict['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            
            homeZone = food_dict['Home Zone']
            homeZone = ', '.join(homeZone)
            
            grill = food_dict['Grill']
            grill = ', '.join(grill)
            
            pizza = food_dict['Pizza']
            pizza = ', '.join(pizza)
            
            soup = food_dict['Soup']
            soup = ', '.join(soup)
            
            trueBalance = food_dict['True Balance']
            trueBalance = ', '.join(trueBalance)
            
            shawarma = ['Falafel Pita']
            shawarma = ', '.join(shawarma)
            
            embed = discord.Embed(title='Tooker House Lunch', description= 'Tooker House Lunch Menu')
        
            embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
            
            try:
                embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Home Zone:", value=homeZone, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='True Balance:', value=trueBalance, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Grill', value=grill, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Pizza', value=pizza, inline=True)
            except:
                pass
            
            try:
                embed.add_field(name='Soup', value=soup, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Shawarma Station', value=shawarma, inline=True)
            except:
                pass

            embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
            
    if(requestedMeal == 'dinner'):
            
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await ctx.send("Sorry but it does not appear that there is a Dinner option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="22793"]', 'Grill')
        await scrape_food('//*[@id="22796"]', 'Pizza')
        await scrape_food('//*[@id="22797"]', 'Soup')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        
        dailyRoot = food_dict['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        homeZone = food_dict['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = food_dict['Grill']
        grill = ', '.join(grill)
        
        pizza = food_dict['Pizza']
        pizza = ', '.join(pizza)
        
        soup = food_dict['Soup']
        soup = ', '.join(soup)
        
        trueBalance = food_dict['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        shawarma = ['Chicken Shawarma Pita', 'Falafel Pita']
        shawarma = ', '.join(shawarma)
        
        embed = discord.Embed(title='Tooker House Dinner', description= 'Tooker House Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
        
        try:
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            embed.add_field(name='Soup', value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Shawarma Station', value=shawarma, inline=True)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
    
    if(requestedMeal == 'brunch'):
        
        if(day != 5 and day != 6):
            await ctx.send("Today is a weekday which means that Tooker dining hall does not serve Brunch, perhaps try Breakfast or Lunch instead")
    
        else:
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Brunch':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Brunch option today at Tooker dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)


            await scrape_food('//*[@id="22794"]', 'Daily Root')
            await scrape_food('//*[@id="22792"]', 'Home Zone')
            await scrape_food('//*[@id="22793"]', 'Grill')
            await scrape_food('//*[@id="22796"]', 'Pizza')
            await scrape_food('//*[@id="30185"]', 'True Balance')

            dailyRoot = food_dict['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            
            homeZone = food_dict['Home Zone']
            homeZone = ', '.join(homeZone)
            
            grill = food_dict['Grill']
            grill = ', '.join(grill)
            
            pizza = food_dict['Pizza']
            pizza = ', '.join(pizza)
            
            trueBalance = food_dict['True Balance']
            trueBalance = ', '.join(trueBalance)
            
            embed = discord.Embed(title='Tooker House Brunch', description= 'Tooker House Brunch Menu')
    
            embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
            
            try:
                embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Home Zone:", value=homeZone, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='True Balance:', value=trueBalance, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Grill', value=grill, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Pizza', value=pizza, inline=True)
            except:
                pass
    
    await ctx.send(embed=embed)
    
    await browser.close()
    
@bot.command(name='manzanita')
async def manzy_menu(ctx, arg1):
    
    now = datetime.now()
    hour = now.hour
    day = now.weekday()
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/en/diningvenues/tempemanzanitaresidentialrestaurant/')
    
    try:
        subscription_modal_button = await page.xpath('//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')
        if subscription_modal_button:
            await asyncio.wait_for(subscription_modal_button[0].click(), timeout=10)
    except TimeoutError:
        pass

    try:
        cookie_banner_button = await page.xpath('//*[@id="onetrust-close-btn-container"]/button')
        if cookie_banner_button:
            await asyncio.wait_for(cookie_banner_button[0].click(), timeout=10)
    except TimeoutError:
        pass
    
    food_dict = {}
    
    async def scrape_food(xpath, key):
        try:
            food_element = await page.xpath(xpath)
            food_element = food_element[0]
            food_elements = await food_element.querySelectorAll('div.sc-eZkCL.hKoqlN > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
        
    requestedMeal = arg1.lower()
    
    if(requestedMeal == 'breakfast'):
            if(day == 5 or day == 6):
                await ctx.send("Today is a weekend which means that Manzanita dining hall does not serve Breakfast, perhaps try asking for lunch instead")
                
            else:
                await asyncio.sleep(2)

                meal = await page.querySelector('.ChoosenMeal')
                meal = await page.evaluate('(element) => element.textContent', meal)

                if meal != 'Breakfast':
                    print('wrong meal')
                    try:
                        swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                        await swapButton.click()
                        print('swap button clicked')
                    except:
                        pass

                    dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                    await dropDown.click()
                    print('dropdown clicked')

                    try:
                        breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                        await breakfastOption.click()
                        print('breakfast option clicked')
                    except:
                        await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Manzanita dining...")

                    doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                    await doneButton.click()
                    await page.waitForSelector('.ChoosenMeal', timeout=60000)

                    await asyncio.sleep(2)
                    
                await scrape_food('//*[@id="9135"]', 'Action')
                await scrape_food('//*[@id="9139"]', 'Home Zone')
                await scrape_food('//*[@id="9141"]', 'Salad Bar')
                await scrape_food('//*[@id="9138"]', 'Grill')
                
                Action = food_dict['Action']
                Action = ', '.join(Action)
                
                homeZone = food_dict['Home Zone']
                homeZone = ', '.join(homeZone)
                
                saladBar = food_dict['Salad Bar']
                saladBar = ', '.join(saladBar)
                
                grill = food_dict['Grill']
                grill = ', '.join(grill)
                
                embed = discord.Embed(title='Manzanita Dining Hall Breakfast', description= 'Manzanita Dining Hall Breakfast Menu')
        
                embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
                
                try:
                    embed.add_field(name="Action:", value=Action, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name="Home Zone:", value=homeZone, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name='Salad Bar:', value=saladBar, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name='Grill:', value=grill, inline=True)
                except:
                    pass

                embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
                
    if(requestedMeal == 'lunch'):
        
        if(day == 5 or day == 6):
            await ctx.send("Sorry, but today appears to be a weekend which means that the Manzanita Dining Hall is not serving lunch, perhaps try requesting the Brunch menu instead")

        else:
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Lunch':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Lunch option today at Manzanita dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)
                    
            await scrape_food('//*[@id="9135"]', 'Action')
            await scrape_food('//*[@id="9139"]', 'Home Zone')
            await scrape_food('//*[@id="9138"]', 'Grill')
            await scrape_food('//*[@id="9140"]', 'Pizza')
            await scrape_food('//*[@id="13991"]', 'Sazon Station')
            
            Action = food_dict['Action']
            Action = ', '.join(Action)
            
            homeZone = food_dict['Home Zone']
            homeZone = ', '.join(homeZone)
            
            grill = food_dict['Grill']
            grill = ', '.join(grill)
            
            pizza = food_dict['Pizza']
            pizza = ', '.join(pizza)
            
            sazonStation = food_dict['Sazon Station']
            sazonStation = ', '.join(sazonStation)
            
            embed = discord.Embed(title='Manzanita Dining Hall Lunch', description= 'Manzanita Dining Hall Lunch Menu')
        
            embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
            
            try:
                embed.add_field(name="Action:", value=Action, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Home Zone:", value=homeZone, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Sazon Station:', value=sazonStation, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Grill:', value=grill, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Pizza', value=pizza, inline=True)
            except:
                pass

            embed.set_image(url="https://i.imgur.com/GSx3eR2.png")

    if(requestedMeal == 'dinner'):
        
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await ctx.send("Sorry but it does not appear that there is a Dinner option today at Manzanita dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
                
        await scrape_food('//*[@id="9135"]', 'Action')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
        
        Action = food_dict['Action']
        Action = ', '.join(Action)
        
        homeZone = food_dict['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = food_dict['Grill']
        grill = ', '.join(grill)
        
        pizza = food_dict['Pizza']
        pizza = ', '.join(pizza)
        
        sazonStation = food_dict['Sazon Station']
        sazonStation = ', '.join(sazonStation)
        
        embed = discord.Embed(title='Manzanita Dining Hall Dinner', description= 'Manzanita Dining Hall Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Action:", value=Action, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Sazon Station:', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Grill:', value=grill, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")

    await ctx.send(embed=embed)
    
@bot.command(name='manzy')
async def manzy_menu(ctx, arg1):
    
    now = datetime.now()
    hour = now.hour
    day = now.weekday()
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/en/diningvenues/tempemanzanitaresidentialrestaurant/')
    
    try:
        subscription_modal_button = await page.xpath('//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')
        if subscription_modal_button:
            await asyncio.wait_for(subscription_modal_button[0].click(), timeout=10)
    except TimeoutError:
        pass

    try:
        cookie_banner_button = await page.xpath('//*[@id="onetrust-close-btn-container"]/button')
        if cookie_banner_button:
            await asyncio.wait_for(cookie_banner_button[0].click(), timeout=10)
    except TimeoutError:
        pass
    
    food_dict = {}
    
    async def scrape_food(xpath, key):
        try:
            food_element = await page.xpath(xpath)
            food_element = food_element[0]
            food_elements = await food_element.querySelectorAll('div.sc-eZkCL.hKoqlN > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
        
    requestedMeal = arg1.lower()
    
    if(requestedMeal == 'breakfast'):
            if(day == 5 or day == 6):
                await ctx.send("Today is a weekend which means that Manzanita dining hall does not serve Breakfast, perhaps try asking for lunch instead")
                
            else:
                await asyncio.sleep(2)

                meal = await page.querySelector('.ChoosenMeal')
                meal = await page.evaluate('(element) => element.textContent', meal)

                if meal != 'Breakfast':
                    try:
                        swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                        await swapButton.click()
                    except:
                        pass

                    dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                    await dropDown.click()

                    try:
                        breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                        await breakfastOption.click()
                    except:
                        await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Manzanita dining...")

                    doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                    await doneButton.click()
                    await page.waitForSelector('.ChoosenMeal', timeout=60000)

                    await asyncio.sleep(2)
                    
                await scrape_food('//*[@id="9135"]', 'Action')
                await scrape_food('//*[@id="9139"]', 'Home Zone')
                await scrape_food('//*[@id="9141"]', 'Salad Bar')
                await scrape_food('//*[@id="9138"]', 'Grill')
                
                Action = food_dict['Action']
                Action = ', '.join(Action)
                
                homeZone = food_dict['Home Zone']
                homeZone = ', '.join(homeZone)
            
                saladBar = food_dict['Salad Bar']
                saladBar = ', '.join(saladBar)
                
                grill = food_dict['Grill']
                grill = ', '.join(grill)
                
                embed = discord.Embed(title='Manzanita Dining Hall Breakfast', description= 'Manzanita Dining Hall Breakfast Menu')
        
                embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
                
                try:
                    embed.add_field(name="Action:", value=Action, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name="Home Zone:", value=homeZone, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name='Salad Bar:', value=saladBar, inline=False)
                except:
                    pass
                
                try:
                    embed.add_field(name='Grill:', value=grill, inline=True)
                except:
                    pass

                embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
                
    if(requestedMeal == 'lunch'):
        
        if(day == 5 or day == 6):
            await ctx.send("Sorry, but today appears to be a weekend which means that the Manzanita Dining Hall is not serving lunch, perhaps try requesting the Brunch menu instead")

        else:
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Lunch':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Lunch option today at Manzanita dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)
                    
            await scrape_food('//*[@id="9135"]', 'Action')
            await scrape_food('//*[@id="9139"]', 'Home Zone')
            await scrape_food('//*[@id="9138"]', 'Grill')
            await scrape_food('//*[@id="9140"]', 'Pizza')
            await scrape_food('//*[@id="13991"]', 'Sazon Station')
            
            Action = food_dict['Action']
            Action = ', '.join(Action)
            
            homeZone = food_dict['Home Zone']
            homeZone = ', '.join(homeZone)
            
            grill = food_dict['Grill']
            grill = ', '.join(grill)
            
            pizza = food_dict['Pizza']
            pizza = ', '.join(pizza)
            
            sazonStation = food_dict['Sazon Station']
            sazonStation = ', '.join(sazonStation)
            
            embed = discord.Embed(title='Manzanita Dining Hall Lunch', description= 'Manzanita Dining Hall Lunch Menu')
        
            embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
            
            try:
                embed.add_field(name="Action:", value=Action, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Home Zone:", value=homeZone, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Sazon Station:', value=sazonStation, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Grill:', value=grill, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Pizza', value=pizza, inline=True)
            except:
                pass

            embed.set_image(url="https://i.imgur.com/GSx3eR2.png")

    if(requestedMeal == 'dinner'):
        
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await ctx.send("Sorry but it does not appear that there is a Dinner option today at Manzanita dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
                
        await scrape_food('//*[@id="9135"]', 'Action')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
        
        Action = food_dict['Action']
        Action = ', '.join(Action)
        
        homeZone = food_dict['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = food_dict['Grill']
        grill = ', '.join(grill)
        
        pizza = food_dict['Pizza']
        pizza = ', '.join(pizza)
        
        sazonStation = food_dict['Sazon Station']
        sazonStation = ', '.join(sazonStation)
        
        embed = discord.Embed(title='Manzanita Dining Hall Dinner', description= 'Manzanita Dining Hall Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Action:", value=Action, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Sazon Station:', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Grill:', value=grill, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")

    await ctx.send(embed=embed)

@bot.command(name='pitchforks')
async def pitchforks_menu(ctx, arg1):
    
    now = datetime.now()
    hour = now.hour
    day = now.weekday()
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/en/diningvenues/tempepitchforksrestaurant/')
    
    try:
        subscription_modal_button = await page.xpath('//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')
        if subscription_modal_button:
            await asyncio.wait_for(subscription_modal_button[0].click(), timeout=10)
    except TimeoutError:
        pass

    try:
        cookie_banner_button = await page.xpath('//*[@id="onetrust-close-btn-container"]/button')
        if cookie_banner_button:
            await asyncio.wait_for(cookie_banner_button[0].click(), timeout=10)
    except TimeoutError:
        pass
    
    food_dict = {}
    
    async def scrape_food(xpath, key):
        try:
            food_element = await page.xpath(xpath)
            food_element = food_element[0]
            food_elements = await food_element.querySelectorAll('div.sc-eZkCL.hKoqlN > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
        
    requestedMeal = arg1.lower()
    
    if(requestedMeal == 'breakfast'):
        
        if(day == 5 or day == 6):
            await ctx.send("Today is a weekend which means that Pitchforks Dining Hall does not serve Breakfast, the dining hall opens at 4 PM for Dinner")
            
        else:
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Breakfast':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Pitchforks dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)
                
            await scrape_food('//*[@id="14584"]', 'International')
            await scrape_food('//*[@id="17302"]', 'Vegan')
            await scrape_food('//*[@id="17305"]', 'Soups')
            
            international = food_dict['International']
            international = ', '.join(international)
            
            vegan = food_dict['Vegan']
            vegan = ', '.join(vegan)
            
            soups = food_dict['Soups']
            soups = ', '.join(soups)
            
            embed = discord.Embed(title='Pitchforks Dining Hall Breakfast', description='Pitchforks Dining Hall Breakfast Menu')
            
            embed.set_thumbnail(url='https://i.imgur.com/FvCWGxy.jpg')
            
            try:
                embed.add_field(name='International Food Station', value=international, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Vegan Station', value=vegan, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Soups', value=soups, inline=False)
            except:
                pass
            
            embed.set_image(url='https://i.imgur.com/hlzODkP.png')
        
    if(requestedMeal == 'lunch'):
        
        if(day == 5 or day == 6):
            await ctx.send("Today is a weekend which means that Pitchforks Dining Hall does not serve Lunch, the dining hall opens at 4 PM for Dinner")


        else:
            await asyncio.sleep(2)

            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Lunch':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Lunch option today at Pitchforks dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)
                
            await scrape_food('//*[@id="17303"]', 'Salad & Deli')
            await scrape_food('//*[@id="14584"]', 'International')
            await scrape_food('//*[@id="17302"]', 'Vegan')
            await scrape_food('//*[@id="17300"]', 'Pizza')
            await scrape_food('//*[@id="17299"]', 'Asian')
            await scrape_food('//*[@id="17301"]', 'Limon')
            await scrape_food('//*[@id="17305"]', 'Soups')
            
            saladDeli = food_dict['Salad & Deli']
            saladDeli = ', '.join(saladDeli)
            
            international = food_dict['International']
            international = ', '.join(international)
            
            vegan = food_dict['Vegan']
            vegan = ', '.join(vegan)
            
            pizza = food_dict['Pizza']
            pizza = ', '.join(pizza)
            
            asian = food_dict['Asian']
            asian = ', '.join(asian)
            
            limon = food_dict['Limon']
            limon = ', '.join(limon)
            
            soups = food_dict['Soups']
            soups = ', '.join(soups)
            
            embed = discord.Embed(title="Pitchforks Dining Hall Lunch", description="Pitchforks Dining Hall Lunch Menu")
            
            embed.set_thumbnail(url='https://i.imgur.com/FvCWGxy.jpg')
            
            try:
                embed.add_field(name="International Food Station", value=international, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Vegan Station', value=vegan, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name="Asian Food Station", value=asian, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Limon', value=limon, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Pizza', value=pizza, inline=False)
            except:
                pass
            
            try:
                embed.add_field(name='Soups', value=soups, inline=True)
            except:
                pass
            
            try:
                embed.add_field(name='Salad & Deli', value=saladDeli, inline=False)
            except:
                pass
            
            embed.set_image(url='https://i.imgur.com/hlzODkP.png')
        
    if(requestedMeal == 'Dinner'):
        
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Pitchforks dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2) 
            
        await scrape_food('//*[@id="17303"]', 'Salad & Deli')
        await scrape_food('//*[@id="14584"]', 'International')
        await scrape_food('//*[@id="17302"]', 'Vegan')
        await scrape_food('//*[@id="17300"]', 'Pizza')
        await scrape_food('//*[@id="17299"]', 'Asian')
        await scrape_food('//*[@id="17301"]', 'Limon')
        await scrape_food('//*[@id="17305"]', 'Soups')
        await scrape_food('//*[@id="45017"]', 'True Balance')
        
        saladDeli = food_dict['Salad & Deli']
        saladDeli = ', '.join(saladDeli)
        
        international = food_dict['International']
        international = ', '.join(international)
        
        vegan = food_dict['Vegan']
        vegan = ', '.join(vegan)
        
        pizza = food_dict['Pizza']
        pizza = ', '.join(pizza)
        
        asian = food_dict['Asian']
        asian = ', '.join(asian)
        
        limon = food_dict['Limon']
        limon = ', '.join(limon)
        
        soups = food_dict['Soups']
        soups = ', '.join(soups)
        
        trueBalance = food_dict['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        embed = discord.Embed(title="Pitchforks Dining Hall Dinner", description="Pitchforks Dining Hall Dinner Menu")
        
        embed.set_thumbnail(url='https://i.imgur.com/FvCWGxy.jpg')
        
        try:
            embed.add_field(name="International Food Station", value=international, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Vegan Station', value=vegan, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Asian Food Station", value=asian, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Limon', value=limon, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Pizza', value=pizza, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Soups', value=soups, inline=True)
        except:
            pass
        
        try:
            embed.add_field(name='Salad & Deli', value=saladDeli, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance', value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url='https://i.imgur.com/hlzODkP.png')
                
                
                
        
    await ctx.send(embed=embed)
            
            
    

    

@bot.command()
@commands.is_owner()
async def shutdown(context):
    exit()     


bot.run(TOKEN)
    
