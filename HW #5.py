
# coding: utf-8

# In[2]:


# Import Dependencies
import pandas as pd


# In[3]:


# Create a reference the CSV file desired
csv_path = "Resources/ufoSightings.csv"

# Read the CSV into a Pandas DataFrame
ufo_df = pd.read_csv(csv_path)

# Print the first five rows of data to the screen
ufo_df.head()


# In[4]:


# Remove the rows with missing data
clean_ufo_df = ufo_df.dropna(how="any")
clean_ufo_df.count()


# In[5]:


# Converting the "duration (seconds)" column's values to numeric
clean_ufo_df["duration (seconds)"] = pd.to_numeric(clean_ufo_df["duration (seconds)"])


# In[6]:


# Filter the data so that only those sightings in the US are in a DataFrame
usa_ufo_df = clean_ufo_df.loc[clean_ufo_df["country"] == "us",:]

usa_ufo_df.head()


# In[11]:


# Count how many sightings have occured within each state
state_counts = usa_ufo_df["state"].value_counts()
state_counts.head()


# In[8]:


# Using GroupBy in order to separate the data into fields according to "state" values
grouped_usa_df = usa_ufo_df.groupby(['state'])

# The object returned is a "GroupBy" object and cannot be viewed normally...
print(grouped_usa_df)

# In order to be visualized, a data function must be used...
grouped_usa_df.count().head(10)


# In[12]:


# Since "duration (seconds)" was converted to a numeric time, it can now be summed up per state
state_duration = grouped_usa_df["duration (seconds)"].sum()
state_duration.head()


# In[15]:


# Creating a new DataFrame using both duration and count
state_summary_table = pd.DataFrame({"Number of Sightings":state_counts,
                                   "Total Visit Time":state_duration})
state_summary_table.head()


# In[21]:


# It is also possible to group a DataFrame by multiple columns
# This returns an object with multiple indexes, however, which can be harder to deal with
grouped_international_data = clean_ufo_df.groupby(['country','state'])

# Converting a GroupBy object into a DataFrame
international_duration = pd.DataFrame(grouped_international_data["duration (seconds)"].sum())
international_duration.head(10)

