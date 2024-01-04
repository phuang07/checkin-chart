from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import os

from matplotlib import rcParams

import numpy as np

import gspread
import seaborn as sns

# Configure Matplotlib to use a Chinese font
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['SimHei']  # Use 'SimHei' or your installed Chinese font
from dotenv import load_dotenv
load_dotenv()

gc = gspread.service_account()
img_dir = os.getenv('IMG_DIR')

url = 'https://docs.google.com/spreadsheets/d/1v85-Fp_YWwoHOT7dtLw8HeHOaL3bxS5yGSOob-2fifQ/edit?usp=sharing'
spreadsheet = gc.open_by_url(url)
# spreadsheet = gc.open("Testme")
data = spreadsheet.sheet1.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

df = df.applymap(lambda x: ''.join(filter(str.isalpha, x)).capitalize() if isinstance(x, str) else x)

# replace Matthewhappybrian with Brian
df = df.replace('Matthewhappybrian', 'Brian')
df = df.replace('李哲esther', 'Esther')

#drop empty values
df = df.replace('', np.nan)
# drop empty rows and columns
# df = df.dropna(axis=1, how='all')

def chart_individual(df):
    # Count the number of occurrences of each name across all days
    name_counts = Counter(df.values.flatten())

    # Remove empty string counts
    del name_counts[""]

    # Prepare data for bar chart
    names = list(name_counts.keys())
    counts = list(name_counts.values())

    # mark y-axis with count 1 per tick
    yticks = np.arange(0, max(counts) + 1, 1.0)



    # Create a bar chart
    plt.figure(figsize=(12, 10))
    sns.barplot(x=names, y=counts, palette='deep')
    plt.xticks(rotation=45)
    # make yticks integers, not floats and use 1 increment
    plt.yticks(yticks, yticks.astype(int))
    plt.xlabel('Names')
    plt.ylabel('Count')
    plt.title('Frequency of Names Across Days')
    plt.show()
    
    plt.savefig('individual.png')

def chart_daily_toal(data):
    print(data)
    # calculate the total count for each day excluding the empty string
    daily_totals = data.apply(lambda x: x.count())


    plt.figure(figsize=(20, 6))
    sns.barplot(x=daily_totals.index, y=daily_totals.values, palette='muted')
    plt.title('Daily Total Counts')
    plt.xlabel('Day')
    plt.ylabel('Total Count')
    plt.xticks(rotation=45)

    # make x-axis labels smaller
    plt.tick_params(axis='x', which='major', labelsize=8)

    plt.show()
    plt.savefig('daily_total.png')


chart_individual(df)
chart_daily_toal(df)



