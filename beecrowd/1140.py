while True:
    phrase = input().strip()

    if phrase == '*':
        break

    words = phrase.split()
    first_letter = words[0][0].lower()

    print('Y') if all(word[0].lower() == first_letter for word in words) else print('N')
