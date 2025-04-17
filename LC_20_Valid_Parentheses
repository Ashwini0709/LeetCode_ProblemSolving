class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = { "]":"[", "}":"{", ")":"(" }

        for i in s:
            if i in closetoOpen:
                if len(stack) == 0 and closetoOpen[i]:
                    return False
                elif closetoOpen[i] != stack.pop():
                    return False
            else:
                stack.append(i)


        return True if len(stack) == 0 else False

