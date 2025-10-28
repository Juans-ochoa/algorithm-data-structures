# Balance delimiters
from using_linked_list import Stack


def isValidSource(src_file):
    s = Stack()

    for line in src_file:
        for token in line:
            if token in "{[(":
                s.push(token)
            elif token in "}])":
                if s.is_empty():
                    return False
                left = s.pop()
                expression = token == '}' and left != "{" \
                    or token == "]" and left != "[" \
                    or token == ")" and left != "("
                if expression:
                    return False

    return s.is_empty()
