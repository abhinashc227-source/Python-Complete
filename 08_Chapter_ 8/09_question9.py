# WAF to print the length of the list

def my_list():
    l = [1,2,3,4,5,5,6]
    print(len(l))
    return l
my_list()


#WAF to print the list of the elements in the single line(list of parameter)


def my_list(l):
    for i in l:
     print(i,end=" ")
     

my_list([1,2,3,5,6,7,8])