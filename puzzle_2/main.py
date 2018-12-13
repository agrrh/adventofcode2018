fname = 'input.txt'


def get_dups_count(word, count):
    counts = {i: word.count(i) for i in word}
    return 1 if len(list(filter(lambda x: counts[x] == count, counts))) > 0 else 0


def get_similars(word, list_):
    for pos in range(len(word)):
        b = list(word)
        b[pos] = '?'
        b = ''.join(b)
        for suspect in list_:
            suspect = suspect.strip()
            suspect = suspect
            if word == suspect:
                continue
            a = list(suspect)
            a[pos] = '?'
            a = ''.join(a)
            if a == b:
                return word, suspect
    return None, None


with open(fname) as fp:
    doubles_count = 0
    triples_count = 0

    lines = fp.readlines()
    for id in lines:
        id = id.strip()
        doubles = get_dups_count(id, 2)
        triples = get_dups_count(id, 3)
        # print(id, doubles, triples)

        doubles_count += doubles
        triples_count += triples

        similars = get_similars(id, lines)
        if similars != (None, None):
            result = []
            for letter in similars[0]:
                if letter in similars[1]:
                    result.append(letter)
            # Part 2. What letters are common between the two correct box IDs?
            print(''.join(result))

    # Part 1. What is the checksum for your list of box IDs?
    print(doubles_count * triples_count)
