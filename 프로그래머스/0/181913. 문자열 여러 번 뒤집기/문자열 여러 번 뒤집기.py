def solution(my_string, queries):
    for i in queries:
        my_string = my_string[:i[0]] + my_string[i[0]:i[1]+1][::-1] + my_string[i[1]+1:]
    return my_string