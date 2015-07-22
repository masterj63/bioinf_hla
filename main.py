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
while i < len(fastq_in):
    if i > 850:
        break

    name = fastq_in[0 + i].strip()  # @name
    atgc = fastq_in[1 + i].strip()  # ATGC
    # name = fastq[2 + i].strip() # plus
    quals = fastq_in[3 + i].strip()  # !@~{|}
    i += 4

    f_atgc, f_quals = filter_by_quality(atgc, quals)

    out_write(name)
    out_write(f_atgc)
    out_write('+')
    out_write(f_quals)

fastq_out.close()
