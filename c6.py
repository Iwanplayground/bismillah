import sys
import warnings
inname = sys.argv[1]
outname = sys.argv[2]
with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)

with open(outname) as ofile:
    for i in ofile:
        print(i) 
        