"""
Fjor Robles 
"""
import requests
from bs4 import BeautifulSoup
import json

def web_scraper():
    """ function to get data from a specific website """
    url = 'https://starbucksmenuprice.net'  
    #json data file path in folder
    data_file = "./app/data/menu.json" 

    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # List to store the scraped data
        data = []
        
        # Extracting all 'strong' elements
        name_elements = soup.find_all('strong')
        
        for name in name_elements:
            # Extract the text content of the 'strong' element
            name_text = name.get_text(strip=True)
            
            if name_text:  
                data.append(name_text)
        #skip first five elements of data from webpage
        data = data[5:]
        
        # Write the data to a JSON file
        with open(data_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    scraped_data = web_scraper()
    if scraped_data:
        print("Data successfully scraped and saved.")
    else:
        print("No data found.")
