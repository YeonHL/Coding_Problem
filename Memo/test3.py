""" def solution(cap, n, deliveries, pickups):
    answer = 0
    while(True):
        sv, mv = cap, 0
        for i in range(n):
            if deliveries[n-i-1] == 0 and pickups[n-i-1] == 0:
                pass
            elif deliveries[n-i-1] <= sv:
                sv -= deliveries[n-i-1]
                deliveries[n-i-1] = 0
                if mv <= n-i:
                    mv = n-i
            elif deliveries[n-i-1] > sv:
                deliveries[n-i-1] -= sv
                sv = 0
                if mv <= n-i:
                    mv = n-i
            if sv == 0:
                break
        for i in range(n):
            if deliveries[n-i-1] == 0 and pickups[n-i-1] == 0:
                pass
            elif pickups[n-i-1] + sv <= cap:
                sv += pickups[n-i-1]
                pickups[n-i-1] = 0
                if mv <= n-i:
                    mv = n-i
            elif pickups[n-i-1]+sv > cap:
                pickups[n-i-1] -= (cap-sv)
                sv = cap
                if mv <= n-i:
                    mv = n-i
            if sv == cap:
                break
        answer += 2 * mv
        if set(deliveries) == {0} and set(pickups) == {0}:
            break
    return answer """


def solution(cap, n, deliveries, pickups):
    answer = 0
    while (True):
        gv, tv, mv = cap, 0, 0
        for i in range(n):
            if deliveries[n-i-1] == 0 and pickups[n-i-1] == 0:
                pass
            else:
                if gv == 0 or deliveries[n-i-1] == 0:
                    pass
                else:
                    if deliveries[n-i-1] <= gv:
                        gv -= deliveries[n-i-1]
                        deliveries[n-i-1] = 0
                        if mv <= n-i:
                            mv = n-i
                    elif deliveries[n-i-1] > gv:
                        deliveries[n-i-1] -= gv
                        gv = 0
                        if mv <= n-i:
                            mv = n-i
                if tv == cap or pickups[n-i-1] == 0:
                    pass
                else:
                    if pickups[n-i-1] + tv <= cap:
                        tv += pickups[n-i-1]
                        pickups[n-i-1] = 0
                        if mv <= n-i:
                            mv = n-i
                    elif pickups[n-i-1]+tv > cap:
                        pickups[n-i-1] -= (cap-tv)
                        tv = cap
                        if mv <= n-i:
                            mv = n-i
            if gv == 0 and tv == cap:
                break
        answer += (2 * mv)
        if set(deliveries) == {0} and set(pickups) == {0}:
            break
    return answer
