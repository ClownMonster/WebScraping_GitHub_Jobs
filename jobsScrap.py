'''
Gets all the Job postings on jobs.github site in python domain

'''
import requests
from bs4 import BeautifulSoup

url = "https://jobs.github.com/positions?description=Python"

res = requests.get(url)

if res.status_code == 200:
    s = BeautifulSoup(res.text,"html.parser")

    for i in s.find_all("tr", class_ = "job"):
        print("Position : ",i.td.h4.a.text)

        print("Description Link: ",i.td.h4.a.attrs['href'])

        print("Company Name: ",i.find("a", class_= "company").text)

        print("Company Url: ",i.find('a' ,class_="company").attrs['href'])

        print("Job Type: ",i.find("strong").text)

        print("Job Location: ",i.find("span", class_ = "location").text)
        print("")
else:
    print("Unable to Connect Check Your Internet Connection")
        

