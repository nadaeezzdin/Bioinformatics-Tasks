"""
1- Edit ReadFastq() function to make it read genomic data from FASTA file.
2- Define a QToPhred33() function that takes a quality score as a parameter and returns its equivalent ASCII symbol
"""

def ReadFast(FileNameFast):
    Seq=[]
    with open(FileNameFast)as Fo:
        while Ture:
            Fo.readline()
            Sequance=Fo.readline()
            if len(Sequance==0):
                break
            Seq.append(Sequance)
    return Seq
Sequances=ReadFast("sample.fast")
print(Sequances[:4])


def Phred33ToQ(qualValue):
    return ord(qualValue)-33

print(Phred33ToQ('H'))