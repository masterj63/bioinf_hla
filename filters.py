from functools import reduce

from fastq_format import symb_num_qualities_map, num_symb_qualities_map

WINDOW_SIZE = 15
LOW_QUAL_VALUE = 20
BAD_WINDOW_CRITERION = 10


## Cuts off 'bad' preffix and suffix from genome `atgc`.
def filter_by_quality(atgc, quals):
    quals = list(map(lambda c: symb_num_qualities_map[c], quals))

    # -->
    count = initialize_window(quals, from_left=True)
    cut_start_pos = 0
    while count_low_quals(count) >= BAD_WINDOW_CRITERION:
        count = step_window(quals, count, cut_start_pos, move_right=True)
        if not count:
            break
        cut_start_pos += 1

    quals = quals[cut_start_pos:]
    atgc = atgc[cut_start_pos:]

    # <--
    count = initialize_window(quals, from_left=False)
    cut_end_pos = len(quals)
    curr_off = len(quals) - WINDOW_SIZE
    while count_low_quals(count) >= BAD_WINDOW_CRITERION:
        count = step_window(quals, count, curr_off, move_right=False)
        if not count:
            break
        cut_end_pos -= 1
        curr_off -= 1

    atgc = atgc[:cut_end_pos]

    quals = quals[:cut_end_pos]
    quals = map(lambda x: num_symb_qualities_map[x], quals)
    quals = list(quals)
    quals = reduce(lambda x, y: x + y, quals, '')

    return (atgc, quals)


def filter_by_length(atgc):
    # TODO
    return atgc


### PRIVATE ROUTINES

def count_low_quals(count):
    res = 0
    for kv in count.items():
        k, v = kv
        if k <= LOW_QUAL_VALUE:
            res += v
    return res


## Initializes window, places it at the beginning or end of genome `atgc`.
def initialize_window(atgc, from_left):
    res = {}
    if from_left:
        for c in atgc[:WINDOW_SIZE]:
            if c not in res:
                res[c] = 0
            res[c] += 1
    else:
        offset = len(atgc) - WINDOW_SIZE
        for c in atgc[offset:]:
            if c not in res:
                res[c] = 0
            res[c] += 1
    return res


## Moves window one position left or right, returns `None` if impossible.
def step_window(atgc, current_count, current_offset, move_right):
    if move_right:
        return step_window_right(atgc, current_count, current_offset)
    else:
        return step_window_left(atgc, current_count, current_offset)


## Moves window one position right, returns `None` if impossible.
def step_window_right(quals, current_count, current_offset):
    if len(quals) >= current_offset + WINDOW_SIZE:
        return None

    outcoming = quals[current_offset]
    current_count[outcoming] -= 1
    if current_count[outcoming] == 0:
        current_count.pop(outcoming, None)

    incoming = quals[WINDOW_SIZE + current_offset]
    if incoming not in current_count:
        current_count[incoming] = 0
    current_count[incoming] += 1

    current_offset += 1
    return current_count


## Moves window one position left, returns `None` if impossible.
def step_window_left(quals, current_count, current_offset):
    if current_offset < WINDOW_SIZE:
        return None

    outcoming = quals[current_offset + WINDOW_SIZE - 1]
    current_count[outcoming] -= 1
    if current_count[outcoming] == 0:
        current_count.pop(outcoming, None)

    incoming = quals[current_offset - 1]
    if incoming not in current_count:
        current_count[incoming] = 0
    current_count[incoming] += 1

    current_offset -= 1
    return current_count
