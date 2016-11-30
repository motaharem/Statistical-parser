import os

def rule_exist(rules,rules_count,extend,totalrulecount):
    extendR =[]
    for i in range(len(extend)):
        extendR.append(extend[i])
    print len(rules)
    L = len(extendR)
    for i in range(len(rules)):
        #print "rule[i]", rules[i]
        tag = True
        if (len(rules[i])==L):
            for j in range(L):
                #print "check ",rules[i][j],extendR[L-j-1]
                if(rules[i][j]!=extendR[L-1-j]):
                    tag = False
            if(tag==True):
                print "%",rules[i]
                rules_count[i] = rules_count[i] + 1
                totalrulecount = totalrulecount + 1
                return True,totalrulecount,rules[i][0]
    return False,totalrulecount,""

#############
#read from a file

rules = []
rules_count = []
totalrulecount = 0

for subdir,dirs,files in os.walk('./'):
    for file in files:
        if(file=='new train.txt'):
            with open(subdir+file) as train_data:
                for line in train_data:
                    line = line.replace("("," ( ").replace(")"," ) ").split()
                    stack = []
                    for i in range(len(line)):
                        #print "stack= ",stack
                        if (line[i]!=")"):
                            stack.append(line[i])
                            print "stack ",stack 
                        else:
                            tag = False
                            extend = []
                            while(tag == False):
                                temp = stack.pop()
                                #print "temp ",temp
                                if(temp != '('):
                                    extend.append(temp)
                                else :
                                    tag = True
                                    if (len(extend)==1):
                                        a= extend.pop()
                                    print "extend1",extend
                                    if (len(extend)!=0):
                                        print "extend2",extend
                                        f = rule_exist(rules, rules_count, extend, totalrulecount)
                                        print "f",f
                                        totalrulecount = f[1]
                                        if(f[2]!=""):
                                            stack.append(f[2])
                                        if((not f[0]) and len(extend)>1):
                                            this_rule = []
                                            for j in range(len(extend)):
                                                this_rule.append(extend.pop())
                                            if(len(this_rule)>0):
                                                stack.append(this_rule[0])
                                            print "stack",stack
                                            rules.append(this_rule)
                                            rules_count.append(1)
                                            totalrulecount = totalrulecount + 1
                                            file1 = open(subdir+'model.txt', 'a')
                                            for j in range(len(this_rule)):
                                                if (j==0):
                                                    #print "ONE"
                                                    file1.write(this_rule[j])
                                                    file1.write(" -> ")
                                                else:
                                                    #print "OTHERS"
                                                    file1.write(this_rule[j])
                                                    file1.write(" ")
                                                if (j==len(this_rule)-1):
                                                    #print "END"
                                                    file1.write("\n")
                                                #file.write(str(rules_count[i]))
                                                #file.write(" ")
                                                #file.write(str(totalrulecount))
                                                #file.write(" ")
                                                #probability = float(rules_count[i])/float(totalrulecount )
                                                #file1.write(str(probability))
                                                #file1.write("\n")

                
                            #print "result",rules
###############
#write in a file
file1 = open(subdir+'model.txt', 'a')
probability = 0
for i in range(len(rules)):
    for j in range(len(rules[i])):
        if (j==0):
            #print "ONE"
            file1.write(rules[i][j])
            file1.write(" -> ")
        else:
            #print "OTHERS"
            file1.write(rules[i][j])
            file1.write(" ")
        if (j==len(rules[i])-1):
            #print "END"
            file1.write(" ")
            #file.write(str(rules_count[i]))
            #file.write(" ")
            #file.write(str(totalrulecount))
            #file.write(" ")
            probability = float(rules_count[i])/float(totalrulecount )
            file1.write(str(probability))
            file1.write("\n")
