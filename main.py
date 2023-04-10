#bot.py

import os
from dotenv import load_dotenv, find_dotenv

import discord
from discord.ext import commands
from discord import app_commands

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')



chrome_driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)


intents = discord.Intents.all()


bot = commands.Bot(command_prefix="?", intents=intents)


now = datetime.now()
hour = now.hour
day = now.weekday()



class Tooker():

    def breakfast():
        
        
        try:
            dailyRoot = driver.find_element(By.XPATH, '//*[@id="22794"]')
            
            dailyRootFoods = dailyRoot.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            daily_root_foods = [food.text for food in dailyRootFoods]
            while '' in daily_root_foods:
                daily_root_foods.remove('')

        except:
            pass
        
        try:
            homeZone = driver.find_element(By.XPATH, '//*[@id="22792"]')
            homeZoneFoods = homeZone.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            home_zone_foods = [food.text for food in homeZoneFoods]
            while '' in home_zone_foods:
                home_zone_foods.remove('')   

        except:
            pass
        
        try:
            trueBalance = driver.find_element(By.XPATH, '//*[@id="30185"]')
            trueBalanceFoods = trueBalance.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            true_balance_foods = [food.text for food in trueBalanceFoods]
            while '' in true_balance_foods:
                true_balance_foods.remove('')  

        except:
            pass
        
        
        food_dict = {}
        try:
            food_dict.update({'Daily Root': daily_root_foods})
        except:
            pass

        try:
            food_dict.update({'Home Zone': home_zone_foods})
        except:
            pass

        try:
            food_dict.update({'True Balance': true_balance_foods})
        except:
            pass
        
        
        return food_dict
        

    def lunch():
        try:
            dailyRoot = driver.find_element(By.XPATH, '//*[@id="22794"]')
            dailyRootFoods = dailyRoot.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            daily_root_foods = [food.text for food in dailyRootFoods]
            while '' in daily_root_foods:
                daily_root_foods.remove('')
        except:
            pass
        
        try:
            homeZone = driver.find_element(By.XPATH, '//*[@id="22792"]')
            homeZoneFoods = homeZone.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            home_zone_foods = [food.text for food in homeZoneFoods]
            while '' in home_zone_foods:
                home_zone_foods.remove('') 
        except:
            pass
        
        try:
            grill = driver.find_element(By.XPATH, '//*[@id="22793"]')
            grillFoods = grill.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            grill_foods = [food.text for food in grillFoods]
            while '' in grill_foods:
                grill_foods.remove('')
        except:
            pass

        
        try:
            pizza = driver.find_element(By.XPATH, '//*[@id="22796"]')
            pizzaFoods = pizza.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            pizza_foods = [food.text for food in pizzaFoods]
            while '' in pizza_foods:
                pizza_foods.remove('')
        except:
            pass
        
        try:
            soup = driver.find_element(By.XPATH, '//*[@id="22797"]')
            soupFoods = soup.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            soup_foods = [food.text for food in soupFoods]
            while '' in soup_foods:
                soup_foods.remove('')
        except:
            pass
        
        try:
            trueBalance = driver.find_element(By.XPATH, '//*[@id="30185"]')
            trueBalanceFoods = trueBalance.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            true_balance_foods = [food.text for food in trueBalanceFoods]
            while '' in true_balance_foods:
                true_balance_foods.remove('')
        except:
            pass
        
            
        shawarma_station = ['Falafel Pita']
            
        food_dict = {}
        
        try:
            food_dict.update({'Daily Root': daily_root_foods})
        except:
            pass
        
        try:
            food_dict.update({'Home Zone': home_zone_foods})
        except:
            pass
        
        try:
            food_dict.update({'Grill': grill_foods})
        except:
            pass
        
        try:
            food_dict.update({'Pizza': pizza_foods})
        except:
            pass
        
        try:
            food_dict.update({'Soup': soup_foods})
        except:
            pass
        
        try:
            food_dict.update({'True Balance': true_balance_foods})
        except:
            pass
        
        try: 
            food_dict.update({'Shawarma': shawarma_station})
        except:
            pass
        
        return food_dict
        
    def dinner():
        
        try:
            dailyRoot = driver.find_element(By.XPATH, '//*[@id="22794"]')
            dailyRootFoods = dailyRoot.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            daily_root_foods = [food.text for food in dailyRootFoods]
            while '' in daily_root_foods:
                daily_root_foods.remove('')
        except:
            pass
        
        
        
        try:
            homeZone = driver.find_element(By.XPATH, '//*[@id="22792"]')
            homeZoneFoods = homeZone.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            home_zone_foods = [food.text for food in homeZoneFoods]
            while '' in home_zone_foods:
                home_zone_foods.remove('') 
        except:
            pass
        
        
        try:
            grill = driver.find_element(By.XPATH, '//*[@id="22793"]')
            grillFoods = grill.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            grill_foods = [food.text for food in grillFoods]
            while '' in grill_foods:
                grill_foods.remove('')
        except:
            pass
            
        try:
            pizza = driver.find_element(By.XPATH, '//*[@id="22796"]')
            pizzaFoods = pizza.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            pizza_foods = [food.text for food in pizzaFoods]
            while '' in pizza_foods:
                pizza_foods.remove('')
        except:
            pass
            
        try:
            soup = driver.find_element(By.XPATH, '//*[@id="22797"]')
            soupFoods = soup.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            soup_foods = [food.text for food in soupFoods]
            while '' in soup_foods:
                soup_foods.remove('')
            
        except:
            pass
        
        try:
            trueBalance = driver.find_element(By.XPATH, '//*[@id="30185"]')
            trueBalanceFoods = trueBalance.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            true_balance_foods = [food.text for food in trueBalanceFoods]
            while '' in true_balance_foods:
                true_balance_foods.remove('')
        except:
            pass
            
        shawarma_station = ['Chicken Shawarma Pita', 'Falafel Pita']
            
        
        food_dict = {}
        
        try:
            food_dict.update({'Daily Root': daily_root_foods})
        except:
            pass
        
        try:
            food_dict.update({'Home Zone': home_zone_foods})
        except:
            pass
        
        try:
            food_dict.update({'Grill': grill_foods})
        except:
            pass
        
        try:
            food_dict.update({'Pizza': pizza_foods})
        except:
            pass
        
        try:
            food_dict.update({'Soup': soup_foods})
        except:
            pass
        
        try:
            food_dict.update({'True Balance': true_balance_foods})
        except:
            pass
        
        try:
            food_dict.update({'Shawarma': shawarma_station})
        except:
            pass
            
        
        return food_dict
        

    def brunch():
        
        try:
            dailyRoot = driver.find_element(By.XPATH, '//*[@id="22794"]')
            dailyRootFoods = dailyRoot.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            daily_root_foods = [food.text for food in dailyRootFoods]
            while '' in daily_root_foods:
                daily_root_foods.remove('')
        except:
            pass
        
        try:
            homeZone = driver.find_element(By.XPATH, '//*[@id="22792"]')
            homeZoneFoods = homeZone.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            home_zone_foods = [food.text for food in homeZoneFoods]
            while '' in home_zone_foods:
                home_zone_foods.remove('') 
        except:
            pass
        
        try:
            grill = driver.find_element(By.XPATH, '//*[@id="22793"]')
            grillFoods = grill.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            grill_foods = [food.text for food in grillFoods]
            while '' in grill_foods:
                grill_foods.remove('')
        except:
            pass
        
        try:
            pizza = driver.find_element(By.XPATH, '//*[@id="22796"]')
            pizzaFoods = pizza.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            pizza_foods = [food.text for food in pizzaFoods]
            while '' in pizza_foods:
                pizza_foods.remove('')
        except:
            pass
        
        try:
            trueBalance = driver.find_element(By.XPATH, '//*[@id="30185"]')
            trueBalanceFoods = trueBalance.find_elements(By.CSS_SELECTOR, 'div.sc-tQuYZ.gvgoZc > button > h3 > span')
            true_balance_foods = [food.text for food in trueBalanceFoods]
            while '' in true_balance_foods:
                true_balance_foods.remove('')
        except:
            pass
        
            
        
        food_dict = {}
        
        try:
            food_dict.update({'Daily Root': daily_root_foods})
        except:
            pass
        
        try:
            food_dict.update({'Home Zone': home_zone_foods})
        except:
            pass
        
        try:
            food_dict.update({'Grill': grill_foods})
        except:
            pass
        
        try:
            food_dict.update({'Pizza': pizza_foods})
        except:
            pass

        try:
            food_dict.update({'True Balance': true_balance_foods})
        except:
            pass

        
        return food_dict
        



@bot.command(name='tooker')
async def tooker_menu(ctx, arg1):
    
    requestedMeal = arg1.lower()
    
    
    if(requestedMeal == 'breakfast'):
        
        driver.get('https://asu.campusdish.com/DiningVenues/TookerHouseDining')
        
        wait = WebDriverWait(driver, 10)
        
        try:
            popup1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')))
            popup2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')))
            popup1.click()
            popup2.click()
        except:
            pass

        driver.refresh()
        
        meal = driver.find_element(By.CLASS_NAME, 'ChoosenMeal')
        meal = meal.text
        
        if(day == 5 or day == 6):
            ctx.send("Today is a weekend which means that the Tooker dining hall does not offer Breakfast, please try requesting the 'Brunch' menu instead")
        
        if(meal != 'Breakfast'): 
                try:
                    swapButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DateMealFilterButton')))
                    swapButton.click()
                except:
                    pass
                
                dropDown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1t70p0u-control')))
                dropDown.click()
                
                try:
                    dinnerOption = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Breakfast"]')))
                    actions = ActionChains(driver)
                    actions.move_to_element(dinnerOption).click().perform()
                except:
                    ctx.send("Sorry but it does not appear that there is a Breakfast option today at Tooker dining...")

                
                doneButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done')))
                driver.execute_script("arguments[0].click();", doneButton)
        
        time.sleep(3)
        
        menu = Tooker.breakfast()
        
        try:
            dailyRoot = menu['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
        except:
           pass
            
        try:
            homeZone = menu['Home Zone']
            homeZone = ', '.join(homeZone)
        except:
            pass
            
        try:
            trueBalance = menu['True Balance']
            trueBalance = ', '.join(trueBalance)
        except:
            pass
        
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
            embed.add_field(name="True Balance:", value=trueBalance, inline=False)
        except:
            pass
        
        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
    
    if(requestedMeal == 'lunch'):
        
        driver.get('https://asu.campusdish.com/DiningVenues/TookerHouseDining')
        
        wait = WebDriverWait(driver, 10)
        
        try:
            popup1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')))
            popup2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')))
            popup1.click()
            popup2.click()
        except:
            pass

        driver.refresh()
        
        meal = driver.find_element(By.CLASS_NAME, 'ChoosenMeal')
        meal = meal.text
        
        if(day == 5 or day == 6):
            ctx.send("Today is a weekend which means that the Tooker dining hall does not offer Lunch, please try requesting the 'Brunch' menu instead")
        
        if(meal != 'Lunch'): 
                try:
                    swapButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DateMealFilterButton')))
                    swapButton.click()
                except:
                    pass
                
                dropDown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1t70p0u-control')))
                dropDown.click()
                
                try:
                    dinnerOption = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Lunch"]')))
                    actions = ActionChains(driver)
                    actions.move_to_element(dinnerOption).click().perform()
                except:
                    ctx.send("Sorry but it does not appear that there is a Lunch option today at Tooker dining...")

                
                doneButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done')))
                driver.execute_script("arguments[0].click();", doneButton)
        
        time.sleep(3)
        
        menu = Tooker.lunch()
        
        try:
            dailyRoot = menu['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
        except:
            pass
        
        try:
            homeZone = menu['Home Zone']
            homeZone = ', '.join(homeZone)
        except:
            pass
        
        try:
            grill = menu['Grill']
            grill = ', '.join(grill)
        except:
            pass
        
        try:
            pizza = menu['Pizza']
            pizza = ', '.join(pizza)
        except:
            pass
        
        try:
            soup = menu['Soup']
            soup = ', '.join(soup)
        except:
            pass
        
        try:
            trueBalance = menu['True Balance']
            trueBalance = ', '.join(trueBalance)
        except:
            pass
        
        try:
            shawarma = menu['Shawarma']
            shawarma = ', '.join(shawarma)
        except:
            pass
        
        
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
            embed.add_field(name="Grill", value=grill, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Pizza", value=pizza, inline=True)
        except:
            pass
        
        try:
            embed.add_field(name="Soup", value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Shawarma Station", value=shawarma, inline=True)
        except:
            pass

        
        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
    
    if(requestedMeal == 'dinner'):
        
        driver.get('https://asu.campusdish.com/DiningVenues/TookerHouseDining')
        
        wait = WebDriverWait(driver, 10)
        
        try:
            popup1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root-mail-subsription"]/div/div/div/div/div/div[1]/button')))
            popup2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')))
            popup1.click()
            popup2.click()
        except:
            pass

        driver.refresh()
        
        meal = driver.find_element(By.CLASS_NAME, 'ChoosenMeal')
        meal = meal.text
        
        if(meal != 'Dinner'): 
                try:
                    swapButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DateMealFilterButton')))
                    swapButton.click()
                except:
                    pass
                
                dropDown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1t70p0u-control')))
                dropDown.click()
                
                dinnerOption = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Dinner"]')))
                actions = ActionChains(driver)
                actions.move_to_element(dinnerOption).click().perform()

                
                doneButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#modal-root > div > div > div > div > div.sc-cCsOjp.gvlGSX > button.sc-bczRLJ.sc-gsnTZi.gObyWR.SlTeX.Done')))
                driver.execute_script("arguments[0].click();", doneButton)
                
        time.sleep(3)
    
        menu = Tooker.dinner()
        
        
        try:
            dailyRoot = menu['Daily Root']
            dailyRoot = ', '.join(dailyRoot)
        except:
            pass
        
        
        try:
            homeZone = menu['Home Zone']
            homeZone = ', '.join(homeZone)
        except:
            pass
        
        try:
            grill = menu['Grill']
            grill = ', '.join(grill)
        except:
            pass
        
        try:
            pizza = menu['Pizza']
            pizza = ', '.join(pizza)
        except:
            pass
        
        try:
            soup = menu['Soup']
            soup = ', '.join(soup)
        except:
            pass
        
        try:
            trueBalance = menu['True Balance']
            trueBalance = ', '.join(trueBalance)
        except:
            pass
        
        try:
            shawarma = menu['Shawarma']
            shawarma = ', '.join(shawarma)
        except:
            pass
        
        
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
            embed.add_field(name="Grill", value=grill, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Pizza", value=pizza, inline=True)
        except:
            pass
        
        try:
            embed.add_field(name="Soup", value=soup, inline=False)
        except:
            pass
        
        try:
            embed.add_field(name="Shawarma Station", value=shawarma, inline=True)
        except:
            pass

        
        embed.set_image(url="https://i.imgur.com/IkomYmr.jpg")
        
        
    
    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    print(f'{bot.user.name} is up and running')
    
bot.run(TOKEN)
    
