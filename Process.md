### Data Ingestion:
Your solution should be able to read and load data from all the provided files. Take into account that these files are in different formats (JSON, YAML, CSV, XML).

### Data Matching and Conforming:
Since the data in people.yml is simpler than the data in people.json, the json file should be split into a data table like a CSV and the converted into a YAML by merging the location object into one value, splitting the devices array into separate values, and "merging" first_name and last_name into a single value also to match the structure of 
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

### Data Analysis:
Your solution should be able to process the conformed data to derive insights about our clients and transactions. This would involve implementing data aggregations, calculating relevant metrics, and identifying patterns. These insights will be invaluable in helping us understand our clientele and transaction trends better. Examples of things, but is not restricted to, we want to be able to see are:

Which clients have what type of promotion?
Give suggestions on how to turn "No" responses from clients in the promotions file.
Insights on stores, like:
What item is the best seller?
What store has had the most profit?
Etc.
How can we use the data we got from the transfer file?
These are only suggestions. Please don't limit yourself to only these examples and explore in your analysis any other suggestions could be beneficial for Venmito.

### Data Output:
The final output of your solution should enable us to consume the reorganized and analyzed data in a meaningful way. This could be, but is not restricted to, a command line interface (CLI), a database with structured schemas, a GUI featuring interactive visualizations, a Jupyter Notebook, or a RESTful API. We invite you to leverage other innovative methods that you believe would be beneficial for a company like Venmito. Please provide at least 2 data consumption methods, 1 for the non-technical team and 1 for the technical team.

### Code:
The code for your solution should be well-structured and comprehensible, with comments included where necessary. Remember, the quality and readability of the code will be a significant factor in the evaluation of the final deliverable.