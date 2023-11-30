from stack import Stack  

def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return "0"

    stack = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        stack.push(remainder)
        dec_num //= 2

    binary_equivalent = ""
    while not stack.is_empty():
        binary_equivalent += str(stack.pop())

    return binary_equivalent


dec_num = 10
result = convert_int_to_bin(dec_num)

print(f"The binary equivalent of {dec_num} is: {result}")
