#bot.py

import os
from dotenv import load_dotenv, find_dotenv

import asyncio

import discord
from discord.ext import commands, tasks
from discord import app_commands


from pyppeteer import launch
from pyppeteer.errors import TimeoutError

import time
from datetime import datetime, timedelta

import threading

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents, case_insensitive=True)



now = datetime.now()
hour = now.hour
day = now.weekday()

'''
tookerBreakfast = {}
tookerLunch = {}
tookerDinner = {}
tookerBrunch = {}

manzyBreakfast = {}
manzyLunch = {}
manzyDinner = {}
manzyBrunch = {}


pitchforksBreakfast = {}
pitchforksLunch = {}
pitchforksDinner = {}
pitchforksBrunch = {}

hassyBreakfast = {}
hassyLunch = {}
hassyDinner = {}
hassyBrunch = {}

barrettBreakfast = {}
barrettLunch = {}
barrettDinner = {}
barrettBrunch = {}
'''


async def barrettReq(requestedMeal):
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/Tempe-Campus/BarrettTempe')
    
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
            food_elements = await food_element.querySelectorAll('div.sc-kdBSHD.gQLTsY > button > h3 > span')

            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
    
    if(requestedMeal == 'breakfast'):
        
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Breakfast':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="9124"]', 'Salad Bar')
        await scrape_food('//*[@id="9120"]', 'Grill')
        await scrape_food('//*[@id="9122"]', 'True Balance')
        await scrape_food('//*[@id="9125"]', 'The Daily Root')
        await scrape_food('//*[@id="9119"]', 'Dessert/Waffle')
        await scrape_food('//*[@id="34900"]', 'Omelets')
        print("Breakfast: ", food_dict)
    
    elif(requestedMeal == 'lunch'):
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

            
        await scrape_food('//*[@id="9121"]', 'Home Zone 1')
        await scrape_food('//*[@id="9118"]', 'Deli')
        await scrape_food('//*[@id="9124"]', 'Salad Bar')
        await scrape_food('//*[@id="9120"]', 'Grill')
        await scrape_food('//*[@id="9123"]', 'Pizza')
        await scrape_food('//*[@id="9122"]', 'True Balance')
        await scrape_food('//*[@id="9125"]', 'The Daily Root')
        await scrape_food('//*[@id="41605"]', 'Soup Station')
        print("Lunch: ", food_dict)
    
    elif(requestedMeal == 'dinner'):
            
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="9121"]', 'Home Zone 1')
        await scrape_food('//*[@id="9118"]', 'Deli')
        await scrape_food('//*[@id="9124"]', 'Salad Bar')
        await scrape_food('//*[@id="9120"]', 'Grill')
        await scrape_food('//*[@id="9123"]', 'Pizza')
        await scrape_food('//*[@id="9122"]', 'True Balance')
        await scrape_food('//*[@id="9125"]', 'The Daily Root')
        await scrape_food('//*[@id="41605"]', 'Soup Station')
        print("Dinner: ", food_dict)
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="9121"]', 'Home Zone 1')
        await scrape_food('//*[@id="9120"]', 'Grill')
        await scrape_food('//*[@id="9123"]', 'Pizza')
        await scrape_food('//*[@id="9122"]', 'True Balance')
        await scrape_food('//*[@id="9125"]', 'The Daily Root')
        print("Brunch: ", food_dict)

    await browser.close()
    return food_dict
    
async def tookerReq(requestedMeal):

    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/Tempe-Campus/TookerHouseDining')
    
    try:
        subscription_modal_button = await page.xpath('//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')
        if subscription_modal_button:
            await asyncio.wait_for(subscription_modal_button[0].click(), timeout=10)
    except TimeoutError:
        print("Popup 1 not closed")
        pass

    try:
        cookie_banner_button = await page.xpath('//*[@id="onetrust-close-btn-container"]/button')
        if cookie_banner_button:
            await asyncio.wait_for(cookie_banner_button[0].click(), timeout=10)
    except TimeoutError:
        print("Popup 2 not closed")
        pass
    
    food_dict = {}
    
    async def scrape_food(xpath, key):
        try:
            food_element = await page.xpath(xpath)
            food_element = food_element[0]
            food_elements = await food_element.querySelectorAll('div.sc-kdBSHD.gQLTsY > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
    
    if(requestedMeal == 'breakfast'):
        
        await asyncio.sleep(5)

        await page.waitForSelector('.ChoosenMeal')
        mealElement = await page.querySelector('.ChoosenMeal')
        if mealElement:  # Ensure the element exists
            meal = await page.evaluate('(element) => element.textContent', mealElement)
            print(meal)
        else:
            print("ChoosenMeal element not found.")

        if meal != 'Breakfast':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

    
        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        print("Breakfast: ", food_dict)
            
    elif(requestedMeal == 'lunch'):
        print('lunch')
        await asyncio.sleep(5)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

            print(4)
        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="22793"]', 'Grill')
        await scrape_food('//*[@id="22796"]', 'Pizza')
        await scrape_food('//*[@id="22797"]', 'Soup')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        print("Lunch: ", food_dict)
            
    elif(requestedMeal == 'dinner'):
            
        await asyncio.sleep(5)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="22793"]', 'Grill')
        await scrape_food('//*[@id="22796"]', 'Pizza')
        await scrape_food('//*[@id="22797"]', 'Soup')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        print("Dinner: ", food_dict)
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(5)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="22793"]', 'Grill')
        await scrape_food('//*[@id="22796"]', 'Pizza')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        print("Brunch: ", food_dict)

    await browser.close()
    return food_dict
      
async def manzyReq(requestedMeal):
    now = datetime.now()
    hour = now.hour
    day = now.weekday()
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/Tempe-Campus/TempeManzanitaResidentialRestaurant')
    
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
            food_elements = await food_element.querySelectorAll('div.sc-kdBSHD.gQLTsY > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
    
    if(requestedMeal == 'breakfast'):
            await asyncio.sleep(2)

            await page.waitForSelector('.ChoosenMeal')
            meal = await page.querySelector('.ChoosenMeal')
            meal = await page.evaluate('(element) => element.textContent', meal)

            if meal != 'Breakfast':
                try:
                    swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                    await swapButton.click()
                except:
                    print("Swap Button Not Found")
                    pass

                dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
                await dropDown.click()

                try:
                    breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                    await breakfastOption.click()
                except:
                    await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

                await doneButton.click()
                await page.waitForSelector('.ChoosenMeal', timeout=60000)

                await asyncio.sleep(2)
                
            await scrape_food('//*[@id="9135"]', 'Daily Root')
            await scrape_food('//*[@id="13988"]', 'Wok Station')
            await scrape_food('//*[@id="9139"]', 'Home Zone')
            await scrape_food('//*[@id="9141"]', 'Salad Bar')
            await scrape_food('//*[@id="9138"]', 'Grill')
            await scrape_food('//*[@id="9140"]', 'Pizza')
            await scrape_food('//*[@id="14484"]', 'Soups')
            await scrape_food('//*[@id="45028"]', 'True Balance')
                
    elif(requestedMeal == 'lunch'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
                
        await scrape_food('//*[@id="9135"]', 'Daily Root')
        await scrape_food('//*[@id="13988"]', 'Wok Station')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9137"]', 'Deli/Sweets')
        await scrape_food('//*[@id="9141"]', 'Salad Bar')
        await scrape_food('//*[@id="9136"]', 'Waffle Station')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
        await scrape_food('//*[@id="14484"]', 'Soups')
        await scrape_food('//*[@id="45028"]', 'True Balance')
        await scrape_food('//*[@id="46596"]', 'Weekly Bar Rotation')
        
        print("Lunch: ", food_dict)
        
    elif(requestedMeal == 'dinner'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
            
        await scrape_food('//*[@id="9135"]', 'Daily Root')
        await scrape_food('//*[@id="13988"]', 'Wok Station')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9141"]', 'Salad Bar')
        await scrape_food('//*[@id="9136"]', 'Waffle Station')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
        await scrape_food('//*[@id="14484"]', 'Soups')
        await scrape_food('//*[@id="45028"]', 'True Balance')
        await scrape_food('//*[@id="46596"]', 'Weekly Bar Rotation')
        
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)
        
        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
        
        
        await scrape_food('//*[@id="13988"]', 'Wok Station')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9141"]', 'Salad Bar')
        await scrape_food('//*[@id="9136"]', 'Waffle Station')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
        await scrape_food('//*[@id="45028"]', 'True Balance')
        
        
        
    await browser.close()
    return food_dict 

async def pitchforksReq(requestedMeal):
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/Tempe-Campus/TempePitchforksRestaurant')
    
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
            food_elements = await food_element.querySelectorAll('div.sc-kdBSHD.gQLTsY > button > h3 > span')
            
            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
        
    
    if(requestedMeal == 'breakfast'):

        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Breakfast':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
            
        await scrape_food('//*[@id="14584"]', 'International')
        await scrape_food('//*[@id="17302"]', 'Vegan')
        await scrape_food('//*[@id="17305"]', 'Soups')
        await scrape_food('//*[@id="26390"]', 'Waffle Station & Ice Cream')
        await scrape_food('//*[@id="45017"]', 'True Balance')
            
        
    elif(requestedMeal == 'lunch'):

        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

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
            
            
    elif(requestedMeal == 'dinner'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

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
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
        
        await scrape_food('//*[@id="14584"]', 'International')
        await scrape_food('//*[@id="17302"]', 'Vegan')
        await scrape_food('//*[@id="17305"]', 'Soups')
        await scrape_food('//*[@id="45017"]', 'True Balance')
    
    await browser.close()
    return food_dict

async def hassyReq(requestedMeal):
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/Tempe-Campus/TempeHassayampaDiningCenter')
    
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
            food_elements = await food_element.querySelectorAll('div.sc-kdBSHD.gQLTsY > button > h3 > span')

            foods = []
            
            for food in food_elements:
                food_text = await page.evaluate('(element) => element.textContent', food)
                if food_text:
                    foods.append(food_text)
                
            food_dict.update({key: foods})
        except:
            pass
    
    if(requestedMeal == 'breakfast'):
        
        await asyncio.sleep(2)


        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Breakfast':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
        
        await scrape_food('//*[@id="30687"]', 'Daily Root')
        await scrape_food('//*[@id="9113"]', 'Salad Bar')
        await scrape_food('//*[@id="42068"]', 'Home Station')
        await scrape_food('//*[@id="42074"]', 'Smokehouse & Grill')
        await scrape_food('//*[@id="42070"]', 'True Balance')
        print("Breakfast: ", food_dict)
    
    elif(requestedMeal == 'lunch'):
        print('lunch')
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

            print(4)
        
        await scrape_food('//*[@id="30687"]', 'Daily Root')
        await scrape_food('//*[@id="9113"]', 'Salad Bar')
        await scrape_food('//*[@id="42071"]', 'Deli Station')
        await scrape_food('//*[@id="42068"]', 'Home Station')
        await scrape_food('//*[@id="42075"]', 'Kosher Bistro')
        await scrape_food('//*[@id="42072"]', 'Pizza Oven')
        await scrape_food('//*[@id="42074"]', 'Smokehouse & Grill')
        await scrape_food('//*[@id="42070"]', 'True Balance')
        print("Lunch: ", food_dict)
    
    elif(requestedMeal == 'dinner'):
            
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Dinner':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Dinner"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

        await scrape_food('//*[@id="30687"]', 'Daily Root')
        await scrape_food('//*[@id="9113"]', 'Salad Bar')
        await scrape_food('//*[@id="42071"]', 'Deli Station')
        await scrape_food('//*[@id="42068"]', 'Home Station')
        await scrape_food('//*[@id="42075"]', 'Kosher Bistro')
        await scrape_food('//*[@id="42072"]', 'Pizza Oven')
        await scrape_food('//*[@id="42074"]', 'Smokehouse & Grill')
        await scrape_food('//*[@id="42070"]', 'True Balance')
        
        print("Dinner: ", food_dict)
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)

        await page.waitForSelector('.ChoosenMeal')
        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                print("Swap Button Not Found")
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[1]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="30687"]', 'Daily Root')
        await scrape_food('//*[@id="9113"]', 'Salad Bar')
        await scrape_food('//*[@id="42071"]', 'Deli Station')
        await scrape_food('//*[@id="42068"]', 'Home Station')
        await scrape_food('//*[@id="42072"]', 'Pizza Oven')
        await scrape_food('//*[@id="42074"]', 'Smokehouse & Grill')
        await scrape_food('//*[@id="42070"]', 'True Balance')
        print("Brunch: ", food_dict)
    
    await browser.close()
    return food_dict

'''
async def checkTime():
    while True:  # Infinite loop to ensure it runs daily
        now = datetime.now()
        # Determine if it's before or after the target time (8 AM minus processing time)
        if now.hour < 21 or (now.hour == 21 and now.minute < 59):
            # If before 7:55 AM, set `then` to today at 7:55 AM
            then = now.replace(hour=21, minute=57, second=0, microsecond=0)
        else:
            # If after 7:55 AM, set `then` to tomorrow at 7:55 AM
            next_day = now + timedelta(days=1)
            then = next_day.replace(hour=21, minute=59, second=0, microsecond=0)
        
        # Calculate wait time in seconds
        wait_time = (then - now).total_seconds()
        # Wait until 5 minutes before 8 AM
        await asyncio.sleep(wait_time)

        # It's now 5 minutes before 8 AM, start the scraping process
        current_day = datetime.now().weekday()  # Ensure to get the current day here
        print("Scraping Started at 7:55 AM")
        
        if((current_day == 5) or (current_day == 6)):
        
            tookerBrunch = await tookerReq('brunch')
            
            manzyBrunch = await manzyReq('brunch')
            
            hassyBrunch = await hassyReq('brunch')
            
            barrettBrunch = await barrettReq('brunch')
            
            pitchforksBrunch = await pitchforksReq('brunch')
        
        else:
            print("Weekday Scraping")
            
            tookerBreakfast = await tookerReq('breakfast')
            tookerLunch = await tookerReq('lunch')
            
            manzyBreakfast = await manzyReq('breakfast')
            manzyLunch = await manzyReq('lunch')
            
            pitchforksBreakfast = await pitchforksReq('breakfast')
            pitchforksLunch = await pitchforksReq('lunch')
            
            hassyBreakfast = await hassyReq('breakfast')
            hassyLunch = await hassyReq('lunch')
            
            barrettBreakfast = await barrettReq('breakfast')
            barrettLunch = await barrettReq('lunch')

            
            tookerDinner = await tookerReq('dinner')

            manzyDinner = await manzyReq('dinner')
            
            pitchforksDinner = await pitchforksReq('dinner')
            
            hassyDinner = await hassyReq('dinner')
            
            barrettDinner = await barrettReq('dinner')
'''
        

async def checkTime():
    
    

    while True:
        now = datetime.now()
        then = now.replace(hour=8, minute = 00, second=0, microsecond=0)  # Target time at 10:05 PM

        # If it's already past 10:05 PM, set `then` to 10:05 PM the next day.
        if now > then:
            then += timedelta(days=1)

        wait_time = (then - now).total_seconds()
        print(f"Waiting for {wait_time} seconds.")
        await asyncio.sleep(wait_time)
    
    
        current_day = now.weekday()

        print("Scraping Started")

        if((current_day == 4) or (current_day == 5) or (current_day == 6)):
            
            global tookerBrunch
            tookerBrunch = await tookerReq('brunch')
            
            print("Tooker Br Scraping Completed")
            
            global manzyBrunch 
            manzyBrunch = await manzyReq('brunch')
            
            print("Manzy B/R Scraping Completed")
            
            global hassyBrunch 
            hassyBrunch = await hassyReq('brunch')
            
            print("Hassy B/R Scraping Completed")
            
            global barrettBrunch 
            barrettBrunch = await barrettReq('brunch')
            
            print("Barrett B/R Scraping Completed")
            
            global pitchforksBrunch 
            pitchforksBrunch = await pitchforksReq('brunch')
            
            print("Pitchforks B/R Scraping Completed")
            
        else:
            print("Weekday Scraping")
            
            global tookerBreakfast
            tookerBreakfast = await tookerReq('breakfast')
            
            
            global tookerLunch
            tookerLunch = await tookerReq('lunch')
            
            print("Tooker B/L Scraping Completed")
            
            global manzyBreakfast
            manzyBreakfast = await manzyReq('breakfast')
            
            global manzyLunch 
            manzyLunch = await manzyReq('lunch')
            
            
            
            print("Manzy B/L Scraping Completed")
            
            global pitchforksBreakfast
            pitchforksBreakfast = await pitchforksReq('breakfast')
            
            global pitchforksLunch
            pitchforksLunch = await pitchforksReq('lunch')
            
            
            
            print("Pitchforks B/L Scraping Completed")
            
            global hassyBreakfast
            hassyBreakfast = await hassyReq('breakfast')
            
            global hassyLunch
            hassyLunch = await hassyReq('lunch')
            
            
            
            print("Hassy B/L Scraping Completed")
            
            global barrettBreakfast 
            barrettBreakfast = await barrettReq('breakfast')
            
            global barrettLunch
            barrettLunch = await barrettReq('lunch')
            
            
            
            print("Barrett B/L Scraping Completed")
        
        global tookerDinner
        tookerDinner = await tookerReq('dinner')
        
        print("Tooker D Scraping Completed")
        
        global manzyDinner
        manzyDinner = await manzyReq('dinner')
        
        print("Manzy D Scraping Completed")

        global barrettDinner
        barrettDinner = await barrettReq('dinner') 
        
        print("Barrett D Scraping Completed")
        
        global hassyDinner
        hassyDinner = await hassyReq('dinner')
        
        print("Hassy D Scraping Completed")
        
        global pitchforksDinner
        pitchforksDinner = await pitchforksReq('dinner')
        
        print("Pitchforks D Scraping Completed")
                



@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running')
    await checkTime()

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    exit()     
    
@bot.command(name='tooker')
async def tooker(ctx, arg1):
    
    # print("\n\n")
    # print(tookerBreakfast)
    # print("\n\n")
    # print(tookerLunch)
    # print("\n\n")
    # print(tookerDinner)
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        embed = discord.Embed(title='Tooker House Breakfast', description= 'Tooker House Breakfast Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
        
        try:
            dailyRoot = tookerBreakfast['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            homeZone = tookerBreakfast['Home Zone']
            homeZone = ', '.join(homeZone)  
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            trueBalance = tookerBreakfast['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
        
        
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
        
        
        
        
        embed = discord.Embed(title='Tooker House Lunch', description= 'Tooker House Lunch Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
        
        try:
            dailyRoot = tookerLunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            
            homeZone = tookerLunch['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            
            trueBalance = tookerLunch['True Balance']
            trueBalance = ', '.join(trueBalance)   
            embed.add_field(name='True Balance:', value=trueBalance, inline=False) 
        except:
            pass
        
        try:
            grill = tookerLunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = tookerLunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            soup = tookerLunch['Soup']
            soup = ', '.join(soup)
            embed.add_field(name='Soup', value=soup, inline=False)        
        except:
            pass
        
        try:
            shawarma = ['Falafel Pita']
            shawarma = ', '.join(shawarma)
            embed.add_field(name='Shawarma Station', value=shawarma, inline=True)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
        
    elif(arg1.lower() == 'dinner'):
        
        
        embed = discord.Embed(title='Tooker House Dinner', description= 'Tooker House Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
        
        try:
            dailyRoot = tookerDinner['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            homeZone = tookerDinner['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            trueBalance = tookerDinner['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            grill = tookerDinner['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = tookerDinner['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            soup = tookerDinner['Soup']
            soup = ', '.join(soup)
            embed.add_field(name='Soup', value=soup, inline=False)
        except:
            pass
        
        try:
            shawarma = ['Chicken Shawarma Pita', 'Falafel Pita']
            shawarma = ', '.join(shawarma)
            embed.add_field(name='Shawarma Station', value=shawarma, inline=True)
        except:
            pass

        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
        
    elif(arg1.lower() == 'brunch'):
        
        if(current_day != 4 and current_day != 5 and current_day != 6):
            await ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        embed = discord.Embed(title='Tooker House Brunch', description= 'Tooker House Brunch Menu')

        embed.set_thumbnail(url="https://i.imgur.com/AKpXgNY.png")
        
        try:
            dailyRoot = tookerBrunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            homeZone = tookerBrunch['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            trueBalance = tookerBrunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            grill = tookerBrunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = tookerBrunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
    else:
        await ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)

@bot.command(name='manzanita', aliases=['manzy'])
async def manzy(ctx, arg1):
    
    # print("\n\n")
    # print(manzyBrunch)
    # print("\n\n")
    # print(manzyLunch)
    # print("\n\n")
    # print(manzyDinner)
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        
        
        embed = discord.Embed(title='Manzanita Dining Hall Breakfast', description= 'Manzanita Dining Hall Breakfast Menu')
        
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            dailyRoot = manzyBreakfast['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            wokStation = manzyBreakfast['Wok Station']
            wokStation = ', '.join(wokStation)
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            homeZone = manzyBreakfast['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            saladBar = manzyBreakfast['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            grill = manzyBreakfast['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = manzyBreakfast['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            soup = manzyBreakfast['Soups']
            soup = ', '.join(soup)
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            trueBalance = manzyBreakfast['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
    
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
        
        embed = discord.Embed(title='Manzanita Dining Hall Lunch', description= 'Manzanita Dining Hall Lunch Menu')
        
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            dailyRoot = manzyLunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            wokStation = manzyLunch['Wok Station']
            wokStation = ', '.join(wokStation)
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            homeZone = manzyLunch['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            deliSweets = manzyLunch['Deli/Sweets']
            deliSweets = ', '.join(deliSweets)
            embed.add_field(name='Deli/Sweets', value=deliSweets, inline=False)
        except:
            pass
        
        try:
            saladBar = manzyDinner['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            waffleStation = manzyLunch['Waffle Station']
            waffleStation = ', '.join(waffleStation)
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
        except:
            pass
        
        try:
            grill = manzyLunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = manzyLunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            sazonStation = manzyLunch['Sazon Station']
            sazonStation = ', '.join(sazonStation)
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            soup = manzyLunch['Soups']
            soup = ', '.join(soup)
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            trueBalance = manzyLunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            weeklyBarRotation = manzyLunch['Weekly Bar Rotation']
            weeklyBarRotation = ', '.join(weeklyBarRotation)
            embed.add_field(name='Weekly Bar Rotation', value=weeklyBarRotation, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
        
        
    elif(arg1.lower() == 'dinner'):
        
        embed = discord.Embed(title='Manzanita Dining Hall Dinner', description= 'Manzanita Dining Hall Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            dailyRoot = manzyDinner['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            wokStation = manzyDinner['Wok Station']
            wokStation = ', '.join(wokStation)
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            homeZone = manzyDinner['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            deliSweets = manzyDinner['Deli/Sweets']
            deliSweets = ', '.join(deliSweets)
            embed.add_field(name='Deli/Sweets', value=deliSweets, inline=False)
        except:
            pass
        
        try:
            saladBar = manzyDinner['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            waffleStation = manzyDinner['Waffle Station']
            waffleStation = ', '.join(waffleStation)
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
        except:
            pass
        
        try:
            grill = manzyDinner['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = manzyDinner['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            sazonStation = manzyDinner['Sazon Station']
            sazonStation = ', '.join(sazonStation)
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            soup = manzyDinner['Soups']
            soup = ', '.join(soup)
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            trueBalance = manzyDinner['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            weeklyBarRotation = manzyDinner['Weekly Bar Rotation']
            weeklyBarRotation = ', '.join(weeklyBarRotation)
            embed.add_field(name='Weekly Bar Rotation', value=weeklyBarRotation, inline=False)
        except:
            pass
        

        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
    
    elif(arg1.lower() == 'brunch'):
        if(current_day != 4 and current_day != 5 and current_day != 6):
            await ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return

        
        embed = discord.Embed(title='Manzanita Dining Hall Brunch', description= 'Manzanita Dining Hall Brunch Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            dailyRoot = manzyBrunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            wokStation = manzyBrunch['Wok Station']
            wokStation = ', '.join(wokStation)
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            homeZone = manzyBrunch['Home Zone']
            homeZone = ', '.join(homeZone)
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            saladBar = manzyBrunch['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            waffleStation = manzyBrunch['Waffle Station']
            waffleStation = ', '.join(waffleStation)
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
        except:
            pass
        
        try:
            grill = manzyBrunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name='Grill', value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = manzyBrunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name='Pizza', value=pizza, inline=True)
        except:
            pass
        
        try:
            sazonStation = manzyBrunch['Sazon Station']
            sazonStation = ', '.join(sazonStation)
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            trueBalance = manzyBrunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
        
    else:
        await ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)


@bot.command(name='hassayampa', aliases=['hassy'])
async def hassy(ctx, arg1):
    
    # print("\n\n")
    # print(hassyBreakfast)
    # print("\n\n")
    # print(hassyLunch)
    # print("\n\n")
    # print(hassyDinner)
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        embed = discord.Embed(title='Hassayampa Dining Hall Breakfast', description= 'Hassayampa Dining Hall Breakfast Menu')
        
        embed.set_thumbnail(url="https://imgur.com/a/HTJJsSe")
        
        try:
            dailyRoot = hassyBreakfast['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            saladBar = hassyBreakfast['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            homeStation = hassyBreakfast['Home Station']
            homeStation = ', '.join(homeStation)
            embed.add_field(name="Home Station:", value=homeStation, inline=False)
        except:
            pass
        
        try:
            smokehouse = hassyBreakfast['Smokehouse & Grill']
            smokehouse = ', '.join(smokehouse)
            embed.add_field(name="Smokehouse & Grill:", value=smokehouse, inline=False)
        except:
            pass
        
        try:
            trueBalance = hassyBreakfast['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/TEkqYiC")
        
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
        
        
        
        embed = discord.Embed(title='Hassayampa Dining Hall Lunch', description= 'Hassayampa Dining Hall Lunch Menu')
        
        embed.set_thumbnail(url="https://imgur.com/a/HTJJsSe")
        
        try:
            dailyRoot = hassyLunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            saladBar = hassyLunch['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            deliStation = hassyLunch['Deli Station']
            deliStation = ', '.join(deliStation)
            embed.add_field(name="Deli Station:", value=deliStation, inline=False)
        except:
            pass
        
        try:
            homeStation = hassyLunch['Home Station']
            homeStation = ', '.join(homeStation)
            embed.add_field(name="Home Station:", value=homeStation, inline=False)
        except:
            pass
        
        try:
            kosherBistro = hassyLunch['Kosher Bistro']
            kosherBistro = ', '.join(kosherBistro)
            embed.add_field(name="Kosher Bistro:", value=kosherBistro, inline=False)
        except:
            pass
        
        try:
            pizzaOven = hassyLunch['Pizza Oven']
            pizzaOven = ', '.join(pizzaOven)
            embed.add_field(name="Pizza Oven:", value=pizzaOven, inline=False)
        except:
            pass
        
        try:
            smokehouse = hassyLunch['Smokehouse & Grill']
            smokehouse = ', '.join(smokehouse)
            embed.add_field(name="Smokehouse & Grill:", value=smokehouse, inline=False)
        except:
            pass
        
        try:
            trueBalance = hassyLunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/TEkqYiC")
    
    elif(arg1.lower() == 'dinner'):
        
        embed = discord.Embed(title='Hassayampa Dining Hall Dinner', description= 'Hassayampa Dining Hall Dinner Menu')
        embed.set_thumbnail(url="https://imgur.com/a/HTJJsSe")
        
        try:
            dailyRoot = hassyDinner['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            saladBar = hassyDinner['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            deliStation = hassyDinner['Deli Station']
            deliStation = ', '.join(deliStation)
            embed.add_field(name="Deli Station:", value=deliStation, inline=False)
        except:
            pass
        
        try:
            homeStation = hassyDinner['Home Station']
            homeStation = ', '.join(homeStation)
            embed.add_field(name="Home Station:", value=homeStation, inline=False)
        except:
            pass
        
        try:
            kosherBistro = hassyDinner['Kosher Bistro']
            kosherBistro = ', '.join(kosherBistro)
            embed.add_field(name="Kosher Bistro:", value=kosherBistro, inline=False)
        except:
            pass
        
        try:
            pizzaOven = hassyDinner['Pizza Oven']
            pizzaOven = ', '.join(pizzaOven)
            embed.add_field(name="Pizza Oven:", value=pizzaOven, inline=False)
        except:
            pass
        
        try:
            smokehouse = hassyDinner['Smokehouse & Grill']
            smokehouse = ', '.join(smokehouse)
            embed.add_field(name="Smokehouse & Grill:", value=smokehouse, inline=False)
        except:
            pass
        
        try:
            trueBalance = hassyDinner['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/TEkqYiC")
    
    elif(arg1.lower() =='brunch'):
        
        if(current_day != 4 and current_day != 5 and current_day != 6):
            await ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        embed = discord.Embed(title='Hassayampa Dining Hall Brunch', description= 'Hassayampa Dining Hall Brunch Menu')
        embed.set_thumbnail(url="https://imgur.com/a/HTJJsSe")
        
        try:
            dailyRoot = hassyBrunch['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            saladBar = hassyBrunch['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            deliStation = hassyBrunch['Deli Station']
            deliStation = ', '.join(deliStation)
            embed.add_field(name="Deli Station:", value=deliStation, inline=False)
        except:
            pass
        
        try:
            homeStation = hassyBrunch['Home Station']
            homeStation = ', '.join(homeStation)
            embed.add_field(name="Home Station:", value=homeStation, inline=False)
        except:
            pass
        
        try:
            pizzaOven = hassyBrunch['Pizza Oven']
            pizzaOven = ', '.join(pizzaOven)
            embed.add_field(name="Pizza Oven:", value=pizzaOven, inline=False)
        except:
            pass
        
        try:
            smokehouse = hassyBrunch['Smokehouse & Grill']
            smokehouse = ', '.join(smokehouse)
            embed.add_field(name="Smokehouse & Grill:", value=smokehouse, inline=False)
        except:
            pass
        
        try:
            trueBalance = hassyBrunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/TEkqYiC")
        
    else:
        await ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)
        

@bot.command(name='barrett')
async def barret(ctx, arg1):
       
    # print("\n\n")
    # print(barrettBreakfast)
    # print("\n\n")
    # print(barrettLunch)
    # print("\n\n")
    # print(barrettDinner)
        
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        
        embed = discord.Embed(title='Barrett Dining Hall Breakfast', description= 'Barrett Dining Hall Breakfast Menu')
        embed.set_thumbnail(url="https://imgur.com/a/slcg2XT")
        
        try:
            saladBar = barrettBreakfast['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            grill = barrettBreakfast['Grill']
            grill = ', '.join(grill)
            embed.add_field(name="Grill:", value=grill, inline=False)
        except:
            pass
        
        try:
            trueBalance = barrettBreakfast['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        try:
            dailyRoot = barrettBreakfast['The Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="The Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            dessert = barrettBreakfast['Dessert/Waffle']
            dessert = ', '.join(dessert)
            embed.add_field(name="Dessert/Waffle:", value=dessert, inline=False)
        except:
            pass
        
        try:
            omelets = barrettBreakfast['Omelets']
            omelets = ', '.join(omelets)
            embed.add_field(name="Omelets:", value=omelets, inline=False)
        except:
            pass
        
        embed.set_image(url="https://https://imgur.com/a/GpBTJPA")
    
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 5 and current_day == 6):
            await ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        embed = discord.Embed(title='Barrett Dining Hall Lunch', description= 'Barrett Dining Hall Lunch Menu')
        embed.set_thumbnail(url="https://imgur.com/a/slcg2XT")
        
        try:
            homeZone1 = barrettLunch['Home Zone 1']
            homeZone1 = ', '.join(homeZone1)
            embed.add_field(name="Home Zone 1:", value=homeZone1, inline=False)
        except:
            pass
        
        try:
            deli = barrettLunch['Deli']
            deli = ', '.join(deli)
            embed.add_field(name="Deli:", value=deli, inline=False)
        except:
            pass
        
        try:
            saladBar = barrettLunch['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            grill = barrettLunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name="Grill:", value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = barrettLunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name="Pizza:", value=pizza, inline=False)
        except:
            pass
        
        try:
            trueBalance = barrettLunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        try:
            dailyRoot = barrettLunch['The Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="The Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            soup = barrettLunch['Soup Station']
            soup = ', '.join(soup)
            embed.add_field(name="Soup Station:", value=soup, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/GpBTJPA")
        
    elif(arg1.lower() == 'dinner'):
        
        
        embed = discord.Embed(title='Barrett Dining Hall Dinner', description= 'Barrett Dining Hall Dinner Menu')
        embed.set_thumbnail(url="https://imgur.com/a/slcg2XT")
        
        try:
            homeZone1 = barrettDinner['Home Zone 1']
            homeZone1 = ', '.join(homeZone1)
            embed.add_field(name="Home Zone 1:", value=homeZone1, inline=False)
        except:
            pass
        
        try:
            deli = barrettDinner['Deli']
            deli = ', '.join(deli)
            embed.add_field(name="Deli:", value=deli, inline=False)
        except:
            pass
        
        try:
            saladBar = barrettDinner['Salad Bar']
            saladBar = ', '.join(saladBar)
            embed.add_field(name="Salad Bar:", value=saladBar, inline=False)
        except:
            pass
        
        try:
            grill = barrettDinner['Grill']
            grill = ', '.join(grill)
            embed.add_field(name="Grill:", value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = barrettDinner['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name="Pizza:", value=pizza, inline=False)
        except:
            pass
        
        try:
            trueBalance = barrettDinner['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        try:
            dailyRoot = barrettDinner['The Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="The Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            soup = barrettDinner['Soup Station']
            soup = ', '.join(soup)
            embed.add_field(name="Soup Station:", value=soup, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/GpBTJPA")
    
    elif(arg1.lower() == 'brunch'):
        
        if(current_day != 4 and current_day != 5 and current_day != 6):
            await ctx.send("This dining hall is not serving Brunch today, try requesting Lunch or Breakfast instead")
            return
            
        
        embed = discord.Embed(title='Barrett Dining Hall Dinner', description= 'Barrett Dining Hall Dinner Menu')
        embed.set_thumbnail(url="https://imgur.com/a/slcg2XT")
        
        try:
            homeZone1 = barrettBrunch['Home Zone 1']
            homeZone1 = ', '.join(homeZone1)
            embed.add_field(name="Home Zone 1:", value=homeZone1, inline=False)
        except:
            pass
        
        try:
            grill = barrettBrunch['Grill']
            grill = ', '.join(grill)
            embed.add_field(name="Grill:", value=grill, inline=False)
        except:
            pass
        
        try:
            pizza = barrettBrunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name="Pizza:", value=pizza, inline=False)
        except:
            pass
        
        try:
            trueBalance = barrettBrunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        try:
            dailyRoot = barrettBrunch['The Daily Root']
            dailyRoot = ', '.join(dailyRoot)
            embed.add_field(name="The Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/a/GpBTJPA")
        
    else:
        await ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)
    

@bot.command(name='pitchforks', aliases=['MU', 'memorial union'])
async def pitchforks(ctx, arg1):
    
    # print("\n\n")
    # print(pitchforksBreakfast)
    # print("\n\n")
    # print(pitchforksLunch)
    # print("\n\n")
    # print(pitchforksDinner)
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        embed = discord.Embed(title='Pitchforks Dining Hall Breakfast', description= 'Pitchforks Dining Hall Breakfast Menu')
        embed.set_thumbnail(url="https://imgur.com/FvCWGxy")
        
        try:
            international = pitchforksBreakfast['International']
            international = ', '.join(international)
            embed.add_field(name="International:", value=international, inline=False)
        except:
            pass
        
        try:
            vegan = pitchforksBreakfast['Vegan']
            vegan = ', '.join(vegan)
            embed.add_field(name="Vegan:", value=vegan, inline=False)
        except:
            pass
        
        try:
            soups = pitchforksBreakfast['Soups']
            soups = ', '.join(soups)
            embed.add_field(name="Soups:", value=soups, inline=False)
        except:
            pass
        
        try:
            waffle = pitchforksBreakfast['Waffle Station & Ice Cream']
            waffle = ', '.join(waffle)
            embed.add_field(name="Waffle Station & Ice Cream:", value=waffle, inline=False)
        except:
            pass
        
        try:
            trueBalance = pitchforksBreakfast['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/hlzODkP")
    
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 4 or current_day == 5 or current_day == 6):
            await ctx.send("This dining hall is not serving Lunch today, try requesting Breakfast instead")
            return
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        embed = discord.Embed(title='Pitchforks Dining Hall Lunch', description= 'Pitchforks Dining Hall Lunch Menu')
        embed.set_thumbnail(url="https://imgur.com/FvCWGxy")
        
        try:
            salad = pitchforksLunch['Salad & Deli']
            salad = ', '.join(salad)
            embed.add_field(name="Salad & Deli:", value=salad, inline=False)
        except:
            pass
        
        try:
            international = pitchforksLunch['International']
            international = ', '.join(international)
            embed.add_field(name="International:", value=international, inline=False)
        except:
            pass
        
        try:
            vegan = pitchforksLunch['Vegan']
            vegan = ', '.join(vegan)
            embed.add_field(name="Vegan:", value=vegan, inline=False)
        except:
            pass
        
        try:
            pizza = pitchforksLunch['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name="Pizza:", value=pizza, inline=False)
        except:
            pass
        
        try:
            asian = pitchforksLunch['Asian']
            asian = ', '.join(asian)
            embed.add_field(name="Asian:", value=asian, inline=False)
        except:
            pass
        
        try:
            limon = pitchforksLunch['Limon']
            limon = ', '.join(limon)
            embed.add_field(name="Limon:", value=limon, inline=False)
        except:
            pass
        
        try:
            soups = pitchforksLunch['Soups']
            soups = ', '.join(soups)
            embed.add_field(name="Soups:", value=soups, inline=False)
        except:
            pass
        
        try:
            trueBalance = pitchforksLunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/hlzODkP")
        
    
    elif(arg1.lower() == 'dinner'):
        
        
        embed = discord.Embed(title='Pitchforks Dining Hall Dinner', description= 'Pitchforks Dining Hall Dinner Menu')
        embed.set_thumbnail(url="https://imgur.com/FvCWGxy")
        
        try:
            salad = pitchforksDinner['Salad & Deli']
            salad = ', '.join(salad)
            embed.add_field(name="Salad & Deli:", value=salad, inline=False)
        except:
            pass
        
        try:
            international = pitchforksDinner['International']
            international = ', '.join(international)
            embed.add_field(name="International:", value=international, inline=False)
        except:
            pass
        
        try:
            vegan = pitchforksDinner['Vegan']
            vegan = ', '.join(vegan)
            embed.add_field(name="Vegan:", value=vegan, inline=False)
        except:
            pass
        
        try:
            pizza = pitchforksDinner['Pizza']
            pizza = ', '.join(pizza)
            embed.add_field(name="Pizza:", value=pizza, inline=False)
        except:
            pass
        
        try:
            asian = pitchforksDinner['Asian']
            asian = ', '.join(asian)
            embed.add_field(name="Asian:", value=asian, inline=False)
        except:
            pass
        
        try:
            limon = pitchforksDinner['Limon']
            limon = ', '.join(limon)
            embed.add_field(name="Limon:", value=limon, inline=False)
        except:
            pass
        
        try:
            soups = pitchforksDinner['Soups']
            soups = ', '.join(soups)
            embed.add_field(name="Soups:", value=soups, inline=False)
        except:
            pass
        
        try:
            trueBalance = pitchforksDinner['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/hlzODkP")
    
    elif(arg1.lower() == 'brunch'):
        
        if(current_day != 4 and current_day != 5 and current_day != 6):
            await ctx.send("This dining hall is not serving Brunch today, try requesting Lunch or Breakfast instead")
            return
        
        embed = discord.Embed(title='Pitchforks Dining Hall Brunch', description= 'Pitchforks Dining Hall Brunch Menu')
        embed.set_thumbnail(url="https://imgur.com/FvCWGxy")
        
        try:
            international = pitchforksBrunch['International']
            international = ', '.join(international)
            embed.add_field(name="International:", value=international, inline=False)
        except:
            pass
        
        try:
            vegan = pitchforksBrunch['Vegan']
            vegan = ', '.join(vegan)
            embed.add_field(name="Vegan:", value=vegan, inline=False)
        except:
            pass
        
        try:
            soups = pitchforksBrunch['Soups']
            soups = ', '.join(soups)
            embed.add_field(name="Soups:", value=soups, inline=False)
        except:
            pass
        
        try:
            trueBalance = pitchforksBrunch['True Balance']
            trueBalance = ', '.join(trueBalance)
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://imgur.com/hlzODkP")
    
    else:
        await ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)


bot.run(TOKEN)


    
