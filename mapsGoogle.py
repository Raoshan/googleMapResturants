import os
import pandas as pd
from urllib.parse import urlsplit, parse_qsl
from serpapi import GoogleSearch
floderPath = os.path.join('C:/Users/RDATS/Desktop/Projects/Data')
params = {
  "api_key": "fa91dd75a3fb04b90c170c2ffe7a8ee9614f95550bbbbfc912c0277e082048f3",
  "engine": "google_maps",
  "type": "search",
  "google_domain": "google.com",
  "q": "Coffee",
  "hl": "en",
  "ll": "@40.7455096,-74.0083012,14z"
}
search = GoogleSearch(params)
all_Details = []
while True:
    results = search.get_dict()
    try:
        details = results['local_results']
        print(len(details))
        all_Details = []
        for item in details:
            CompanyName = item['title']
            print(item['title'])
            CompanyType = item['type']
            print(item['type'])
            Rating = item['rating']
            print(item['rating'])
            Reviews = item['reviews']
            print(item['reviews'])
            Address = item['address']
            print(item['address'])
            Phone = item['phone']
            print(item['phone'])
            Website = item['website']
            print(item['website'])
            all_Details.append([CompanyName, CompanyType, Rating, Reviews, Address, Phone, Website])
    except:
        print('Done')
        break

    if (not 'serpapi_pagination' in results) and (not 'next' in results['serpapi_pagination']):
        break

    search.params_dict.update(
        dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
datadf = pd.DataFrame(all_Details, columns=['CompanyName', 'CompanyType', 'Rating', 'Reviews', 'Address', 'Phone', 'Website'])
datadf.to_csv(os.path.join(floderPath, 'Resturent.csv'), index=False)
print("run successfully......")