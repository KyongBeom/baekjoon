def solution(data, ext, val_ext, sort_by):
    list = ["code", "date", "maximum", "remain"]
    ext_idx = list.index(ext)
    sort_idx = list.index(sort_by)

    answer = []
    for i in range(len(data)):
        if data[i][ext_idx] < val_ext:
            answer.append(data[i])

    answer.sort(key = lambda x: x[sort_idx])
    return answer