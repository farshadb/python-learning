def minion_game(string):
    given_string = string.upper()
    vowel_sound = ['A', 'E', 'I', 'O', 'U']
    substring = []
    kevin_score = 0
    stuart_score = 0

    length = len(given_string)
    # find all substring and put it in substring array
    for i in range(length):
        for j in range(length + 1):
            if given_string[i:j] != "":
                substring.append(given_string[i:j])
    # find stuart and kevin score
    for i in range(len(substring)):
        if substring[i][0] in vowel_sound:
            kevin_score += 1
        else:
            stuart_score += 1
    if kevin_score > stuart_score:
        return print(f"Kevin {kevin_score}")
    else:
        return print(f"Stuart {stuart_score}")


if __name__ == '__main__':
    s = input()
    minion_game(s)


