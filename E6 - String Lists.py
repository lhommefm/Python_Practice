def palindrome ():
    word = input("What word should I check?")
    left = 0
    right = len(word)-1
    paldrome = True
    while left < right/2:
        if word[left] != word[right]:
            print("This word is not a palindrome")
            paldrome = False
            break
        left = left+1
        right = right-1
    if paldrome == True:
        print("This word is a palindrome")

palindrome()