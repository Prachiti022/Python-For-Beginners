class ReverseString:
    def reverse(self, s):
        return ' '.join(s.split()[::-1])

# Creating an object
rev = ReverseString()
print(rev.reverse("Hello World"))
