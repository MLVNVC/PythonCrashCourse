rivers = ['Morava', 'Dunav', 'Tisa', 'Drina','Kolubara']
print(len(rivers)) #length of the list
print(sorted(rivers)) #sort temporarily alph.order
print(sorted(rivers, reverse=True)) #sort temporarily reverse alph.order
rivers.reverse() #reverse the order
print(rivers)
print(rivers[1].title()) #print value from index 1, with big first letter
rivers[2] = 'DTD' #changing values
print(rivers)
rivers.append('Ibar') #add value at the end of list
print(rivers)
rivers.insert(4, 'Lim') #insert at index 4 new value
print(rivers)
del rivers[5] #perma delete 
print(rivers)
popped_river = rivers.pop() #remove temporarily from the end of the list
print(rivers)
rivers.pop(4) # remove temporarily from index 4
print(rivers)
rivers.remove('Drina') #remove an item by value
print(rivers)
