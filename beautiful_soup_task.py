# -*- coding: utf-8 -*-
"""Beautiful soup task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbLzWA1nAe4qXVNqq-nswsYmpp-6vPFK
"""

import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
all_jobs = []

jobs = soup.find_all("div", {"class": "card"})
for job in jobs:
    position = job.find('h2').text.strip()
    company = job.find('h3').text.strip()
    location = job.find('p').text.strip()
    date = job.find('time').text.strip()
    
    all_jobs.append({
            "position": position,
            "company": company,
            "location": location,
            "date":date,
        })

for i in all_jobs:
  print(i)
    

keys = all_jobs[0].keys()

with open('job_listing.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_jobs)