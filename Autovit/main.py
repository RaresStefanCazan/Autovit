import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_autovit():
    url = "https://www.autovit.ro/autoturisme"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Nu se poate accesa pagina {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    car_elements = soup.find_all('article', attrs={'data-id': True})
    print(f"Am gasit {len(car_elements)} anunturi.")  

    car_data = []
    for car in car_elements:
        try:
            
            name_tag = car.find('p', class_='e2z61p70 ooa-1ed90th er34gjf0')
            if name_tag:
                name = name_tag.text.strip()
            else:
                name = 'N/A'

            
            price_tag = car.find('h3', class_='e6r213i1 ooa-1n2paoq er34gjf0')  
            price = price_tag.text.strip() if price_tag else 'N/A'

            
            mileage_tag = car.find('dd', class_='ooa-1omlbtp ecru18x13')  #  ooa-1omlbtp ecru18x13
            mileage = mileage_tag.text.strip() if mileage_tag else 'N/A'

            
            year_tag = car.find('dd', class_='ooa-1omlbtp ecru18x13', attrs={"data-parameter": "year"})
            year = year_tag.text.strip() if year_tag else 'N/A'

            
            car_data.append({
                "name": name,
                "price": price,
                "mileage": mileage,
                "year": year
            })
        except AttributeError as e:
            print(f"Eroare: {e}")
            continue

    return car_data

def save_to_json(data, filename="cars.json"):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError):
        existing_data = []

    existing_data.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "cars": data
    })

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)
    print(f"Datele au fost salvate în {filename}")

if __name__ == "__main__":
    car_data = scrape_autovit()
    if car_data:
        print("Informatiile extrase despre masini:")
        for car in car_data:
            print(f"Nume: {car['name']}, Pret: {car['price']}, Kilometraj: {car['mileage']}, An: {car['year']}")
        
        save_to_json(car_data)
    else:
        print("Nu au fost gasite informatii despre masini.")
