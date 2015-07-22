qualities_line = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI"

symb_num_qualities_map = {}
for i in range(len(qualities_line)):
    symb_num_qualities_map[qualities_line[i]] = i

num_symb_qualities_map = {}
for (k, v) in symb_num_qualities_map.items():
    num_symb_qualities_map[v] = k
