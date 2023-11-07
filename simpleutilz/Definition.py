import requests
from bs4 import BeautifulSoup
import csv

def createDataset():
    url = "https://css-tricks.com/snippets/css/named-colors-and-hex-equivalents/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        
        if tables:
            with open('colors.csv', 'w') as file:
                for table in tables:
                    table_data = []
                    rows = table.find_all('tr')
                    
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        row_data = [cell.get_text(strip=True) for cell in cells]
                        table_data.append(row_data)
                    
                    for row in table_data[1:]:
                        hex_code = row[1].strip()
                        color_name = row[0].strip()
                        file.write(f"{hex_code},{color_name}\n")
            
            print("Data from all tables saved to 'colors.csv'")
        else:
            print("No tables found on the page.")
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    
    convertToDenary()

def convertToDenary():
    with open ("colors.csv", "r") as file:
        f = open("denary.csv", "a")
        for line in file:
            line = line.split(",")
            hexvalue = line[0]
            colour = line[1]
            denary = int((hexvalue.replace("#","")), 16)
            f.write(f"{denary},{colour}")
    
    sortDataset()

def sortDataset():
    input_file = "denary.csv"

    with open(input_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    sorted_data = sorted(data, key=lambda x: int(x[0]))
    output_file = "sorted_denary.csv"

    with open(output_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sorted_data)

    print(f"Data sorted and saved to {output_file}")
