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



async def barrettReq(requestedMeal):
    
    browser = await launch()
    page = await browser.newPage()
    
    page.setDefaultNavigationTimeout(60000)
    await page.goto('https://asu.campusdish.com/DiningVenues/TempeBarrettDiningCenter')
    
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
    
    if(requestedMeal == 'breakfast'):
        
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
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
                await print("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)
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
                await print("Sorry but it does not appear that there is a Dinner option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
                await print("Sorry but it does not appear that there is a Brunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
    
    if(requestedMeal == 'breakfast'):
        
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
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)

    
        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="30185"]', 'True Balance')
        print("Breakfast: ", food_dict)
            
    elif(requestedMeal == 'lunch'):
        print('lunch')
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                print(1)
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
            await dropDown.click()

            try:
                print(2)
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)
            print(3)
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
                await print("Sorry but it does not appear that there is a Dinner option today at Tooker dining...")

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
        print("Dinner: ", food_dict)
    
    elif(requestedMeal == 'brunch'):
        
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
                await print("Sorry but it does not appear that there is a Brunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
    
    if(requestedMeal == 'breakfast'):
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
                    await print("Sorry but it does not appear that there is a Breakfast option today at Manzanita dining...")

                doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            print('swapping to lunch')
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
                print('swap button clicked')
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
            await dropDown.click()
            print('drop down clicked')

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
                print('lunch option clicked')
            except:
                await print("Sorry but it does not appear that there is a Lunch option today at Manzanita dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)
            print('done button clicked')
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
                await print("Sorry but it does not appear that there is a Dinner option today at Manzanita dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)
        
        if meal != 'Brunch':
            try:
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Brunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Dinner option today at Manzanita dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
        await scrape_food('//*[@id="45028"]', 'True Balance')
        
        
        
    await browser.close()
    return food_dict 

async def pitchforksReq(requestedMeal):
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
        
    
    if(requestedMeal == 'breakfast'):

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
                await print("Sorry but it does not appear that there is a Breakfast option today at Pitchforks dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
                await print("Sorry but it does not appear that there is a Lunch option today at Pitchforks dining...")

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
            
            
    elif(requestedMeal == 'dinner'):
        
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
                await print("Sorry but it does not appear that there is a Breakfast option today at Pitchforks dining...")

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
    
    elif(requestedMeal == 'brunch'):
        
        await asyncio.sleep(2)

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Brunch':
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
                await print("Sorry but it does not appear that there is a Breakfast option today at Pitchforks dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
    await page.goto('https://asu.campusdish.com/DiningVenues/TempeHassayampaDiningCenter')
    
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
    
    if(requestedMeal == 'breakfast'):
        
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
                await print("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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

        meal = await page.querySelector('.ChoosenMeal')
        meal = await page.evaluate('(element) => element.textContent', meal)

        if meal != 'Lunch':
            try:
                print(1)
                swapButton = await page.waitForSelector('.DateMealFilterButton', timeout=5000)
                await swapButton.click()
            except:
                pass

            dropDown = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div', timeout=5000)
            await dropDown.click()

            try:
                print(2)
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                await print("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)
            print(3)
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
                await print("Sorry but it does not appear that there is a Dinner option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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
                await print("Sorry but it does not appear that there is a Brunch option today at Tooker dining...")

            doneButton = await page.waitForXPath('//*[@id="modal-root"]/div[2]/div/div/div/div[3]/button[2]', timeout=5000)

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



async def checkTime():

    now = datetime.now()
    then = now + timedelta(days=0)
    then = then.replace(hour=16, minute=10, second=0, microsecond=0)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    
    
    current_day = now.weekday()

    print("Scraping Started")

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
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        dailyRoot = tookerBreakfast['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        homeZone = tookerBreakfast['Home Zone']
        homeZone = ', '.join(homeZone)
        
        trueBalance = tookerBreakfast['True Balance']
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
        
        
    elif(arg1.lower() == 'lunch'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
        
        dailyRoot = tookerLunch['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        homeZone = tookerLunch['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = tookerLunch['Grill']
        grill = ', '.join(grill)
        
        pizza = tookerLunch['Pizza']
        pizza = ', '.join(pizza)
        
        soup = tookerLunch['Soup']
        soup = ', '.join(soup)
        
        trueBalance = tookerLunch['True Balance']
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
        
    elif(arg1.lower() == 'dinner'):
        
        dailyRoot = tookerDinner['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        homeZone = tookerDinner['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = tookerDinner['Grill']
        grill = ', '.join(grill)
        
        pizza = tookerDinner['Pizza']
        pizza = ', '.join(pizza)
        
        soup = tookerDinner['Soup']
        soup = ', '.join(soup)
        
        trueBalance = tookerDinner['True Balance']
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
        
    elif(arg1.lower() == 'brunch'):
        if(current_day != 5 and current_day != 6):
            ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        dailyRoot = tookerBrunch['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        homeZone = tookerBrunch['Home Zone']
        homeZone = ', '.join(homeZone)
        
        grill = tookerBrunch['Grill']
        grill = ', '.join(grill)
        
        pizza = tookerBrunch['Pizza']
        pizza = ', '.join(pizza)
        
        trueBalance = tookerBrunch['True Balance']
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
        
    else:
        ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)

@bot.command(name='manzanita', aliases=['manzy'])
async def manzy(ctx, arg1):
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        
        dailyRoot = manzyBreakfast['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        wokStation = manzyBreakfast['Wok Station']
        wokStation = ', '.join(wokStation)
        
        homeZone = manzyBreakfast['Home Zone']
        homeZone = ', '.join(homeZone)
        
        saladBar = manzyBreakfast['Salad Bar']
        saladBar = ', '.join(saladBar)
        
        grill = manzyBreakfast['Grill']
        grill = ', '.join(grill)
        
        pizza = manzyBreakfast['Pizza']
        pizza = ', '.join(pizza)
        
        soup = manzyBreakfast['Soups']
        soup = ', '.join(soup)
        
        trueBalance = manzyBreakfast['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        embed = discord.Embed(title='Manzanita Dining Hall Breakfast', description= 'Manzanita Dining Hall Breakfast Menu')
        
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
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
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
    
    elif(arg1.lower() == 'lunch'):
        
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        
        dailyRoot = manzyLunch['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        wokStation = manzyLunch['Wok Station']
        wokStation = ', '.join(wokStation)
        
        homeZone = manzyLunch['Home Zone']
        homeZone = ', '.join(homeZone)
        
        deliSweets = manzyLunch['Deli/Sweets']
        deliSweets = ', '.join(deliSweets)
        
        saladBar = manzyDinner['Salad Bar']
        saladBar = ', '.join(saladBar)
        
        waffleStation = manzyLunch['Waffle Station']
        waffleStation = ', '.join(waffleStation)
        
        grill = manzyLunch['Grill']
        grill = ', '.join(grill)
        
        pizza = manzyLunch['Pizza']
        pizza = ', '.join(pizza)
        
        sazonStation = manzyLunch['Sazon Station']
        sazonStation = ', '.join(sazonStation)
        
        soup = manzyLunch['Soups']
        soup = ', '.join(soup)
        
        trueBalance = manzyLunch['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        weeklyBarRotation = manzyLunch['Weekly Bar Rotation']
        weeklyBarRotation = ', '.join(weeklyBarRotation)
        
        embed = discord.Embed(title='Manzanita Dining Hall Lunch', description= 'Manzanita Dining Hall Lunch Menu')
        
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Deli/Sweets', value=deliSweets, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
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
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Weekly Bar Rotation', value=weeklyBarRotation, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
        
        
    elif(arg1.lower() == 'dinner'):
        
        
        dailyRoot = manzyDinner['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        wokStation = manzyDinner['Wok Station']
        wokStation = ', '.join(wokStation)
        
        homeZone = manzyDinner['Home Zone']
        homeZone = ', '.join(homeZone)
        
        deliSweets = manzyDinner['Deli/Sweets']
        deliSweets = ', '.join(deliSweets)
        
        saladBar = manzyDinner['Salad Bar']
        saladBar = ', '.join(saladBar)
        
        waffleStation = manzyDinner['Waffle Station']
        waffleStation = ', '.join(waffleStation)
        
        grill = manzyDinner['Grill']
        grill = ', '.join(grill)
        
        pizza = manzyDinner['Pizza']
        pizza = ', '.join(pizza)
        
        sazonStation = manzyDinner['Sazon Station']
        sazonStation = ', '.join(sazonStation)
        
        soup = manzyDinner['Soups']
        soup = ', '.join(soup)
        
        trueBalance = manzyDinner['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        weeklyBarRotation = manzyDinner['Weekly Bar Rotation']
        weeklyBarRotation = ', '.join(weeklyBarRotation)
        
        
        embed = discord.Embed(title='Manzanita Dining Hall Dinner', description= 'Manzanita Dining Hall Dinner Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Deli/Sweets', value=deliSweets, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
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
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Soups', value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Weekly Bar Rotation', value=weeklyBarRotation, inline=False)
        except:
            pass
        

        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
    
    elif(arg1.lower() == 'brunch'):
        if(current_day != 5 and current_day != 6):
            ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        dailyRoot = manzyBrunch['Daily Root']
        dailyRoot = ', '.join(dailyRoot)
        
        wokStation = manzyBrunch['Wok Station']
        wokStation = ', '.join(wokStation)
        
        homeZone = manzyBrunch['Home Zone']
        homeZone = ', '.join(homeZone)
        
        saladBar = manzyBrunch['Salad Bar']
        saladBar = ', '.join(saladBar)
        
        waffleStation = manzyBrunch['Waffle Station']
        waffleStation = ', '.join(waffleStation)
        
        grill = manzyBrunch['Grill']
        grill = ', '.join(grill)
        
        pizza = manzyBrunch['Pizza']
        pizza = ', '.join(pizza)
        
        sazonStation = manzyBrunch['Sazon Station']
        sazonStation = ', '.join(sazonStation)
        
        trueBalance = manzyBrunch['True Balance']
        trueBalance = ', '.join(trueBalance)
        
        embed = discord.Embed(title='Manzanita Dining Hall Brunch', description= 'Manzanita Dining Hall Brunch Menu')
    
        embed.set_thumbnail(url="https://i.imgur.com/DKR50qf.jpg")
        
        try:
            embed.add_field(name="Daily Root:", value=dailyRoot, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Wok Station:", value=wokStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Home Zone:", value=homeZone, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Salad Bar', value=saladBar, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='Waffle Station', value=waffleStation, inline=False)
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
            embed.add_field(name='Sazon Station', value=sazonStation, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name='True Balance:', value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/GSx3eR2.png")
        
    else:
        ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)





bot.run(TOKEN)


    
