import os
import requests
import json
from .models import Books

class my_dictionary(dict): 
  
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value 

class gbooks():
    googleapikey = os.environ.get('API_KEY')
    
    def __init__(self, book_search):
        self.book_search= book_search

    def search(self):
        list1=[]
        list2=[]
        list3=[]
        idlist=[]
        list4=[]
        parms = {"q":self.book_search, 'key':self.googleapikey}
        
        try:
            r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
            my_json = r.json()
            for i in my_json["items"]:
                list1.append(i['volumeInfo']['title'])
                list2.append(i["volumeInfo"]["previewLink"])
                try:
                    list3.append(i['volumeInfo']["imageLinks"]["thumbnail"])
                except:
                    list3.append('#')
                idlist.append(i["id"])
                        
            '''books= Books.objects.filter().values('count')
            books = list(books)
            valuee=[]
            for i in books:
                key, value = list(i.items())[0]
                valuee.append(value)
            print(valuee)'''
                
            for j in idlist:
                
                if Books.objects.filter(ID= j):
                    i= Books.objects.filter(ID= j).values('count')
                    i = list(i)
                    key, value = list(i[0].items())[0]
                    #print(value)
                    #list4.append("available")
                    list4.append( f'This item is available in the inventory and STOCK LEFT:{value}')
                else:
                    list4.append("This item is not available in the inventory")

            data= zip(list1, list2, list3, list4)
            return data
        except:
            return zip(list1, list2, list3, list4)

        
        
        
       
