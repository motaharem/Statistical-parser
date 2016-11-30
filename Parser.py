import os

###################
def BackTrace(i,j,S,back,Grammer,NT,line):
    print i," ",j," ",S
    file = open(Subdir+'output.txt', 'a')
    temp = back[i][j][Key(S,NT)]
    if(temp==[]):
        file.write("(")
        file.write(" ")
        file.write(S)
        file.write(" ")
        file.write(line[j-1])
        file.write(" )")
        return
    file.write("(")
    file.write(" ")
    print S
    file.write(str(S))
    file.close()
    BackTrace(i,temp[0],NT[temp[1]],back,Grammer,NT,line)
    file = open(Subdir+'output.txt', 'a')
    file.write(" ")
    file.close()
    BackTrace(temp[0],j,NT[temp[2]],back,Grammer,NT,line)
    file = open(Subdir+'output.txt', 'a')
    file.write(")")
    file.close()

###################
def Key(A,NT):
    for i in range(len(NT)):
        if(NT[i]==A):
            return i
    return -1

###################
#grammerd
Grammer = []
NT = []
for subdir,dirs,files in os.walk('./'):
    for file in files:
        if(file=='Model.txt'):
            with open(subdir+file) as grammer:
                for line in grammer :
                    temp = []
                    this = line.split()
                    tag = True
                    for j in range(len(NT)):
                        #print this[0]
                        if(NT[j]==this[0]):
                            tag = False
                            break
                    if (tag == True):
                        NT.append(this[0])
                    for i in range(len(this)):
                        temp.append(this[i])
                    Grammer.append(this)
print NT

#parser
Subdir = ''
for subdir,dirs,files in os.walk('./'):
    Subdir = subdir
    for file in files:
        if(file=='input.txt'):
            with open(subdir+file) as imput:
                for linep in imput:
                    line = linep.split()
                    table = [[[0 for k in xrange(len(NT))] for j in xrange(len(line)+1)] for i in xrange(len(line)+1)]
                    #print table
                    back = [[[[] for k in xrange(len(NT))] for j in xrange(len(line)+1)] for i in xrange(len(line)+1)]
                    
                    for j in range(1,len(line)+1):
                        for rule in Grammer :
                            if(len(rule)==4 and rule[2]==line[j-1]):
                                table[j-1][j][Key(rule[0],NT)] = float(rule[3])
                                
                        X = j-2
                        #print "j",j
                        #print "0,j-1 :: ",0,j-1
                        for i in range(0,j-1):
                            #print "i ::",(X-i)+1,j
                            for k in range((X-i)+1,j):
                                #print "k : ",k
                                for rule in Grammer:
                                    #print rule
                                    if(len(rule)==5):
                                        A = rule[0]
                                        B = rule[2]
                                        C = rule[3]
                                        p = float(rule[4])
                                        #print rule
                                        #print "table[X-i+1][k][Key(B,NT)] ","table[k][j][Key(C,NT)]"
                                        #print table[X-i][k][Key(B,NT)],table[k][j][Key(C,NT)]
                                        if(table[X-i][k][Key(B,NT)] > 0) and (table[k][j][Key(C,NT)] > 0):
                                            #print "inja chi ?"
                                            if(table[X-i][j][Key(A,NT)]<p*table[X-i][k][Key(B,NT)]*table[k][j][Key(C,NT)]):
                                                table[X-i][j][Key(A,NT)] = p*table[X-i][k][Key(B,NT)]*table[k][j][Key(C,NT)]
                                                #print "OK"
                                                #print "---",k,Key(B,NT),Key(C,NT)
                                                back[X-i][j][Key(A,NT)] = [k,Key(B,NT),Key(C,NT)]
                                                #print back[X-i][j][Key(A,NT)]

                    print NT
                    #for i in range(len(table)):
                        #for j in range(len(table[0])):
                            #print table[i][j]
                    for i in range(len(back)):
                        for j in range(len(back[i])):
                            print back[i][j]
                    BackTrace(0,len(line),"S",back,Grammer,NT,line)
