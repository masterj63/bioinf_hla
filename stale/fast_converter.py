# fastq to fasta
import sys

filein_name = sys.argv[1]
filein = open(filein_name, 'r')

fileout_name = sys.argv[2]
fileout = open(fileout_name, 'w')

lines = filein.readlines()
i = 0
while 4 + i <= len(lines):
    name = lines[i]
    atgc = lines[1 + i]

    fileout.write('>' + name[1:])
    fileout.write(atgc)

    i += 4
