freq = 0

history = []
found = False
finished = False

while not (found and finished):
    with open('input.txt') as fp:
        delta = True
        while delta:
            try:
                delta = int(fp.readline())
            except Exception:
                break
            freq += delta

            if not found and freq in history:
                print('again: {}'.format(freq))
                found = True
            history.append(freq)

    if not finished:
        print('result: {}'.format(freq))
        finished = True
