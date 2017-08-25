import csv
import os
from pprint import pprint

if __name__ == "__main__":

    with open('amzn_hist_test.csv') as csvfile:
        priceList = csv.DictReader(csvfile)
        #for row in priceList:
        #   print(row)

    with open ('Option_Exp_dates_Test.csv') as csvfile2:
        optionExp = csv.DictReader(csvfile2)
        for row in optionExp:
            pprint(row)

    #pprint(optionExp['TradeDate'])
    #startDate=optionExp['TradeDay']
    #pprint(startDate)

    #why is this modifying my OptionExp csv, merging cell date