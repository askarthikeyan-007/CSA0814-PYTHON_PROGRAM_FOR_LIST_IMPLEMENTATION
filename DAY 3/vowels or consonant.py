sentence  = "hello world"
vowels = sum(1 for in sentence)
consonant = sum(1 for in sentence if char(sample and char(vowels)not in 'a,e,i,o,u'))
print(f"vowels:{vowels},consonant:{consonant}")