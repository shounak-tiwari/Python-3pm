lst = {'name1' : 'Pushpanjali','name2' :'Vidushi','name3' :'Komal','name4' :'Prabhu','name5' :'Shalu','name6' :'Arvind'}
try:
    print(lst['name7'])

except KeyError as e:
    print(e)