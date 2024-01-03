import enchant, copy
dict = enchant.Dict("en_US")
word = ['D','E','A','D']
valid = dict.check("".join(word))
cards = [['A','G'],['T','F'],['P','E'],['S','J'],['S','N'],['T','R']]#,['M','V'],['K','Z'],['C','B'],['A','L'],['B','U'],['H','A'],['A','T']]

def is_valid_move(current,pos,letter):
    if current[pos] == letter:
        return False
    else:
        temp = copy.deepcopy(current)
        temp[pos] = letter
#        print(temp," ", dict.check("".join(temp)))
        return dict.check("".join(temp))

def placeWord(remain,current):
    maxseqlen = 0
    bestmove = []
    if remain == []:
        return None, 0
    for i in range(len(remain)):
        for j in range(2):
            for k in range(4):
                moves=[]
                seqlen = 0
                if is_valid_move(current,k,remain[i][j]):
                    temp = copy.deepcopy(current)
                    temp[k] = remain[i][j]
                    temp2 = copy.deepcopy(remain)
                    temp2.pop(i)
                    moves.append((k,remain[i],remain[i][j]))
                    moves.append(placeWord(temp2, temp)[0])
                    seqlen+=placeWord(temp2, temp)[1]+1
                if seqlen>maxseqlen:
                    bestmove = copy.deepcopy(moves)
                    maxseqlen=seqlen
    return bestmove, maxseqlen


                
#print(placeWord(cards,word))