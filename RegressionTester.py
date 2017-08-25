import csv
import os
from pprint import pprint

if __name__ == "__main__":

    with open('amzn_hist_test.csv') as csvfile:
        priceList = csv.DictReader(csvfile)
        #pprint(priceList.fieldnames)
        for row in priceList:
            print(row)