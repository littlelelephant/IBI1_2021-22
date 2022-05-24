import pandas as pd
DLX5_mouse = 'MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY'
DLX5_human = 'MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY'
RandomSeq  = 'GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP'
BLOSUM = pd.read_excel(r'C:\Users\OMEN\IBI1_2021-22\BLOSUM.xlsx')
 #imput the sequence of mouse, human, random sequence and BLOSUM matrix
seq="ARNDCQEGHILKMFPSTWYVBZX"
def cal_score(DLX5_human,DLX5_mouse):
    seq_1 = list(DLX5_human) #change the protein sequence to a list
    seq_2 = list(DLX5_mouse)
    i=0
    sum=0
    for i in range (0,len(seq_1)):
        a=seq.find(seq_1[i])
        b=seq.find(seq_2[i])
        i=i+1
        score = BLOSUM.iloc[a,b+1]
        sum=sum+score
    return sum
print('score1 =',cal_score(DLX5_human,DLX5_mouse))
print('score2 =',cal_score(DLX5_human,RandomSeq))
print('score3 =',cal_score(DLX5_mouse,RandomSeq))
def aliment(seq1,seq2): 
    edit_distance=0
    for i in range(0,len(seq1)):
        if seq1[i]!=seq2[i]:
            edit_distance+=1
    return edit_distance
print('distance =',aliment(DLX5_human,DLX5_mouse),'rate =',1-aliment(DLX5_human,DLX5_mouse)/len(DLX5_human))
print('distance =',aliment(DLX5_human,RandomSeq),'rate =',1-aliment(DLX5_human,RandomSeq)/len(DLX5_human))
print('distance =',aliment(DLX5_mouse,RandomSeq),'rate =',1-aliment(DLX5_mouse,RandomSeq)/len(DLX5_human))
#From the progamme above, we can found that
#The BLOSUM score between human and mouse is 1490.
#The similarities of amino acids between the human sample and the mouse sample is 96.54%.
#The similarities of amino acids between the mouse sample and the random sample is 3.11%.
#The similarities of amino acids between the random sample and the human sample is 2.77%.
#What I found was that the amino acid sequences in humans and mice were very different from the random sequences but they were very similar.