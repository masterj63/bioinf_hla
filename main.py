from filters import filter_by_quality

# open file and read lines
fastq_in = open('child10_S4_L001_R1_001.fastq', 'r')
fastq_in = fastq_in.readlines()

fastq_out = open('out_child10_S4_L001_R1_001.fastq', 'w')


def out_write(line):
    fastq_out.write(line)
    fastq_out.write('\n')


# iterate over the lines
i = 0
len_dist = {}
while i < len(fastq_in):
    # if i > 850:
    #     break

    name = fastq_in[0 + i].strip()  # @name
    atgc = fastq_in[1 + i].strip()  # ATGC
    # name = fastq[2 + i].strip() # plus
    quals = fastq_in[3 + i].strip()  # !@~{|}
    i += 4

    filtered_atgc, filtered_quals = filter_by_quality(atgc, quals)

    out_write(name)
    out_write(filtered_atgc)
    out_write('+')
    out_write(filtered_quals)

    t = len(filtered_atgc)
    if t not in len_dist:
        len_dist[t] = 0
    len_dist[t] += 1

fastq_out.close()

for i in range(0, 302):
    # print(i)
    if i not in len_dist:
        print(0)
    else:
        print(len_dist[i])
