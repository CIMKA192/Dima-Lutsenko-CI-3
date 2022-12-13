with open("file.txt",'r',encoding='utf8') as txt: 
    data = txt.read() 
word1 = input("Введіть 1 слово: ") 
word2 = input("Введіть 2 слово: ") 
data = data.replace(word1,word2) 
with open("file.txt",'w',encoding='utf8') as result: 
    result.write(data)
    