from bs4 import BeautifulSoup
import requests

url = "https://www.headphonezone.in/"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')
detail = soup.find_all('div',class_='product-details')
for details in detail:
    print(details.text)
        #name_dict[stripped_names] = {"product": product_name}

#product_name = read.select(".active")
#stripped_product_name = [prodname.text.strip() for prodname in product_name]

#p = {
#        "p1": {
#            "price": 500,
#            "product":["name1","name2"]
#            },
#        "p2": {
#            "price": 500,
#            "product":["name1","name2"]
#            }
#        }
#for pname,pinfo in p.items():
#    print(pname)
#    print("priced at", pinfo['price'])
#    print("products :")
#    print(",".join(pinfo['product']))
#    print("\n")



   
