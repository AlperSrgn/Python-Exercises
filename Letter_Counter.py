#Write a program that calculates the number of times the letter we want occurs in a text.

sentence = input("Sentence: ")
letter = input("Letter: ")
count = 0

for i in sentence:
    if i == letter:
        count+=1

print("{} letters '{}' found".format(count,letter))