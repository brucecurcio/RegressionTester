import csv
import os
from pprint import pprint

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
    startDate = optionExpList[0]['TradeDate']

    listLen=len(optionExpList)

    #last expiration date in regression
    lastDay = optionExpList[listLen-1]['Exp Day']

