""" We have seen that lists are mutable (they can be changed),
and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it."""

def mutation():
    string="Apple"
    n=list(string)

    n[2]='l'

    new_str=''.join(n)

    return new_str
v=mutation()
print(v)