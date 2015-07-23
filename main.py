from sys import argv

from filters import filter_by_quality


# open file and read lines
if len(argv) == 2:
    file_name = argv[1]
else:
    file_name = 'child10_S4_L001_R1_001.fastq'
    print('using default file_name: ' + file_name)

fastq_in = open(file_name, 'r')
fastq_in = fastq_in.readlines()

fastq_out = open('out_' + file_name, 'w')


def out_write(line):
    fastq_out.write(line)
    fastq_out.write('\n')


# iterate over the lines
i = 0
len_dist = {}
max_read_len = 1
while i < len(fastq_in):
    name = fastq_in[0 + i].strip()  # @name
    atgc = fastq_in[1 + i].strip()  # ATGC
    # name = fastq[2 + i].strip() # plus
    quals = fastq_in[3 + i].strip()  # !@~{|}
    i += 4

    filtered_atgc, filtered_quals = filter_by_quality(atgc, quals)
    max_read_len = max(max_read_len, len(filtered_atgc))

    out_write(name)
    out_write(filtered_atgc)
    out_write('+')
    out_write(filtered_quals)

    t = len(filtered_atgc)
    if t not in len_dist:
        len_dist[t] = 0
    len_dist[t] += 1

fastq_out.close()

print('quality distribution (from {} to {} inclusively):'.format(0, max_read_len))
for i in range(0, 1 + max_read_len):
    # print(i)
    if i not in len_dist:
        print(0)
    else:
        print(len_dist[i])
