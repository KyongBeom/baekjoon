def solution(numbers):
    answer = []
    i = 0
    j = i + 1
    while True:
        if i > len(numbers):
            break
        
        if j < len(numbers):
            k = numbers[i] + numbers[j]
            if k not in answer:
                answer.append(k)
            j += 1
        else:
            i += 1
            j = i + 1
    return sorted(answer)