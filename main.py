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
            food_elements = await food_element.querySelectorAll('div.sc-tQuYZ.gvgoZc > button > h3 > span')
            
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

                dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

                doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

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

                dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

                doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

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

            dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await ctx.send("Sorry but it does not appear that there is a Dinner option today at Tooker dining...")

            doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

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

                dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await ctx.send("Sorry but it does not appear that there is a Brunch option today at Tooker dining...")

                doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

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

@bot.command()
@commands.is_owner()
async def shutdown(context):
    exit()     
    
bot.run(TOKEN)
    
