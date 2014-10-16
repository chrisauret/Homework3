#  PART 1 
#  Create a market simulation tool, marketsim.py that takes a command line like this:
#
#   python marketsim.py 1000000 orders.csv values.csv
#
#  Where the number represents starting cash and orders.csv is a file of orders organized like this:
#  Year
#  Month
#  Day
#  Symbol
#  BUY or SELL
#  Number of Shares
#
#  For example:
#   2008, 12, 3, AAPL, BUY, 130
#   2008, 12, 8, AAPL, SELL, 130
#   2008, 12, 5, IBM, BUY, 50
#
#  Your simulator should calculate the total value of the portfolio for each day using adjusted closing 
#  prices (cash plus value of equities) and print the result to the file values.csv. The contents of the 
#  values.csv file should look something like this:
#
#   2008, 12, 3, 1000000
#   2008, 12, 4, 1000010
#   2008, 12, 5, 1000250
#   ...

import sys
import csv

def main(argv):
    # Capture command-line arguments
    cash = argv[0]
    ordersFile = argv[1]
    valuesFile = argv[2]

    # Read the orders.csv data into a trades array - Order it by date, 
    # http://stackoverflow.com/a/3519314
    # http://stackoverflow.com/a/26296194

    tradesArray = []
    with open(ordersFile, 'rb') as ordersCsv:
        csvReader = csv.reader(ordersCsv, delimiter=' ', quotechar='|')
        for row in csvReader:
            tradesArray.append(row)
    
    print tradesArray
    #   with column for the symbol, but/sell, number of shares
    # Scan trades for symbols and dates ( all the symbols and the boundries of dates)
    # Read in data using data access methods, and read in the adjusted close prices
    # Scan trades to update cash
    # Scan trades to create ownership array & value
    # Scan cash and value to create total fund value
    # Order the array by date

if __name__ == "__main__":
    main(sys.argv[1:])
