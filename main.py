import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def soundex(word):
    """Converts a word to its Soundex code."""
    word = word.upper()
    soundex_mapping = {"BFPV": "1", "CGJKQSXZ": "2", "DT": "3", "L": "4",
                       "MN": "5", "R": "6"}

    first_letter = word[0]

    
    encoded = first_letter
    for char in word[1:]:
        for key, value in soundex_mapping.items():
            if char in key:
                if encoded[-1] != value:  
                    encoded += value
                break
        else:
            if char not in "HWY":  
                encoded += "0"  

    
    encoded = encoded.replace("0", "")
    return (encoded[:4] + "000")[:4]

bot.run(Token)
