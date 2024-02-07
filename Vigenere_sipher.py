def visioner(m, k):
    message = m.upper()
    key = k.upper()
    if len(key) > len(message):
        return False
    answer = ""
    keyiter = 0
    a = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    keynums = [a.find(i) + 1 for i in key]

    for i in range(len(message)):
        if message[i] not in a:
            answer += message[i]
        else:
            if keyiter == len(key):
                keyiter = 0
            nextindex = keynums[keyiter] + a.index(message[i]) + 1
            if nextindex > len(a):
                nextindex -= len(a)
            answer += a[nextindex - 1]
            keyiter += 1
    return answer
