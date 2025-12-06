def reverse_string(string: str) -> str:
    n = len(string)

    def reverse(reversed = "", tail = 0):
        if tail == n:
            return reversed
        reversed += string[n - 1 - tail]

        return reverse(reversed, tail = tail + 1)
    
    return reverse()

print(reverse_string("banana"))
