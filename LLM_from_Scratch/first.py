f = open("wizard_of_oz.txt" , "r" , encoding="utf-8")
text = f.read()
print(text[:200]) # first 200 characters of the text

#extracting all the characters from the text
characters = sorted(set(text))
print(characters)

#Tokenizer -> Encoder and decorder