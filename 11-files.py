#open file
myFile = open('myfile.txt', 'w')

#Get some info
print('File Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

#write to file
myFile.write('Ami loves Python')
myFile.write(' and JavaScript,')
myFile.close()

#Append to file
myFile = open('myfile.txt', 'a')
myFile.write('also PHP :)')
myFile.close()

#Read from file
myFile = open('myfile.txt', 'r')
text = myFile.read(20)
print(text)