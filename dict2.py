#using forloop
capitals={'India':'New Delhi',
          'Russia':'Moscow',
          'China':'Beijing',
          'USA':'Washington DC'}
for key,values in capitals.items():
    print(key,values)
    
#add a element to dic using update()
capitals.update({"Germany":"Berlin"})
print(capitals)
#update an existing element
capitals.update({'USA':'Las Vegas'})
print(capitals)
#remove an element using pop
capitals.pop("China")
print(capitals)
#clear all elements
capitals.clear()
print(capitals)