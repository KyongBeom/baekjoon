def solution(data, ext, val_ext, sort_by):
    answer = []
    for idx in range(len(data)):
        if ext == "code":
            if data[idx][0] < val_ext:
                answer.append(data[idx])
        elif ext == "date":
            if data[idx][1] < val_ext:
                answer.append(data[idx])
        elif ext == "maximum":
            if data[idx][2] < val_ext:
                answer.append(data[idx])
        else:
            if data[idx][3] < val_ext:
                answer.append(data[idx])
                 
                    
    if sort_by == "code":
        answer.sort(key=lambda answer: answer[0])
    elif sort_by == "date":
        answer.sort(key=lambda answer: answer[1])
    elif sort_by == "maximum":
        answer.sort(key=lambda answer: answer[2])
    else:
        answer.sort(key=lambda answer: answer[3])

    return answer