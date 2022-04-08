####################################################
#This program takes in a tab-delimited txt file of historical data
#of a stock, and convert the data into a json file with ticker added.
#This serves a modifiable program for converting dataframe into json.
####################################################
import sys
import json

if len(sys.argv)<4:
  print("input_txt output_json ticker")
  quit()
def tsv2json(input_file,output_file):
    arr = []
    file = open(input_file, 'r')
    a = file.readline()
      
    # The first line consist of headings of the record 
    # so we will store it in an array and move to 
    # next line in input_file.
    titles = [t.strip() for t in a.split('\t')]
    for line in file:
        d = {}
        for t, f in zip(titles, line.split('\t')):
            
              # Convert each row into dictionary with keys as titles
            d[t] = f.strip()
        d["Ticker"]=sys.argv[3]      
        # we will use strip to remove '\n'.
        d["Date"]=d["Date"].split(" ")[0]
        arr.append(d)
          
        # we will append all the individual dictionaires into list 
        # and dump into file.
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(json.dumps(arr, indent=4))
  
tsv2json(sys.argv[1],sys.argv[2])
