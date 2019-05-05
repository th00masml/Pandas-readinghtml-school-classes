import pandas as pd

# Defines website, to get first page of data
website = 'https://ischool.syr.edu/classes/?page=1'

# Assigning data do variable
data = pd.read_html(website)

# Generating links to all pages
website = 'https://ischool.syr.edu/classes/?page='
classes = pd.DataFrame() #  (columns are = ['Course','Section','ClassNo','Credits','Title','Instructor','Time','Days','Room'])

# Here is the function, that appends all 6 pages
for i in range(1,6):
    link = website + str(i)
    data = pd.read_html(website  + str(i))    
    classes = classes.append(data[0], ignore_index=True)

classes.columns = ['Course','Section','ClassNo','Credits','Title','Instructor','Time','Days','Room'] # Adding collumns

# Let's see the first results 
print (classes.describe())
print (classes.head(5))

# Creating ,Subject' and 'Number' columns
# Note that first three letters from 'Course' collumn describes class subject and remaining numbers describes class number
classes['Subject'] = classes['Course'].str[0:3]
classes['Number'] = classes['Course'].str[3:]

# Creating 'Type' column. Knowing the fact that >500 courses are availabile only for undergrads
pd.options.mode.chained_assignment = None
classes['Type'] = ''
classes['Type'][classes['Number'] < '500'] = 'UGrad'
classes['Type'][classes['Number'] >= '500'] = 'Grad'

# Now let's look at sample of output data
print (classes.sample(5))

