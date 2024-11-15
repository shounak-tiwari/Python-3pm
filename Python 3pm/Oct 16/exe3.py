lst = ['Pushpanjali','Vidushi','Komal','Prabhu','Shalu','Arvind']

print(len(lst))

try:
    print(lst[4])

except IndexError as e:
    print(e)


except:
    pass