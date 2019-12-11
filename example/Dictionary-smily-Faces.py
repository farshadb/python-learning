def imoji_converter(message):
    words = message.split(" ")  # Returns a list with separated words
    emojis = {
        ":)": "😀",
        ":(": "😞",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(imoji_converter(message))



