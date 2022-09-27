print('Шифр Цезаря')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

step=int(input('Шаг для шифрования:'))%26
line=input('Строка для шифрования:').upper()
result=''
  
for i in line:
    m=alphabet.find(i)
    n=m+step
    if i in alphabet:
        result+=alphabet[n]
    else:
        resuit += i
print('Зашифрованное слово: ',result)


step=int(input('Шаг для шифрования:'))%26
line = input('Строка для расшифровки: ').upper()
result = ''
for i in line:
    m = alphabet.find(i)
    n = m - step
    if i in alphabet:
        result += alphabet[n]
    else:
        result += i
print ('Расшифрованное слово:', result)
 
