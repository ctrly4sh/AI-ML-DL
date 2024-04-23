import torch 

'''LLM from Scratch'''

f = open("LLM_from_Scratch\wizard_of_oz.txt" , "r" , encoding="utf-8")
text = f.read()
print(text[:200]) # first 200 characters of the text

#extracting all the characters from the text
characters = sorted(set(text))
print(characters)

#Tokenizer -> consists of a Encoder and decoder
string_to_int = {ch:i for i,ch in enumerate(characters)}
int_to_string = {i:ch for i,ch in enumerate(characters)}

#lambda function for encoding and decoding 
encode = lambda s:[string_to_int[c] for c in s]
encoded = encode("hello")

decode = lambda l: "".join([int_to_string[i] for i in l])
decoded = decode(encode("hello"))

# print("encoded is " ,encoded , "Decoded is " , decoded )

data = torch.tensor(encode(text) , dtype=torch.long)
print(data[:100])





