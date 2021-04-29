from bs4 import BeautifulSoup
import requests
import json
import sqlite3

def getWeathersparkHomepage():

    datavar = requests.get('https://weatherspark.com/')
    textvar = datavar.text
    soupvar = BeautifulSoup(textvar, 'html.parser')

    filevar = open('testfile.htm', 'w')
    writevar = filevar.write(str(soupvar.prettify))
    filevar.close()

