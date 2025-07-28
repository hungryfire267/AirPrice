import gzip
import os
import requests
import shutil 

listings_url = "https://data.insideairbnb.com/australia/qld/sunshine-coast/2025-05-31/data/listings.csv.gz"
data_path = r"C:\Users\Gordon Li\Desktop\AirPrice\AirPrice\data"

response = requests.get(listings_url)
if response.status_code == 200: 
    data_gz = os.path.join(data_path, "listings.csv.gz")
    with open(data_gz, "wb") as f: 
        f.write(response.content)
    print(f"Downloaded to path {data_gz}")
    
    data_csv = os.path.join(data_path, "listings.csv")
    with gzip.open(data_gz, "rb") as f_in: 
        with open(data_csv, "wb") as f_out: 
            shutil.copyfileobj(f_in, f_out)
    print("Extraction complete")
else: 
    print(f"Failed to download. Status code {response.status_code}")
    