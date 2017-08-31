import csv
import os
from pprint import pprint
from datetime import datetime

def convert_date (rawDate):
    if '-' in rawDate:
        rawDate.replace("'","")
        #pprint(rawDate)
        newDate = datetime.strptime(rawDate, "%Y-%m-%d")

    else:
        newDate = datetime.strptime(rawDate, "%m/%d/%Y")

    return newDate

if __name__ == "__main__":

    with open('amzn_hist_test.csv', 'r') as csvfile:
        priceIter = csv.DictReader(csvfile)
        priceList = list(priceIter)     #convert iterable into list of dictionaries
        #for row in priceIter:
        #   print(row)

    with open ('Option_Exp_dates_Test.csv', 'r') as csvfile2:
        optionExp = csv.DictReader(csvfile2)
        optionExpList = list(optionExp)   #convert iterable into list of Dictionaries
        # for row in optionExp:
        #   print(row)

    #first trade date in regression
    startDateString = optionExpList[0]['TradeDate']
    startDate = convert_date(startDateString)
    #pprint(startDate)


    optListLen=len(optionExpList)

    #last expiration date in regression
    lastDayString = optionExpList[optListLen-1]['Exp Day']
    lastDay = convert_date(lastDayString)
    #pprint(lastDay)

    priceListLen = len(priceList)

    counter=0

    while counter < priceListLen:
        pl = convert_date(priceList[counter]['date'])
        if startDate != pl:
            counter+=1
        else:
            startDateLow = pl
            pprint(startDateLow)
            break

    #pprint(startDateLow)

