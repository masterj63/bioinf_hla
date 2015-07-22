# open file and read lines
my_fastq = open('child10_S4_L001_R1_001.fastq', 'r')
my_fastq = my_fastq.readlines()

from fastq_format import qualities_map

# iterate over the lines
delim = '=' * 20
i = 0
j = 0
while i < len(my_fastq):
    if i > 850:
        break

    name = my_fastq[0 + i]  # @name
    atgc = my_fastq[1 + i]  # ATGC
    # name = fastq[2 + i] # plus
    qual = my_fastq[3 + i]  # !@~{|}
    i += 4

    good = True
    for q in qual[:20]:
        q = qualities_map[q]
        if q < 34:
            good = False
            break

    if not good:
        continue
    # print(i // 4, end=' ')
    print(i, end=' ')
    j += 1
    if j == 20:
        print()
        j = 0
