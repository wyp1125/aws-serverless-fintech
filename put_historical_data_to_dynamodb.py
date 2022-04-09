#####################################################################
####This program takes in the historical data of individual stock and
####uploads them to dynamodb
#####################################################################

import boto3
import sys,os
import pandas as pd
import json
from decimal import Decimal

tickers=["AAPL","AMZN","FB","GILD","BIIB","TSLA","BAC","SPY","MS","F"]
#tickers=["AAPL"]

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table("stock_data")

for ticker in tickers:
  tsv_path=os.path.join("/Users/wyp1125/projects/AWS/stock_data",ticker+".tsv")
  stock_df=pd.read_csv(tsv_path,sep="\t")
  stock_df["Date"]=stock_df["Date"].apply(lambda x: x.split( )[0])
  stock_df=stock_df.reset_index()
  for index,row in stock_df.iterrows():
    info={}
    info['High']=Decimal(str(row['High']))
    info['Low']=Decimal(str(row['Low']))
    info['Open']=Decimal(str(row['Open']))
    info['Close']=Decimal(str(row['Close']))
    rec={}
    rec['Ticker']=ticker
    rec['Date']=row['Date']
    rec['Info']=info
    print(rec) 
    table.put_item(Item=rec)

