while 1:
    s=input()
    if s=='.':break
    stack=[]
    for c in s:
        if c in'([':
            stack+=[c]
        elif c==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                print('no')
                break
        elif c==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:print('no')
        else:print('yes')