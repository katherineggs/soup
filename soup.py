#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url_1="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
def soups(url):
    try:
        html_content = requests.get(url).text
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    # Parse the html content, this is the Magic ;)
    sopa = BeautifulSoup(html_content, "html.parser")
    return sopa

soup = soups(url_1)

item = "\n****************************"
parte = "##########################\n"

print("   KATHERINE GARCIA G")
print(parte)
print("1. Portal")
def titles():
    title = soup.title.string
    print(title)
print(item)

hrefs = soup.find_all("a", href = True)
image_href = []
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

    elif i.text == "Estudios":
        estudios = ref

    imag = i.find_all("img")
    for im in imag:
        image_href.append(ref)
    

print("Direccion:", direccion)
print(item)
print("Telefono:", telefono)
print(item)
print("Mail:", mail)
print(item)
menu = soup.find_all("div", class_="menu-key")
for i in menu:
    tags = i.text
    tags.strip("\n")
    print(tags)
print(item)
print(mailbutton,"\n")
print(item)
print(miubutton, "\n")
for i in image_href:
    print(i)
print(item)

def count_a ():
    a = len(soup.find_all("a"))
    print("\nThere are",a,"<a> tags\n")
count_a()

print("2. Estudios")
print(parte)
url_2 = "http://ufm.edu" + estudios
soup = soups(url_2)

top = soup.find("div", id="topmenu")
print(top.text)
print(item)
estuds = soup.find("div", class_="row-fluid sinbullets")
print(estuds.text)
print(item)
leftbar = soup.find("div", class_= "leftbar")
leftmenu = leftbar.find_all("li")
for i in leftmenu:
    print(i.text)
print(item)
print("Redes Sociales")
socials = soup.find("div", class_= "social pull-right")
socs = socials.find_all("a", href = True)
for i in socs:
    redes = i['href']
    print(redes)
print(item)

count_a()

print(parte)

url_3 = "https://fce.ufm.edu/carrera/cs/"
soup = soups(url_3)
titles()


# for ul in top:
#     print(ul)






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