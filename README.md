# Autovit Crawler

This project implements a crawler for [autovit.ro](https://www.autovit.ro/), designed to extract data about the best car offers promoted on the website's first page. The crawler retrieves information such as the **name**, **price**, **year**, and **mileage** of the advertised cars. Each day, the extracted information is appended to a JSON file, gradually building up a history of the best deals.

## Project Overview

- **Daily Data Extraction:**  
  The crawler is intended to run once per day, capturing the most promoted car offers from autovit.ro.

- **Extracted Data:**  
  For each car, the following information is collected:
  - **Name**
  - **Price**
  - **Year**
  - **Mileage**

- **Data Storage:**  
  The collected data is saved in a JSON file (`cars.json`). Each day's extraction is stored as a separate entry, including the date and the corresponding list of cars, ensuring that historical data is preserved.

## Requirements

- Python 3.x
- Python libraries:
  - `requests`
  - `beautifulsoup4`
  
You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
