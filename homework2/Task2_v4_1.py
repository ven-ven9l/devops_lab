# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

list = []
l = [str(input("Enter command: ")) for i in range(int(input("Enter N: ")))]
for x in l:
    x = x.split()
    # 1 insert i e: Insert integer i at position e.
    if x[0] == "insert":
        list.insert(int(x[1]), int(x[2]))
    # 2 print: Print the list.
    elif x[0] == "print":
        print(list)
    # 3 remove e: Delete the first occurrence of integer e
    elif x[0] == "remove":
        list.remove(int(x[1]))
    # 4 append e: Insert integer e at the end of the list.
    elif x[0] == "append":
        list.append(int(x[1]))
    # 5 sort: Sort the list.
    elif x[0] == "sort":
        list.sort()
    # 6 pop: Pop the last element from the list.
    elif x[0] == "pop":
        list.pop()
    # 7 reverse: Reverse the list.
    elif x[0] == "reverse":
        list.reverse()
