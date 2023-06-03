import pandas as pd
 
# Create lists for the data
# Each list will become a pd.Series
pages = ['/python', '/pandas', '/seo', '/excel']
clicks = [400, 300, 200, 100]
 
# Store lists into a dictionary
dictionary = {
    'pages':pages,
    'clicks':clicks
}
 
# Create the DataFrame
df = pd.DataFrame(dictionary)

print(df)
print(df())