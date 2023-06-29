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

manzyBreakfast = {}
manzyLunch = {}
manzyDinner = {}

pitchforksBreakfast = {}
pitchforksLunch = {}
pitchforksDinner = {}

hassyBreakfast = {}
hassyLunch = {}
hassyDinner = {}

barrettBreakfast = {}
barrettLunch = {}
barrettDinner = {}

async def tooker(requestedMeal, food_dict):

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

            dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                pass

            doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)


        await scrape_food('//*[@id="22794"]', 'Daily Root')
        await scrape_food('//*[@id="22792"]', 'Home Zone')
        await scrape_food('//*[@id="30185"]', 'True Balance')

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

            dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                pass

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
                pass

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
    

async def manzy(requestedMeal, food_dict):

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

            dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Breakfast"]', timeout=5000)
                await breakfastOption.click()
            except:
                pass

            doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
            
        await scrape_food('//*[@id="13988"]', 'Daily Root')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9141"]', 'Salad Bar')
        await scrape_food('//*[@id="9138"]', 'Grill')

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

            dropDown = await page.waitForSelector('.css-1t70p0u-control', timeout=5000)
            await dropDown.click()

            try:
                breakfastOption = await page.waitForXPath('//div[text()="Lunch"]', timeout=5000)
                await breakfastOption.click()
            except:
                pass

            doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
                
        await scrape_food('//*[@id="13988"]', 'Daily Root')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')

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
                pass

            doneButton = await page.waitForSelector('#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done', timeout=5000)

            await doneButton.click()
            await page.waitForSelector('.ChoosenMeal', timeout=60000)

            await asyncio.sleep(2)
                
        await scrape_food('//*[@id="13988"]', 'Daily Root')
        await scrape_food('//*[@id="9139"]', 'Home Zone')
        await scrape_food('//*[@id="9138"]', 'Grill')
        await scrape_food('//*[@id="9140"]', 'Pizza')
        await scrape_food('//*[@id="13991"]', 'Sazon Station')


async def pitchforks(requestedMeal, food_dict):

def checkTime():
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if(current_time == '07:00:00'):

        tooker('breakfast', tookerBreakfast)
        tooker('lunch', tookerLunch)
        tooker('dinner', tookerDinner)

        manzy('breakfast', manzyBreakfast)
        manzy('lunch', manzyLunch)
        manzy('dinner', manzyDinner)
        


@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running')

