#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import shutil
#----------------------------------------------------------------parte 1
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

def exceeds(fresas,nombre):
    if fresas is not None:
        if len(fresas) >= 30:
            txt_name = nombre+".txt"
            txt = open(txt_name,'w+')
            if type(fresas) == list:
                for i in fresas:
                    text = txt.write(i)
                    text = txt.write("\n")
            else:
                text = txt.write(fresas)
                return text

def titles():
    title = soup.title.string
    print(title)

def hre():
    lista = []
    prophref = soup.find_all("a", href = True)
    for i in prophref:
        ref = i['href']
        if not ref.startswith(("#", "/")):
            lista.append(ref)
    return(lista)

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

menu = soup.find_all("div", class_="menu-key")
tags = []
for i in menu:
    tag = i.get('data-menu')
    if tag is not None:
        tags.append(tag.upper())
images =[]
for i in image_href:
    if i.startswith("http"):
        images.append(i)

def count_ (element):
    a = len(soup.find_all(element))
    print("There are",a,"<"+element+">","tags")

def easy_for (element):
    for ele in element:
        if ele is not None:
            print(ele)
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################

item = "\n****************************"
parte = "##########################\n"

print("   KATHERINE GARCIA G")
print(parte)
print("1. Portal")

titles()
print(item)

print("Direccion:", direccion)
print(item)
print("Telefono:", telefono)
print(item)
print("Mail:", mail)
print(item)

print("Nav-Menu\n")
easy_for(tags)
print(item)
exceeds(hre(),"hrefs")
print("All <href> in: hrefs.txt")

print("UFMail")
print(mailbutton)
print("MiU")
print(miubutton)
print(item)
print("IMG tags")
easy_for(images)
print(item)

count_("a")
print(item)

#----------------------------------------------------------------------------------parte 2
print("2. Estudios")
print(parte)
url_2 = "http://ufm.edu" + estudios
soup = soups(url_2)

top = soup.find("div", id="topmenu")
print("Top Menu")
print(top.text)
print(item)

print("Estudios")
estuds = soup.find_all("div", class_="estudios")
for est in estuds:
    if est is not None:
        print(est.text)
each = soup.find("div", class_="row-fluid sinbullets").text
exceeds(each,"estudios")
print("All estudios in: estudios.txt")
print(item)

print("Left bar")
leftbar = soup.find("div", class_= "leftbar")
leftmenu = leftbar.find_all("li")
for i in leftmenu:
    print("-",i.text)
print(item)
print("Redes Sociales")
socials = soup.find("div", class_= "social pull-right")
socs = socials.find_all("a", href = True)
def get_name(media):
    media = media.replace("https://www.", "")
    media = media.replace("http://www.", "")
    media = media.replace("https://", "")
    media= media.replace(".com", "\\").split("\\")
    return media[0]
for i in socs:
    redes = i['href']
    print(get_name(redes).upper())
    print("              ",redes)
print(item)

count_("a")
print(item)
#-------------------------------------------------------------------------------------------parte 3
print("3. Computer Science")
print(parte)
url_3 = "https://fce.ufm.edu/carrera/cs/"
soup = soups(url_3)
titles()
print(item)
cs_href = soup.title.find_next_sibling('link')
print("---",cs_href['href'],"---")
print(item)

tag_a = soup.find_all("a", href = "https://fce.ufm.edu")
for i in tag_a:
    source = i.find("img")['src']
r = requests.get(source, stream=True)
logo = open('logo.jpg', 'wb')
r.raw.decode_content = True
shutil.copyfileobj(r.raw,logo)

print("Logo Facultad")
print(item)
title = soup.find("meta", property= "og:title")['content']
description = soup.find("meta", property="og:description")['content']
print("Title")
print(title)
print("Descripcion")
print(description)
print(item)
count_("a")
print(item)
count_("div")
print(item)

print("\n4. Directorio")
print(parte)
url_4 = "https://www.ufm.edu/Directorio"
soup = soups(url_4)









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