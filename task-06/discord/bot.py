import discord
from discord.ext import commands
import scraper
import csv


intents = discord.Intents.default()
intents.typing = False
intents.presences = False  

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
live_scores = []


bot.remove_command('help')


@bot.command() 
async def livescore(ctx):
    try:
        url = 'https://www.espncricinfo.com/live-cricket-score'  
        class_name1 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate'
        class_name2 = 'ds-text-tight-m ds-font-bold ds-capitalize ds-truncate'

        over1 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"
        over2 = "ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap"

        det = "ds-text-tight-s ds-font-regular ds-truncate ds-text-typo"

        print('executing livescore')
        scraped_data = scraper.scrape_specific_division(url, class_name1, class_name2, det, over1, over2)

        if scraped_data:
            await ctx.send(f'Title: {scraped_data}')
            live_scores.append(scraped_data)

            
            
            with open('allscores.csv', mode='a', newline='') as file:
                
                file.write(scraped_data + '\n' + '\n')
            

        else:
            await ctx.send('data not found')

    except ValueError:
        await ctx.send('Usage /livescore')

@bot.command()
async def csv(ctx):
    
    
    if live_scores:

        await ctx.send("All Live Scores:")

        with open('allscores.csv', 'rb') as file:
            await ctx.send(file=discord.File(file, 'allscores.csv'))
    
    
    else:
        
        await ctx.send('YOU Didnot ASKED FOR ANY LIVE SCORES YET.')

@bot.command()
async def help(ctx):
    await ctx.send('''use /livescore to get livescore 
/csv for livescores youve asked until now
/help for help with so complicated commands''')


@bot.command()
async def reset(ctx):
    try:
        with open('allscores.csv', 'w', newline='') as file:
            pass  
        await ctx.send('CSV file has been reset.')
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')



bot.run('MTE1NDc1NTQwNDYxNDYxMDk0NA.G4XT1U.t2WvlPIVky9-ZZUeqh8QxDCX-JyEuwYWgfVgkc')
