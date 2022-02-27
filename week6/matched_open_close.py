from pythonds.basic import Stack


def check_open_close(string_in):

    char_stack = Stack()
    matching_chars = {"{": "}", "(": ")", "[": "]"}

    for char in string_in:
        #intitially had longer/more repetitive code (commented out below) for this loop but then had this idea to use a map to make it a little more elegant. could easily add different chars to the map to expand the use of this now

        if char in matching_chars:
            char_stack.push(char)

        elif char in matching_chars.values():
            if char_stack.isEmpty():
                return False

            elif char == matching_chars[char_stack.peek()]:
                char_stack.pop()

            else:
                return False

        ''' 
        #my initial thought for the for loop

        if char == "(" or char == "{" or char == "[":
            char_stack.push(char)

        elif char == ")":
            if char_stack.isEmpty():
                return False
            elif char_stack.peek() == "(":
                char_stack.pop()
            else:
                return False

        elif char == "}":
            if char_stack.isEmpty():
                return False
            elif char_stack.peek() == "{":
                char_stack.pop()
            else:
                return False

        elif char == "]":
            if char_stack.isEmpty():
                return False
            elif char_stack.peek() == "[":
                char_stack.pop()
            else:
                return False
        '''

    if not char_stack.isEmpty():
        return False

    return True


'''
# Tests
print(check_open_close("(aaa[bbb{ccc}bbb]aaa)"))
print(check_open_close("(({})[])("))
print(check_open_close("][][][]"))
print(check_open_close("top{big{mediu}m(small[tiny])}}"))
print(check_open_close("top{big{medium(small[ti[ny])}}"))
'''
