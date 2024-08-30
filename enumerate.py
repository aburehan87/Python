items=['banana','apple','orange','seeds','guava']
for i,items in zip(range(len(items)),items):
    print(i,items)
    
fruits=['mango','pomegranate','kiwi','chickoo']#enemerate returns index as well as the item
for i,fruits in enumerate(fruits):
    print(i,fruits)