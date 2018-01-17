import pandas as pd
import numpy as np
# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_csv('Datasets/servo.data')
df.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
five = 0
#print(df.loc[:,['vgain']])
for row in df['vgain']:
    if row == 5:
        five = five + 1
print(five)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
E = 0
for row1, row2 in zip(df['motor'], df['screw']):
    if row1 == 'E' and row2 == 'E':
        E = E + 1
print(E)




# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
vgain = []
for row1, row2 in zip(df['vgain'], df['pgain']):
    if row2 == 4:
        vgain.append(row1)
np_vgain = np.array(vgain)
print(np_vgain.mean())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



