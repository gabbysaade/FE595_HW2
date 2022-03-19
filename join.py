# Part 2. Join shared files from classmates together

import pandas as pd

# Initialize df variable

# Function to set original dataframe from csv
def data_load():
    df = pd.DataFrame()
    data = pd.read_csv('fake_companies.csv')
    data.drop(columns=data.columns[0], axis=1, inplace=True)

    url1 = 'https://raw.githubusercontent.com/WangJ0347/Webscrape-and-NLP/main/fake_companies.csv'
    url2 = 'https://raw.githubusercontent.com/RiccardoPaladin/FINTECH/main/webscrape_companies.csv'

    df1 = pd.read_csv(url1)
    df2 = pd.read_csv(url2)

    df1.drop(columns=df1.columns[0], axis=1, inplace=True)
    df2.drop(columns=df2.columns[0], axis=1, inplace=True)
    data.columns = df1.columns = df2.columns = ['Name', 'Purpose']

    df = df.append(data)
    df = df.append(df1)
    df = df.append(df2)

    df.to_csv('total_fake_companies.csv')
    return df

if __name__ == '__main__':
    data_load()