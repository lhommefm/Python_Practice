def input_string(question="Tell me a phrase"):
    answer = input(question)
    return answer

def reverse_word_order():
    string = input_string()
    lis = string.split()
    lis = reversed(lis)
    string = " ".join(lis)
    return string

reverse_word_order()