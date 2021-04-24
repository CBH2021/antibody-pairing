import anarci
import numpy as np
import pandas as pd


def align_abs(Hchain, Lchain):
    """
    Creates antibody alignments using the ANARCI numbering scheme.
    """
    
    anarci_out = anarci.run_anarci(Hchain.reset_index().values.tolist(), ncpu=1, scheme='imgt')
    hseqs = create_alignment(anarci_out, cdr3_len_cut=12)

    lanarci_out = anarci.run_anarci(Lchain.reset_index().values.tolist(), ncpu=1, scheme='imgt')
    lseqs = create_alignment(lanarci_out, cdr3_len_cut=12)

    return pd.DataFrame(zip(hseqs, lseqs), columns=['Hchain_align', 'Lchain_align'])

    
    
def create_alignment(anarci_out, cdr3_len_cut=12):
    aln_seqs = []

    for seq in anarci_out[1]:
        
        if seq == None:
            aln_seqs.append('no seq')
            continue
        
        aln_seq = []
        extra111 = []
        extra112 = []

        for res in seq[0][0]:

            if res[0][1] == ' ': aln_seq.append(res[1])
            elif res[0][0] == 111: extra111.append(res[1])
            elif res[0][0] == 112: extra112.append(res[1])
            else: pass #print(res)


        while len(aln_seq) < 128: aln_seq = aln_seq + ['-']
                
        if len(extra111 + extra112) > cdr3_len_cut: 
            aln_seqs.append(''.join(['-']*(128+cdr3_len_cut)))
            continue

        while len(extra112) < cdr3_len_cut//2: extra112 = ['-'] + extra112
        while len(extra111) < cdr3_len_cut//2: extra111 = extra111 + ['-']

        extra112.reverse()
        extra111.reverse()

        [aln_seq.insert(112-1, resi) for resi in extra112]
        [aln_seq.insert(112-1, resi) for resi in extra111]    

        aln_seqs.append(''.join(aln_seq))
    
    return np.array(aln_seqs)


def one_hot_encode(Hchain, Lchain):
    """
    Encodes the sequences with one-hot encoding
    """
    
    encode_dic = get_encoding('src/one-hot.txt')
    
    one_hot_heavy = Hchain.apply(lambda x: appl_encoding(x, encode_dic))
    one_hot_light = Lchain.apply(lambda x: appl_encoding(x, encode_dic))
    return pd.concat([one_hot_heavy, one_hot_light], axis=1)
    
    
def get_encoding(Embedding_file):
    embedding_dic = {}
    with open(Embedding_file, 'r') as f:
        for line in f:
            if not line.startswith('#'):
                line = line.split()
                embedding_dic[line[0]] = [float(i) for i in line[1:]]
                
    return embedding_dic


def appl_encoding(seq, embed_dic):
    """
    Applies the score on a sequence based on embedding
    """
    residf = pd.DataFrame(list(seq), columns=['res'])
    
    features = np.concatenate(residf.apply(lambda x: np.array(embed_dic[x.res]), axis=1).values)
    
    return pd.Series(features)

