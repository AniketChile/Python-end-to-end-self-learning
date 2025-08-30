items = ['apple','banana','orange','apple','mango']
duplicate = ""
for item in items:
    if(items.count(item)>1):
        duplicate += item
        break
    
print(duplicate)