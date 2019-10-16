def primaryFunc(toEncrypt,key,selectedType,action):
    if selectedType=="string":
        key = key.lower()
        modifiedStr=""   
        if action=="encrypt":
            for i in range(len(toEncrypt)):
                modifiedStr += chr(ord(toEncrypt[i])+ord(key[i%len(key)])-97)
           # return modifiedStr            
        elif action=="decryption":
            for i in range(len(toEncrypt)):
                modifiedStr += chr(ord(toEncrypt[i])-ord(key[i%len(key)])+97)
        return modifiedStr

    elif selectedType=="tuple":
        modifiedTuple=()
        keyTuple=()
        for i in range(len(key)):
            if ord(key[i])<97:
                keyTuple+=chr(ord(key[i])+32),
            else:
                keyTuple+=key[i],
        if action=="encrypt":
            for i in range(len(toEncrypt)):
                modifiedTuple += chr(ord(toEncrypt[i])+ord(key[i%len(key)])-97),
        elif action=="decryption":
            for i in range(len(toEncrypt)):
                 modifiedTuple += chr(ord(toEncrypt[i])-ord(key[i%len(key)])+97),
        return modifiedTuple

    elif selectedType=="list":
        modifiedList = []
        for i in range(len(key)):
            if ord(key[i])<97:
                key[i]=chr(ord(key[i])+32)
        if  action=="encrypt":
            for i in range(len(toEncrypt)):
                modifiedList.append(chr(ord(toEncrypt[i])+ord(key[i%len(key)])-97))
        elif action=="decryption":
            for i in range(len(toEncrypt)):
                modifiedList.append(chr(ord(toEncrypt[i])-ord(key[i%len(key)])+97))
        return modifiedList
   
select = input(" if you Want to encrypt string  - 1 \n  if you Want to encrypt tuple  - 2 \n if you Want to encrypt list  - 3 \n your option is - ")  
if select=="1":
    string = input("Enter string ")
    key = input("Enter key ")
    action = input("encypt or decrypt ")
    print(primaryFunc(string,key,"string",action.lower()))
elif select=="2":
    myTuple = input("Enter string separated  by comma  ") #example: H,E,L,L,O
    key = input("Enter key  separated with commas ")#example: a,b,c
    action = input("encypt or decrypt ")
    list = myTuple.split(",")
    wordtuple = tuple(list)
    list=key.split(",")
    keytuple = tuple(list)
    print(primaryFunc(wordtuple,keytuple,"tuple",action.lower()))
elif select=="3":
    mylist=input("Enter string separated  by commas  ") #example: H,E,L,L,O
    key = input("Enter key  separated with comma ")#example: a,b,c
    action = input("encypt or decrypt ")
    list=mylist.split(",")
    splitlist=list
    list=key.split(",")
    keysplit=list
    print(primaryFunc(splitlist,keysplit,"list",action.lower()))
else:
    print("This option doesn't exist")

        
