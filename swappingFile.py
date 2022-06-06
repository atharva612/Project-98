def swapFileData():
    fileName=input("Enter Name of file: ")
    replaceFile=input("Enter file name you want to replace with: ")
    data_a=open(fileName)
    with open("file1.txt",'r') as a:
        data_a=a.read()
    
    data_b=open(replaceFile)
    with open("file2.txt",'r') as b:
        data_b=b.read()

    with open("File1.txt",'w') as at:
        at.write(data_b)

    with open("File2.txt",'w') as bt:
        bt.write(data_a)

    print()
swapFileData()

    

  
    


    