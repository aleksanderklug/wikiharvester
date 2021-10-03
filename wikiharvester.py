
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

url = input("Enter URL here: ")
filename = input("Name your file: ")
def main():
    
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table_class="wikitable sortable jquery-tablesorter"
    wikitable = soup.find('table',{'class':"wikitable"})    
    table_content = pd.read_html(str(wikitable))
    table_content = pd.DataFrame(table_content[0])
    table_conten = table_content.drop([0,1], axis=0)
    table_conten = table_content.iloc[0]
    table_content.to_csv(filename + ".csv", index=False)
    
if __name__ == "__main__":
    main()
    print("Finished scraping for tables!")