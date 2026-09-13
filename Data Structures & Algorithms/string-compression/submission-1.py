class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        result = ""
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                result += chars[i-1]
                if count != 1:
                    result += str(count)
                count = 1

        result += chars[-1]
        if count != 1:
            result += str(count)

        print(result)
        
        chars[:] = list(result)
        
        return len(result)


        