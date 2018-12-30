from difflib import SequenceMatcher

with open('input.txt') as fp:
    lines = [_.strip() for _ in fp.readlines()]

    similarity_max = (0, "", "")

    for word_a in lines:
        for word_b in lines:
            similarity = SequenceMatcher(None, word_a, word_b).ratio()
            if similarity == 1:
                continue
            if similarity > similarity_max[0]:
                similarity_max = (similarity, word_a, word_b)

    print(similarity_max)

    _, word_a, word_b = similarity_max
    result = ""
    for i in range(len(word_a)):
        if word_a[i] == word_b[i]:
            result += word_a[i]
    print(result)
