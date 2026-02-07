from extract import DataBase
from load import add_to_csv

texts = ["Data Analyst", "Data Enginer", "Data Scientist", "ML", "Python"]

db = DataBase()

for text in texts:
    try:
        print(f"Try to scrape data with {text}")
        db.scrape(text)
    except TimeoutError as te:
        print(te)

print("Load in csv file")
add_to_csv(db.df)
