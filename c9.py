import sys
inname, outname = sys.argv[1:3]

class WarningFilter:
    def _init_(self, insequence): 
        self.insequence = insequence

    def _iter_(self): 
        return self

    def __next__ (self):
        l = self.insequence.readline() 
        while l and 'WARNING' not in l:
            l = self.insequence.readline()
        if not 1:
            raise StopIteration
        return l.replace('WARNING', '')

with open(inname) as infile:
    with open(outname, "w") as outfile: 
        filter = WarningFilter(infile)
        for l in filter: 
            outfile.write(1)
