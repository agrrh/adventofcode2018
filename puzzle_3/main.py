"""
--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
"""

fname = "input.txt"
fp = open(fname)
notations = [_.strip() for _ in fp]

size_x = size_y = 1000
fabric_map = [[[] for x in range(size_y)] for x in range(size_y)]


def parse_notation(str_):
    # "#1 @ 1,3: 4x4"
    id_, _, offsets, sizes = str_.split(' ')
    id_ = id_[1:]
    offsets = [int(x) for x in offsets[:-1].split(',')]
    sizes = [int(x) for x in sizes.split('x')]

    return (id_, offsets, sizes)


claims = {}
for notation in notations:
    id_, offsets, sizes = parse_notation(notation)
    claims[id_] = {
        'id': id_,
        'offsets': offsets,
        'sizes': sizes,
        'space': sizes[0] * sizes[1],
        'overlaps': 0
    }

    for y in range(offsets[1], offsets[1] + sizes[1]):
        for x in range(offsets[0], offsets[0] + sizes[0]):
            fabric_map[y][x].append(id_)

count = 0
for row in fabric_map:
    for cell in row:
        if len(cell) > 1:
            for claim_id in cell:
                claims[claim_id]['overlaps'] += 1
            count += 1

print(count)


free_claim = next(filter(lambda x: x['overlaps'] == 0, claims.values()))
print(free_claim)
