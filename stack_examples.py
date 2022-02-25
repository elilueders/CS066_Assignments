from pythonds.basic import Stack


def check_open_close(string_in):

    char_stack = Stack()

    for char in string_in:

        if char == "(" or "{" or "[":
            char_stack.push(char)

        if char == ")":
            if char_stack.isEmpty():
                return False
            else:
                char_stack.pop()

        if char == "}":
            if char_stack.isEmpty():
                return False
            else:
                char_stack.pop()
                
        if char == "]":
            if char_stack.isEmpty():
                return False
            else:
                char_stack.pop()

    if char_stack.isEmpty():
        return True

    while not char_stack.isEmpty():
        print(char_stack.pop())

    return False


print(check_open_close("([{}])"))
