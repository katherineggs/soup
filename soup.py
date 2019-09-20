#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
# print(soup.prettify())
item = "****************************"
parte = "##########################\n"
#print(soup.title)
print("   KATHERINE GARCIA G")
print(parte)
print("1. Portal")
title = soup.title.string
print(title)
print(item)
direccion = soup.find("a", href= "#myModal")
print (direccion.text)
print(item)
contador = 1
prophref = soup.find_all("a", href = True)
for i in prophref:
    ref = i['href']
    if not ref.startswith(("#", "/")):
        print(contador, ref)
        contador += 1
print("2. Estudios")
print(parte)


# for divs in todo:
#     if (divs.todos is not None): #and (divs.todos["href"] == "#myModal") and (divs.todos["data-toggle"]== "modal"):
#         print("hola")
#         if (divs.todos["href"] == "#myModal"):
#             print ("2")
#             if (divs.todos["data-toggle"] == "modal"):
#                 print("3")
        # print(divs.todos)
        
    

    # try :
    #     direccion2 = div.a["href"]
    #     if direccion2 == "#myModal":
    #         print(direccion2)
    # except:
    #, class_= 'span4'
    #     if None:
    #         pass
    
# for i in soup.find_all("a"):
#if direccion.startswith("Calle"):


# for div in soup.find_all("div"):
#     print(div)
#     print("--------------------------")