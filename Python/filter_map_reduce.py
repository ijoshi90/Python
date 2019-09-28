nums = [3,4,6,2,3,6,8,5,3]

def is_even(n):
    return n%2 == 0


evens = list(filter(is_even,nums))

print("Even Number : {}".format(evens))
