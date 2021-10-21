"""
Description from canvas:
Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv
Combines them into a single JSON file called ComicCharacters.JSON
The JSON file should list every character as an object by "Character Name"
Must Contain Object Ownership containing the value Publisher (DC or Marvel)
Must contain the object Characteristics containing the values:
Alignment (Good, Bad, or Neutral)
Eye Color
Hair Color
Gender
When run it should generate a new file
"""
# import pandas

import pandas as pd


# use pandas to read the DC csv and pull the columns we need
# write a new csv from pandas object
df = pd.read_csv (r'dc-wikia-data.csv', usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'])
df.to_csv (r'dc-chars-select.csv', index = None)

# add ending column to ID entries as DC
df = pd.read_csv("dc-chars-select.csv")
df["Publisher"] = "DC"
df.to_csv("dc-chars-select.csv", index=False)

# use pandas to read the Marvel csv and pull the columns we need
# write a new csv from pandas object
df = pd.read_csv (r'marvel-wikia-data.csv', usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'])
df.to_csv (r'marvel-chars-select.csv', index = None)

# add ending column to ID entries as Marvel
df = pd.read_csv("marvel-chars-select.csv")
df["Publisher"] = "Marvel"
df.to_csv("marvel-chars-select.csv", index=False)

# append marvel csv to the end of dc csv
# start by opening the marvel csv
#
with open('marvel-chars-select.csv', 'r') as f1:
    original = f1.read()

with open('dc-chars-select.csv', 'a') as f2:
    f2.write('\n')
    f2.write(original)

# write merged csv into ComicCharacters.json
df = pd.read_csv (r'dc-chars-select.csv')
df.to_json (r'ComicCharacters.json')

print("All files written. Check directory to confirm. Thank you!")

# for concurrency, let's make DC and Marvel happen separately, then append them?
# stretch goal we've already missed. dammit.