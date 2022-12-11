from stk import Stack as St

stack = St()
l = input('Введите скобки балят')
for c in l:
    if c == ')':
        if stack.top() is None:
            print('Не верное количество скобок')
            stack.push(c)
            break
        else:
            stack.pop()
    else:
        stack.push(c)

if stack.top() is None:
    print('Верное количество скобок')
else:
    print('Не верное количество скобок')