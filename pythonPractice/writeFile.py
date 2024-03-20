
data = {
    "LAYP:" : "Layena Pellets"
    }

newData = {}
#Reads file.
with open('dataTest.txt','w') as fileObject :
    for element in data : 
        fileObject.write(f'{element} {data[element]}\n')
#Writes file.        
with open('dataTest.txt','r') as fileObject :
    for line in fileObject :
        line = line.strip()
        arguments = line.split(':')
        if len(arguments) != 2 : continue
        newData[arguments[0]] = arguments[1]
        
print(newData)        