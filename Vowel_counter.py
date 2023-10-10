#Write the code of the program that finds the vowels in the sentence and adds these letters to another list.

vowels = ['a','e','ı','i','o','ö','u','ü']
sentence = input("Your Sentence: ")
vowels_found = []

for i in sentence:
    for j in vowels:
        if i == j:
            vowels_found.append(i)

print("Vowels:", set(vowels_found))




