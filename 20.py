class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for l in s:
            if l == '{' or l == '(' or l == '[':
                st.append(l)
            else:
                if (len(st) == 0) or (l == ')' and st.pop() != '(') or (l == ']' and st.pop() != '[') or (l == '}' and st.pop() != '{'): return False

        return len(st) == 0
