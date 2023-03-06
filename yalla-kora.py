import requests
from bs4 import BeautifulSoup
import csv
import os
import datetime

# Save the date in value
date = input("Please enter a Date in the following format MM/DD/YYYY: ")
# Url of the website yalla kora
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")
# Save the data in the folder
date_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
date_str = date_obj.strftime("%Y-%m-%d_%H-%M-%S")
dir_name = date_obj.strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"{dir_name}/match_details_{date.replace('/', '-')}.csv"

def main(page):
    src = page.content

    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all('li')
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            team_A = all_matches[i].find('div', {'class' : 'teamA'}).text.strip()
            team_B = all_matches[i].find('div', {'class' : 'teamB'}).text.strip()

            # Get score
            match_result = all_matches[i].find('div', {'class' : 'MResult'}).find_all('span', {'class' : 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            # Get match time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()

            # Add Match info to matches details
            matches_details.append(
                {"Championship": championship_title, "team A": team_A, "team B": team_B, "match time": match_time,
                 "score": score})
    for i in range(len(championships)):
            get_match_info(championships[i])

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

   # Check if the date have data
    if matches_details:
        keys = matches_details[0].keys()
        with open(file_name, 'w', newline='', encoding='utf-8', errors="ignore") as output_file:
            dict_writer = csv.DictWriter(output_file,keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)
            print("file created")
    else:
        print("No matches found for the given date.")

main(page)