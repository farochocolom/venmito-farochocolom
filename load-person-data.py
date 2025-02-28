import pandas as pd
import yaml, json
import xml.etree.ElementTree as ET

# Parse the people.yml file into a dataFrame
with open('data/people.yml', 'r') as df_json:
    people_data = yaml.safe_load(df_json)
    # people_data_df = pd.DataFrame.from_dict(people_data)
    df_yml = pd.json_normalize(people_data)

# Parse the people.json file into a dataFrame
with open('data/people.json', 'r') as df_json:
    people_data_json = json.load(df_json)
    # people_data_json_df = pd.DataFrame.from_dict(people_data_json)
    people_data_json_df = pd.json_normalize(people_data_json)

# Modify the json dataframe keys to match the yml dataframe keys
df_json = people_data_json_df
df_json['name'] = df_json['first_name'] + ' ' + df_json['last_name']
df_json['city'] = df_json['location.City'] + ', ' + df_json['location.Country']
df_json['phone'] = df_json['telephone']
df_json['id'] = df_json['id'].astype(str).str.lstrip("0").astype(int)
df_json.drop(['first_name', 'last_name', 'location.City', 'location.Country', 'telephone'], axis=1, inplace=True)

df_json['Android'] = df_json['devices'].astype(str).str.contains('Android', na=False).astype(int)
df_json['Iphone'] = df_json['devices'].astype(str).str.contains('Iphone', na=False).astype(int)
df_json['Desktop'] = df_json['devices'].astype(str).str.contains('Desktop', na=False).astype(int)
df_json.drop(['devices'], axis=1, inplace=True)

# Ensure 'id' column exists in both
if 'id' in df_json.columns and 'id' in df_yml.columns:
    # Find missing ids
    missing_ids = df_yml[~df_yml['id'].isin(df_json['id'])]

    # Append missing rows
    df_updated = pd.concat([df_json, missing_ids], ignore_index=True).sort_values('id')

    # Save the updated CSV
    df_updated.to_csv("data/merged_people.csv", index=False)


# Parsing the promotions data into a dataFrame
promotions_data = pd.read_csv('data/promotions.csv')
