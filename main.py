
# an array for all the letters in the alphabet (repeated to avoid index errors)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# User input 
direction = input("Type 'decode' to encrypt, type 'decode' to decrypt:\n").lower()
textInput = input("Type your message:\n").lower()
shiftInput = int(input("Type the shift number:\n"))

# function call 
def caesarCipher(text,shift,method):
  # initialize empty string for new output
  newString = ""
  # loop through each letter in the textInput
  for e in text:
    #if current element is a space, add a space to newString
    if e.isspace():
      newString += " "
      
    elif method == "encrypt":
      #find the index in alphabet list using the current letter 
      oldLetterIndex = alphabet.index(e)
      newLetterIndex = oldLetterIndex+shift
      newLetter = alphabet[newLetterIndex]
      newString += newLetter
      
    elif method == "decode":
      
      oldLetterIndex = alphabet.index(e)
      newLetterIndex = oldLetterIndex-shift
      newLetter = alphabet[newLetterIndex]
      newString += newLetter
    else:
      print("Sorry, that was a invalid choice")
    
  # print the string at the end of the for loop 
  print(newString)
  

caesarCipher(text = textInput, shift = shiftInput,method = direction)









  


