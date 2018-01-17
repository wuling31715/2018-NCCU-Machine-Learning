import pandas as pd
import numpy as np



# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
url = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df = pd.read_html(url)
# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it
#
df = df[0].dropna(axis=0, thresh=4)
df.columns = [df.iloc[0]]
df.reset_index()

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df.dropna(axis=0)  # row
df = df.dropna(axis=1)  # column
df = df.reset_index()
#
# TODO: Get rid of the 'RK' column
# .. your code here ..
df = df.drop('RK', axis = 1)
# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df2 = df[1:]
print(df2)

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print(df2['PTC'].unique)
