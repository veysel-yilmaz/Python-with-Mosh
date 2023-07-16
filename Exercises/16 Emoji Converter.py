message = input(">")
words = message.split(' ') #here it splits the input when blank occurs
#Good Morning :)
print(words)
emojis = {
    ":)": "🙂",
    ":))": "😁",
    ":(": "🙁",
    ":D": "😆",
    ";)": "😉"
}
output = ""
for word in words:
    output += emojis.get(word,  word) + " "
#print(words) # output should be printed instead
print(output)
