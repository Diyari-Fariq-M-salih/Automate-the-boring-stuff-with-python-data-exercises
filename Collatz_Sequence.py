def Collatz_Sequence(number):
    final_value = 1
    value = number
    while True:
        if ((value % 2) == 0):
            value = value // 2
        else:
             value = (3 * value) + 1 
        final_value = value
        print(final_value)
        if value == 1:
            print("End of sequence")
            break
    return final_value

Collatz_Sequence(10)