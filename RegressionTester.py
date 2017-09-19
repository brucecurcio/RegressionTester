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

def premium_collected(lowPrice):
    premium = round(float(lowPrice) * .1, 2)
    return premium

def calc_strike(lowPrice):
    strike=int((int(float(lowPrice)) - 5) / 5 * 5)
    return strike




if __name__ == "__main__":
    #pprint('start')
    with open('amzn_hist_test.csv', 'r') as csvfile:
        priceIter = csv.DictReader(csvfile)
        priceList = list(priceIter)     #convert iterable into list of dictionaries

    with open ('Option_Exp_dates_Test.csv', 'r') as csvfile2:
        optionExp = csv.DictReader(csvfile2)
        optionExpList = list(optionExp)   #convert iterable into list of Dictionaries


    startDate = convert_date(optionExpList[0]['TradeDate']) #first trade date in regression

    optListLen=len(optionExpList)

    lastDay = convert_date(optionExpList[optListLen-1]['Exp Day']) #last expiration date in regression

    priceListLen = len(priceList)

    # find the first trading day after the first exp
    pl_counter=0

    while pl_counter < priceListLen:

        if startDate != convert_date(priceList[pl_counter]['date']):
            pl_counter += 1
        else:
            break

    ownStock = 'no'
    acct_balance = 0

    #pprint(pl_counter)
    exp_counter=1
    while exp_counter <= optListLen: #iterate through expiration dates in csv
        #pprint(exp_counter)
        nextExpDay=convert_date(optionExpList[exp_counter]['Exp Day']) #get the next expiration day
        sellPrem=premium_collected(priceList[pl_counter]['low'])
        acct_balance += sellPrem # collect premium for sale of put
        strikePrice=calc_strike(priceList[pl_counter]['low']) #capture the closest strike price

        while convert_date(priceList[pl_counter]['date']) <= nextExpDay:
            #pprint (convert_date(priceList[pl_counter]['date']))
            if float(priceList[pl_counter]['low']) < strikePrice * .9:
                # buy put back, subtract premium+10% loss; need a better estimate here; will tune so that losses will decrease
                # as we get closer to expiration; maybe 10% to start and then decrease to 1% as we get closer to expiration
                acct_balance=acct_balance-2*sellPrem
                if convert_date(priceList[pl_counter]['date'])-nextExpDay < 16: #move to next exp date if less than 15 days til expire on current month
                    exp_counter+=1
                break
            else:
                pl_counter+=1
                if convert_date(priceList[pl_counter]['date'])== nextExpDay: #move to next exp date if iterated through current month
                    pprint (convert_date(priceList[pl_counter]['date'])== nextExpDay)
                    exp_counter+=1






