import csv
import os
from pprint import pprint
from datetime import datetime, timedelta

def convert_date (rawDate):
    if '-' in rawDate:
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
    startDate = convert_date(optionExpList[0]['TradeDate'])

    optListLen=len(optionExpList)

    #last expiration date in regression
    lastDay = convert_date(optionExpList[optListLen-1]['Exp Day'])

    priceListLen = len(priceList)
    # pprint(priceListLen)

    pl_counter=0
    #find the low price of stock the first trading day after the first exp
    while pl_counter < priceListLen:
        if startDate != convert_date(priceList[pl_counter]['date']):
            pl_counter += 1
        else:
            startDateLow = priceList[pl_counter]['low']
            break

    sellPrem = round(float(startDateLow)*.1,2)  #premium collected for sale of put
    putStrike= int((int(float(startDateLow))-5)/5*5)    #strike price that is $5 below market value
    ownStock = 'no'
    acct_balance = sellPrem

    exp_counter=1
    nextExpDay=convert_date(optionExpList[exp_counter]['Exp Day'])
    #pprint(pl_counter)

    while convert_date(priceList[pl_counter]['date']) <= nextExpDay:
        pprint(convert_date(priceList[pl_counter]['date']) <= nextExpDay)
        if float(priceList[pl_counter]['low']) < putStrike * .9:
            # buy put back, subtract premium+10% loss; need a better estimate here; will tune so that losses will decrease
            # as we get closer to expiration; maybe 10% to start and then decrease to 1% as we get closer to expiration
            acct_balance=acct_balance-2*sellPrem
            break
        else:
            pl_counter += 1
            #pprint(pl_counter)
            #pprint(convert_date(priceList[pl_counter]['date']))

    NextDay=startDate+timedelta(days=1)
    # pprint(NextDay)


