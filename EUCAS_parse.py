from bs4 import BeautifulSoup

# Grab your html source here and open it up within Python.
html = open("EUCAS.txt")

# Generate the bs object.
bsobj = BeautifulSoup(html.read())

# findAll returns a list of hited items.
# .contents extract the content within a tag.
# pass IndexError enable a more flexible way for handling format change.
for item in bsobj.findAll('td',{"class":"black10px ef-abstract-description"}):
    try:        
        print(item.contents[1].contents[0] + ' ' + item.contents[3].contents[0])
    except:        
        pass
