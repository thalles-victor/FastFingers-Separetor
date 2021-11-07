text = input('Cole no terminal o texto: ')

print('Se usar espaço, então apenas aperte enter')
currentSeparetor = input('Digite o charactere separador atualmente usado: ')
if currentSeparetor == '':
  currentSeparetor = ' '

newSeparetor = input('Digite o charactere que será usado para separar:  ')
if newSeparetor == '':
  newSeparetor = '|'



word = ''
for char in text:
  if (char == currentSeparetor):
    word += newSeparetor
    continue
  
  else:
    word += char

with open("Output.txt", "w") as text_File:
  text_File.write(word)

print( 3 * '\n' + '\033[92m' + word + '\n' * 3)
