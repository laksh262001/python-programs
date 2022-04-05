'''
fhr=open("data.txt","r")
line1=fhr.readline()    
print(line1,end="")
line2=fhr.readline()    
print(line2,end="")
line3=fhr.readline()    
print(line3,end="")

fhr=open("data.txt","r")
list_var=fhr.readlines()
for line in list_var:
    print(line,end="") 
fhr.close()

fhr=open("data.txt","r")
data =fhr.read(10)
print(data)
fhr.close()

fhr=open("data.txt","r")
data =fhr.read()
print(data)
fhr.close()

fhr=open("data.txt","r")
for line in fhr:
    print(line,end="")
fhr.close()
'''


'''
fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","w")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
'''


'''
fhr=open("data.txt","r")
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
fhr.close()
'''



'''
fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()
'''

fhr=open("data.txt","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("closed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)
