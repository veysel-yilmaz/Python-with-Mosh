# as a general rule of thumb: dont imclude input and print functions in a function definition
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":))": "😁",
        ":(": "🙁",
        ":D": "😆",
        ";)": "😉"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# don't forget to add second blank line to remove yellow lines under the line.
message = input(">")
"""
result = emoji_converter(message)
print(result)
or use the code below
"""
print(emoji_converter(message))
