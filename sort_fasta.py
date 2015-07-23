from sys import argv

file_name_in = argv[1]
file_name_out = argv[2]

fasta_out = open(file_name_out, 'w')
fasta_in = open(file_name_in, 'r')

lines = fasta_in.readlines()

name = lines[0].strip()
pairs = []
i = 1
while i < len(lines):
    atgc = ''
    while i < len(lines):
        last_line = lines[i]
        i += 1
        if last_line[0] == '>':
            pair = (name, atgc)
            pairs.append(pair)
            name = last_line
            break
        atgc += last_line

pair = (name, atgc)
pairs.append(pair)

pairs.sort(key=lambda x: x[0])

for (p0, p1) in pairs:
    fasta_out.write(p0.strip())
    fasta_out.write('\n')
    fasta_out.write(p1.strip())
    fasta_out.write('\n')
