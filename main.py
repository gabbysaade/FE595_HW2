# Homework 2

# Part 1. Extract the name and the purpose of about 50 randomly generated companies from the company generator
# Save this to a file on your computer.

import requests
import pandas as pd

# Create empty list to store webscraping data
scrape = []
name = []
purpose = []


# Perform get request in loop to ensure all 50 companies
def get_req():
    for i in range(50):
        url = "http://34.238.119.208:8000/random_company"
        info = requests.get(url)
        if info.status_code == 200:
            lines = info.text.split('\n')
            scrape.append(lines)
        else:
            print("Error, Incorrect Status Code:", info.status_code)
            break
    return scrape


# Put only name and purpose data in lists
def get_name():
    for i in range(50):
        for x in scrape[i]:
            if 'Name:' in x:
                name.append(x)
    return name


def get_purpose():
    for i in range(50):
        for x in scrape[i]:
            if 'Purpose:' in x:
                purpose.append(x)
    return purpose


# Clean, compile, and save data
def clean_compile():
    name_clean = str(name)
    name_clean = name_clean.replace('            <li>Name: ', '')
    name_clean = name_clean.replace('</li>', '')
    name_clean = name_clean.split("', '")
    name_clean[0] = name_clean[0].replace("['", "")
    name_clean[-1] = name_clean[-1].replace("']", '')
    name_df = pd.DataFrame(name_clean)

    purpose_clean = str(purpose)
    purpose_clean = purpose_clean.replace("'            <li>Purpose: ", "")
    purpose_clean = purpose_clean.replace("</li>'", "")
    purpose_clean = purpose_clean.split(', ')
    purpose_clean[0] = purpose_clean[0].replace('[', '')
    purpose_clean[-1] = purpose_clean[-1].replace(']', '')
    purpose_df = pd.DataFrame(purpose_clean)

    df = pd.concat([name_df, purpose_df], axis=1)
    df.columns = ['Name', 'Purpose']
    df.to_csv('fake_companies.csv')
    return df


if __name__ == "__main__":
    get_req()
    get_name()
    get_purpose()
    clean_compile()
