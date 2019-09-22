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


item = "\n****************************"
parte = "##########################\n"

print("   KATHERINE GARCIA G")
print(parte)
print("1. Portal")
title = soup.title.string
print(title)
print(item)

image_href = []
hrefs = soup.find_all("a", href = True)
for i in hrefs:
    ref = i['href']

    if ref == "#myModal":
        direccion = (i.text)

    elif ref.startswith("tel"):
        ref.strip("tel:")
        telefono = ref

    elif ref.startswith("mailto:inf"):
        ref.strip("mailto:")
        mail = ref

    elif i.text == "UFMail":
        mailbutton = ref

    elif i.text == "MiU":
        miubutton = ref

    imag = i.find_all("img")
    for im in imag:
        image_href.append(ref)

print("Direccion:", direccion)
print("Telefono:", telefono)
print("Mail:", mail)
print(item)
menu = soup.find_all("div", class_="menu-key")
for i in menu:
    tags = i.text
    tags.strip("\n")
    print(tags)
print(mailbutton,"\n")
print(miubutton, "\n")
for i in image_href:
    print(i)
        
# contador = 1
# prophref = soup.find_all("a", href = True)
# for i in prophref:s
#     ref = i['href']
#     if not ref.startswith(("#", "/")):
#         print(contador, ref)
#         contador += 1

#ufmail = soup.find("meta", property="og:image").get('content')

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
        
#contador = 1
# prophref = soup.find_all("a", href = True)
# for i in prophref:s
#     ref = i['href']
#     if not ref.startswith(("#", "/")):
#         print(contador, ref)
#         contador += 1
        
    

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