def solution(commands):
    answer = []
    _data = []
    merged = []
    for a in range(50):
        _data.append([])
        for b in range(50):
            _data[a].append("EMPTY")

    for c in commands:
        l = c.split()
        if l[0] == "UPDATE":
            if len(l) == 4:
                for m in merged:
                    if m[0] == int(l[1]) and m[1] == int(l[2]):
                        _data[m[2]][m[3]] = l[3]
                _data[m[0]][int(m[1])] = l[3]
            elif len(l) == 3:
                for v1 in _data:
                    for v2 in v1:
                        if v2 == l[1]:
                            v2 = l[2]
        elif l[0] == "MERGE":
            _data[int(l[3])][int(l[4])] = _data[int(l[1])][int(l[2])]
            merged.append([int(l[1]), int(l[2]), int(l[3]), int(l[4])])
        elif l[0] == "UNMERGE":
            for m in merged:
                if m[0] == int(l[1]) and m[1] == int(l[2]):
                    _data[m[2]][m[3]] = "EMPTY"
        elif l[0] == "PRINT":
            answer.append(_data[int(l[1])][int(l[2])])
    return answer
