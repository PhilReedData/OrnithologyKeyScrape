#sort
import pandas as pd 
df = pd.read_csv('blocks.csv', na_filter=False)
df['entry_lower'] = df['entry'].str.lower()
df = df.sort_values('entry_lower')
del df['entry_lower']
df = df.rename({'def': 'definition'}, axis=1) # avoid reserved word

html_head = """<html>
<head>
<title>Key to Scientific Names in Ornithology</title>
<style>
	th {
    	text-align: left;
    	vertical-align: top;
    	color: #C4202B;
    	background-color: lightgray;
	}
	td {
		background-color: #eee;
	}
</style>
</head>
<body>
<table><tr><th>entry></th><th>defintion</th></tr>
"""

html_tail = '</body></html>'

# Create an empty list 
html_rows =[] 
  
# Iterate over each row 
for index, rows in df.iterrows(): 
    # Create html of the current row
    tr = '<tr><th>' + rows.entry + '</th><td>' + rows.definition + '</td>\n'
      
    # append the row to the final list 
    html_rows.append(tr) 
  
# Print the list 
filename = 'blocks.html'
with open(filename, 'w') as f:
	f.write(html_head)
	for tr in html_rows:
		f.write(tr)
	f.write(html_tail)