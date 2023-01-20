
# Nathan Hutton

def Brackets(s):
    s = [char for char in s]
    while s:
        bracket = s.pop(0)
        if bracket == '(':
            if ')' in s:
                s.remove(')')
                continue
        elif bracket == '[':
            if ']' in s:
                s.remove(']')
                continue
        elif bracket == '{':
            if '}' in s:
                s.remove('}')
                continue
        return False
    return True
