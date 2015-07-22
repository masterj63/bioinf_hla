#qualities0 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
qualities0 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI"
qualities_map = {}
for i in range(len(qualities0)):
    qualities_map[qualities0[i]] = i


fastq = open('child10_S4_L001_R1_001.fastq', 'r')
fastq = fastq.readlines()

qual_sum = 0
qual_num = 0
distribution = [0 for i in qualities0]
i = 0
lengths = {}
while i < len(fastq):
    name = fastq[0 + i] # @name
    atgc = fastq[1 + i] # ATGC
    #name = fastq[2 + i] # plus
    qual = fastq[3 + i] #!@~{|}
    i += 4

    for c in qual.strip():
        j = qualities_map[c]
        qual_sum += j
        qual_num += 1
        distribution[j] += 1

    l = len(qual.strip())
    if l not in lengths:
        lengths[l] = 0
    lengths[l] += 1
    # if i > 4000:
    #     break

print(lengths)

print('num: {} ; sum: {};   avg: {}'.format(qual_num, qual_sum, qual_sum / qual_num))
for i in range(len(distribution)):
    #print('{}{}  '.format(distribution[i], qualities0[i]), end='')
    print(distribution[i])
    #print(qualities0[i]) ###
# i = 0
# for line in fastq:
#     if i >= 10:
#         break
#     i += 1
#     print(line)


# @name
# genome
# +
# quality