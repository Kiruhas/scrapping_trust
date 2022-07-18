import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.trust.ru/development/property/"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
}

# req = requests.get(url, headers=headers)
# src = req.text

# with open("index.html", "w", encoding="utf=8") as file:
#     file.write(src)

# with open("index.html", encoding="utf=8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")

# cards = soup.find_all(class_="card__inner")

# cards_data = {}
# count = 1

# for item in cards:
#     item_href = "https://www.trust.ru" + \
#         item.find("a", class_="card__title-link").get("href")
#     item_name = str(count) + "_" + \
#         item.find("div", class_="cards-list__item-title").text.strip()
#     count = count + 1
#     cards_data[item_name.replace(" ", "_")] = item_href

# with open("all_cards.json", "w", encoding="utf=8") as file:
#     json.dump(cards_data, file, indent=4, ensure_ascii=False)

count = 1
card_type = "Не указано"

with open("all_cards.json", encoding="utf=8") as file:
    cards_data = json.load(file)

for card_name, card_href in cards_data.items():
    req = requests.get(url=card_href, headers=headers)
    src = req.text

    with open(f"data/{count}.html", mode="w", encoding="utf=8") as file:
        file.write(src)

    with open(f"data/{count}.html", encoding="utf=8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    try:
        card_type = soup.find_all(
            class_="realize-patents-detail__card-meta__text")[1].text.strip()
    except Exception as ex:
        print(ex)

    cards_data[card_name] = {
        "Ссылка": card_href,
        "Тип объекта": card_type
    }
    print(f"{card_name} is done!")
    count += 1
    card_type = "Не указано"

with open("all_cards_with_type.json", "w", encoding="utf=8") as file:
    json.dump(cards_data, file, indent=4, ensure_ascii=False)

print("Work is complete")
