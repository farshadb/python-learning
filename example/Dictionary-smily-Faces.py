message = input("> ")
words = message.split(" ") # Returns a list with separated words
emojis = {
    ":)": "😀",
    ":(": "😞",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)