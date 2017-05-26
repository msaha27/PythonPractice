import random

my_array = ['a','b','c','d','e','f', 'f']

def shuffle(arr):
    new_array = list()
    var_len = len(arr)
    for i in range(len(arr)):
        rindex     = random.randrange(0,var_len)
        chosen_ele = arr[rindex]
        tmp        = arr[(len(arr)-1)-i] 
        arr[len(arr)-1-i] = chosen_ele
        arr[rindex] = tmp
        var_len -= 1
    return arr
print "Before shuffle: %s " %(my_array)

for i in range (10):
    print "shuffle %d" % i
    my_array = shuffle(my_array)
    print "After shuffle : %s " %(my_array)

