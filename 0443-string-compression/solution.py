class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0
        write = 0

        while read < n:
            char = chars[read]
            count = 0

            # count repeating characters
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # write character
            chars[write] = char
            write += 1

            # write count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


