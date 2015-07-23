from sys import argv

from filters import filter_is_too_short

file_name = argv[1]
file_in = open(file_name, 'r')
file_out = open('out_' + file_name, 'w')
fastq_in = file_in.readlines()


def out_write(line):
    file_out.write(line)
    file_out.write('\n')


i = 0
reads_total = 0
reads_cut_off = 0
while i < len(fastq_in):
    reads_total += 1
    name = fastq_in[0 + i].strip()  # @name
    atgc = fastq_in[1 + i].strip()  # ATGC
    # name = fastq[2 + i].strip() # plus
    quals = fastq_in[3 + i].strip()  # !@~{|}
    i += 4

    if not filter_is_too_short(atgc):
        out_write(name)
        out_write(atgc)
        out_write('+')
        out_write(quals)
    else:
        reads_cut_off += 1

file_in.close()
file_out.close()

print('reads total: {}'.format(reads_total))
print('reads cut off: {} ({}%)'.format(reads_cut_off, reads_cut_off / reads_total))
