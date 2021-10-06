import library 

marvel_data = library.loadList('marvel-data.csv')
dc_data = library.loadList('dc-data.csv')

#page_id,name,urlslug,ID,ALIGN,EYE,HAIR,SEX,GSM,ALIVE,APPEARANCES,FIRST APPEARANCE,YEAR
col = {'name':1,'identity':3,'align':4,'sex':7,'alive':9}

print("Below is a list of all the female good living charachters in the dc and marvel universes, \nand some information on them: ")

list = []

def listBuilder(data,universe):
    if data[n][col['sex']] == 'Female Characters' and data[n][col['align']] == 'Good Characters' and data[n][col['alive']] == 'Living Characters':
        name = data[n][col['name']]
        identity = data[n][col['identity']]
        list.append([name,identity,universe])

for n in range(len(marvel_data)):
    listBuilder(marvel_data,'marvel')

for n in range(len(dc_data)):
    listBuilder(dc_data,'DC')

for i in list:
    print(i)
