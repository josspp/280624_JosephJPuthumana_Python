def double_evens(int_list):
    return [2*i if i%2==0 else i for i in int_list]

double_evens([i for i in range(10)])