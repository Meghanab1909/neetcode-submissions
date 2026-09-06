class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    top = stack.pop()

                    if i == ")" and top != "(":
                        return False
                    elif i == "}" and top != "{":
                        return False
                    elif i == "]" and top != "[":
                        return False
                else:
                    return False
        return len(stack) == 0

        