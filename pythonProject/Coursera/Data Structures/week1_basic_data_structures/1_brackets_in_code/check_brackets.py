import time
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    '''Вводятся скобки ()[]{} и проверяется закрытые ли они'''
    opening_brackets_stack = []
    for i in range(len(text)):
        opening_brackets_stack.append(text[i])

        if len(opening_brackets_stack) > 1 and \
                  are_matching(opening_brackets_stack[len(opening_brackets_stack) - 2], text[i]):
            opening_brackets_stack.remove(opening_brackets_stack[len(opening_brackets_stack) - 2])
            opening_brackets_stack.remove(text[i])
        elif text[i] in ']})':
            return i + 1


    return 'Success' if len(opening_brackets_stack) == 0 else len(opening_brackets_stack)


# Мое то работает, но не понимаю что нужно выводить при неправильном ответе...
def find_mismatch_git(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if (top.char == '(' and next != ')') or (top.char == '[' and next != ']') or (top.char == '{' and next != '}'):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"

def main():
    text = input()
    print(find_mismatch_git(text))



if __name__ == "__main__":
    main()
