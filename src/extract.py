"""Module for extract"""

import requests
import pandas as pd


class DataBase:
    """Class for database"""

    def __init__(self, n=10, url="https://api.hh.ru/vacancies"):
        self.df = pd.DataFrame()
        self.n = n
        self.url = url

    def scrape(self, text, pages=100):
        """
        :param text: Key words for search
        :param pages: How many pages scrape
        """
        for page in range(pages):
            params = {"text": text, "area": 1, "per_page": self.n, "page": page}
            try:
                response = requests.get(self.url, params=params, timeout=10)
                data = response.json()
                self.extract(data)
                # если вакансий меньше чем per_page -> значит вакансии кончились
                if len(data.get("items",{})) < self.n:
                    break

            except TimeoutError as e:
                print(f"Time: {e}")
                break

    def extract(self, data):
        """
        :param data: json-file
        """
        for item in data.get("items",{}):
            item_name = item.get("name", "No Info")

            # salary
            salary = item.get("salary")
            if salary:
                item_salary = f"from {salary.get('from')} to {salary.get('to')} in {salary.get('currency')}"
            else:
                item_salary = "No Info"

            # type
            item_type = item.get("type").get("name", "No Info")

            # address
            item_address = (
                item.get("address").get("name", "No Info")
                if item.get("address")
                else "No Info"
            )

            # other fields
            item_url = item.get("url", "No Info")
            item_schedule = item.get("schedule").get("name", "No Info")
            i = item.get("work_format")
            item_format = (
                i[0].get("name", "No Info")
                if isinstance(i, list) and len(i) > 0
                else "No Info"
            )
            item_exp = item.get("experience").get("name", "No Info")

            self.df = pd.concat(
                [
                    self.df,
                   pd.DataFrame(
                        [
                            {
                                "name": item_name,
                                "salary": item_salary,
                                "type": item_type,
                                "address": item_address,
                                "url": item_url,
                                "schedule": item_schedule,
                                "work_format": item_format,
                                "experience": item_exp,
                            }
                        ]
                    ),
                ],
                ignore_index=True,
            )

