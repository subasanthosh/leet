class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif stack and i==')' and stack[-1]=='(':
                stack.pop()
                continue
            elif stack and i==']' and stack[-1]=='[':
                stack.pop()
                continue
            elif stack and i=='}' and stack[-1]=='{':
                stack.pop()
                continue
            else:
                stack.append(i)
                break
        return stack==[]
        

            

        