from sys import argv


def extract_keyword(name):
    kw_from, kw_to = '>HLA', '*'
    if (kw_from not in name) or (kw_to not in name):
        return 'trash'
    i = name.index(kw_from) + len(kw_from)
    j = name.index(kw_to)
    if i > j:
        return 'trash'
    return name[i:j]


file_name_in = argv[1]

fasta_in = open(file_name_in, 'r')

lines = fasta_in.readlines()

name = lines[0].strip()
pairs = []
keywords = set()
i = 1
while i < len(lines):
    atgc = ''
    while i < len(lines):
        last_line = lines[i]
        i += 1
        if last_line[0] == '>':
            kw = extract_keyword(name)
            file_out_name = 'class_' + kw + '_' + file_name_in
            if kw not in keywords:
                keywords.add(kw)
                with open(file_out_name, 'w') as _:
                    pass  # create/erase file
            with open(file_out_name, 'a') as fasta_out:
                fasta_out.write(name.strip())
                fasta_out.write('\n')
                fasta_out.write(atgc.strip())
                fasta_out.write('\n')

            pair = (name, atgc)
            pairs.append(pair)
            name = last_line
            break
        atgc += last_line

kw = extract_keyword(name)
file_out_name = 'class_' + kw + '_' + file_name_in
if kw not in keywords:
    keywords.add(kw)
    with open(file_out_name, 'w') as _:
        pass  # create/erase file
with open(file_out_name, 'a') as fasta_out:
    fasta_out.write(name.strip())
    fasta_out.write('\n')
    fasta_out.write(atgc.strip())
    fasta_out.write('\n')
