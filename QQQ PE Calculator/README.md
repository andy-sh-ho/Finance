# QQQ PE Calculator

This is a Python script that calculates the price-to-earnings ratio (PE) of the Invesco QQQ Trust (QQQ), an exchange-traded fund (ETF) that tracks the Nasdaq-100 Index. The script uses the pandas and yfinance libraries to fetch and process the data.

## How it works

The script performs the following steps:
* It downloads a CSV file from the Invesco website that contains the holdings of QQQ as of a given date, along with their ticker symbols, shares, and market value.
* It converts the date column to a datetime object and sets it as the index of the dataframe.
* It defines a function that takes a ticker symbol as input and returns the trailing EPS of the corresponding stock, using the yfinance API. If an error occurs, it prints the error and returns None.
* It applies the function to each ticker symbol in the dataframe and creates a new column for the EPS values.
* It converts the EPS column to a numeric type and handles any missing or invalid values.
* It calculates the earnings of each holding by multiplying the shares and the EPS, and creates a new column for the earnings values.
* It sums up the earnings and market value of all holdings, and divides them to get the PE of QQQ based on trailing EPS.
* It prints the result and displays the dataframe.

To run this script, you need to have Python 3 installed on your system, along with pandas and yfinance. You can install them using pip:
```
pip install pandas yfinance
```
Then, you can run the script from the command line:
```
python QQQ_PE_Ratio.py
```
The output should look something like this:
```
QQQ PE based on trailing EPS: 41.35431434687081
           Fund Ticker Security Identifier Holding Ticker Shares/Par Value  ...              Class of Shares                  Sector   EPS       Earning
Date                                                                        ...
2023-07-17         QQQ           594918104          MSFT        78,078,757  ...                 Common Stock  Information Technology  9.22  7.198861e+08
2023-07-17         QQQ           037833100          AAPL       133,396,212  ...                 Common Stock  Information Technology  5.89  7.857037e+08
2023-07-17         QQQ           67066G104          NVDA        33,788,594  ...                 Common Stock  Information Technology  1.91  6.453621e+07
2023-07-17         QQQ           023135106          AMZN       108,191,762  ...                 Common Stock  Consumer Discretionary  0.41  4.435862e+07
2023-07-17         QQQ           88160R101          TSLA        33,421,328  ...                 Common Stock  Consumer Discretionary  3.43  1.146352e+08
...                ...                 ...            ...              ...  ...                          ...                     ...   ...           ...
2023-07-17         QQQ           98980G102            ZS         1,985,191  ...                 Common Stock  Information Technology -1.89 -3.752011e+06
2023-07-17         QQQ           82968B103          SIRI        52,918,067  ...                 Common Stock  Communication Services  0.29  1.534624e+07
2023-07-17         QQQ           98980L101            ZM         3,431,866  ...                 Common Stock  Information Technology  0.02  6.863732e+04
2023-07-17         QQQ           47215P106            JD         6,210,632  ...  American Depository Receipt  Consumer Discretionary  1.71  1.062018e+07
2023-07-17         QQQ           549498103          LCID        25,091,742  ...                 Common Stock  Consumer Discretionary -1.56 -3.914312e+07
[101 rows x 11 columns]
```

## Author
- [@andy-sh-ho](https://www.github.com/andy-sh-ho)
