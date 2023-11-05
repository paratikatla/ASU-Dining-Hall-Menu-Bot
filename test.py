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

bot = commands.Bot(command_prefix="?", intents=intents)



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
                
            await scrape_food('//*[@id="9135"]', 'Action')
            await scrape_food('//*[@id="9139"]', 'Home Zone')
            await scrape_food('//*[@id="9141"]', 'Salad Bar')
            await scrape_food('//*[@id="9138"]', 'Grill')
                
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
                
        await scrape_food('//*[@id="9135"]', 'Action')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
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
                
        await scrape_food('//*[@id="9135"]', 'Action')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')
    
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
            
            
        
    if(requestedMeal == 'lunch'):

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
        
        food_dict = await tookerReq('breakfast')
        
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
        
        
    elif(arg1.lower() == 'lunch'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
            
        food_dict = await tookerReq('lunch')
        
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
        
    elif(arg1.lower() == 'dinner'):
        
        food_dict = await tookerReq('dinner')
        
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
        
    elif(arg1.lower() == 'brunch'):
        if(current_day != 5 and current_day != 6):
            ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        food_dict = await tookerReq('brunch')
        
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
        
    else:
        ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)

@bot.command(name='Tooker')
async def Tooker(ctx, arg1):
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        food_dict = await tookerReq('breakfast')
        
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
        
        
    elif(arg1.lower() == 'lunch'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Lunch today, try requesting Brunch instead")
            return
            
        food_dict = await tookerReq('lunch')
        
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
        
    elif(arg1.lower() == 'dinner'):
        
        food_dict = await tookerReq('dinner')
        
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
        
    elif(arg1.lower() == 'brunch'):
        if(current_day != 5 and current_day != 6):
            ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
        food_dict = await tookerReq('brunch')
        
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
        
    else:
        ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)

# @bot.command(name='barrett')
# async def barrett(ctx, arg1):
    
#     now = datetime.now()
#     current_day = now.weekday()
    
#     if(arg1.lower() == 'breakfast'):
#         if(current_day == 5 or current_day == 6):
#             ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
#             return

#         food_dict = barrettReq('breakfast')
        
#     elif(arg1.lower() == 'lunch'):
#         if(current_day == 5 or current_day == 6):
#             ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
#             return

#         food_dict = barrettReq('lunch')
        
#     elif(arg1.lower() == 'dinner'):
        
#         food_dict = barrettReq('dinner')
    
#     elif(arg1.lower() == 'brunch'):
#         if(current_day != 5 and current_day != 6):
#             ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
#             return

#         food_dict = barrettReq('brunch')
        
#     else:
#         ctx.send("You have requested an invalid meal, please try again")


@bot.command(name='manzy')
async def test_menu(ctx, arg1):
    
    now = datetime.now()
    current_day = now.weekday()
    
    if(arg1.lower() == 'breakfast'):
        
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        food_dict = manzyReq('breakfast')
        
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
    
    elif(arg1.lower() == 'lunch'):
        if(current_day == 5 or current_day == 6):
            ctx.send("This dining hall is not serving Breakfast today, try requesting Brunch instead")
            return
        
        food_dict = manzyReq('lunch')
        
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
    
    elif(arg1.lower() == 'dinner'):
        
        food_dict = manzyReq('dinner')
        
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
    
    elif(arg1.lower() == 'brunch'):
        if(current_day != 5 and current_day != 6):
            ctx.send("This dining hall is not serving Brunch today, try requesting Breakfast or Lunch instead")
            return
        
    else:
        ctx.send("You have requested an invalid meal, please try again")
    
    await ctx.send(embed=embed)

bot.run(TOKEN)


    
