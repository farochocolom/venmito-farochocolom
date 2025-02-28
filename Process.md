## Personal Info
Name: Fernando J. Arocho Colom
Email: f.arochocolom@gmail.com

## Approach
My approach was mostly about learning the ropes. I wasn't familiar with data engineering before starting with this project so I had to learn about the different tools available for managing files such as pandas, which is the one I chose to go with.
I got familiar with dataFrames to where I managed to parse and combine the data for the `people` files

### Data Ingestion:
Used imports such as pandas, yaml, json, and xml.etree.ElementTree to consume and transform the data.

### Data Matching and Conforming:
1. Since the data in people.yml is simpler than the data in people.json, the json file should be turned into a dataFrame to update the keys such as merging the location object into one value, splitting the devices array into separate values, and "merging" first_name and last_name into a single value to match the keys inside the yml file: 
``` YAML
  Android: 1
  Desktop: 0
  Iphone: 0
  city: Montreal, Canada
  email: Jamie.Bright@example.com
  id: 1
  name: Jamie Bright
  phone: 533-849-3913
```

2. After the data is "cleaned", I would join the data from the yaml dataFrame into the json file dataFrame to add the rows that are in the yaml file but not the json file. 
3. With all the people accounted for on a single file I can now complete the missing data in the promotions csv by looking for the email by their unique phone number or viceversa.
4. Now we can match transactions in the `transactions.xml` to user emails given their phone number and generate a few data points from this. These could be how many times the person has bought an item and the average amount of each item based on all the transactions.

### Data Analysis:
No data analysis was reached, but 
### Data Output:
I was only able to get the data organized for the people files, there is no useful data output outside of that

## How to run the code
1. Clone the repo to your machine
2. open your preferred IDE for python
3. Run the project, you should see the merged_people.csv show up on the project files or get updated if it's already there