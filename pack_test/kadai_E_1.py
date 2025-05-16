# %%


def kadai_E_1(pdb_seqres, number):
    import re
    import urllib.request

    from Bio import SeqIO

    allrecords = 0
    with open(pdb_seqres, "rt") as handle:
        for record in handle:
            if ">" in record:
                allrecords = allrecords + 1
            else:
                allrecords = allrecords + 0

    count = 0

    with open(pdb_seqres, "rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            desc_part = record.description
            A = desc_part.split()
            B = A[2]
            C = B.split(":")
            D = C[1]
            if int(D) <= number:
                count = count + 1

    print(count)

    print(count / allrecords * 100)


# %%
