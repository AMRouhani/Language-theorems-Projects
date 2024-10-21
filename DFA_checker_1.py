# Defalut Delta table

Delta_table = [['q0', 'q1', 'q3'], ['q1', 'q1', 'q2']
    , ['q2', 'q3', 'q4'], ['q3', 'q3', 'q4'], ['q4', 'q1', 'q2']]

#Number of alphabets
number_of_alphabet = 2

#list for changing stuts of states
AA = []
BB = [['q2', 'q4'], ['q0', 'q1', 'q3']]
CC = []
DD = []
BB_last_adder = []

#function that find connections in inner list of couple states
def index_2d_find(myList, v, inner_index="None"):
    for ih in range(len(myList)):
        if inner_index == "None":
            for x in range(len(myList[ih])):
                if v == myList[ih][x]:
                    return ih
        else:
            if v == myList[ih][int(inner_index)]:
                return ih

# function that check lists for being in true group list
def list_checker(list_2, list_3, list_4):
    EE = []
    SS = []
    FF = []
    WW = []
    print("list_2 is : ", list_2)
    print("list_3 is : ", list_3)
    print("list_4 is : ", list_4)
    checker_list_1 = list(dict.fromkeys(list_2))
    sorted(checker_list_1)
    print("checker list 1 :", checker_list_1)
    print("list_2 2 is : ", list_2)
    for mm in checker_list_1:
        for nn, jj, kk in zip(list_2, list_3, list_4):
            if mm == nn:
                EE.append(jj)
                SS.append(kk)
        FF.append(EE)
        WW.append(SS)
        EE.clear()
        SS.clear()
    return FF, WW

# def check lengh of input 
def lengh_checker(list_lengh):
    for qw in range(list_lengh):
        CC_adder, DD_adder = list_checker(AA[qw], CC[qw], DD[qw])
        print("CC_adder : ", CC_adder)
        print("DD_adder", DD_adder)
        if CC_adder != CC[qw]:
            del AA[qw]
            del CC[qw]
            del DD[qw]
            for val_insert_c in range(qw, qw + len(CC_adder)):
                rr_c = 0
                CC.insert(val_insert_c, CC_adder[rr_c])
                rr_c += 1
            for val_insert_d in range(qw, qw + len(DD_adder)):
                rr_d = 0
                DD.insert(val_insert_d, DD_adder[rr_d])
                rr_d += 1
            return "finish"
        else:
            del AA[qw]
            del CC[qw]
            del DD[qw]
    return "no_problem 1 "

#main function
def list_setting(list_1):
    print(" list 1 is : ", list_1)
    AB = []
    AC = []
    CC_index_val = []
    for kp in range(number_of_alphabet):
        for ko in list_1:
            print(" ko is : ", ko)
            vc = index_2d_find(Delta_table, ko, "0")
            CC_index_val.append(Delta_table[vc][0])
            print(" vc is : ", vc)
            aa = Delta_table[vc][kp + 1]
            AC.append(aa)
            bb = index_2d_find(BB, str(aa))
            AB.append(bb)
            print(" AB is : ", AB)
        print(" AB 2 is : ", AB)
        AA.append(AB)
        print("AA 1 is : ", AA)
        CC.append(AC)
        DD.append(CC_index_val)
        print(" AA 2 is : ", AA)
        AA_lengh_1 = len(AA)
        mode_check = lengh_checker(AA_lengh_1)
        if mode_check == "finish":
            break
        print(" AA 3 is : ", AA)
        AB.clear()
        AC.clear()
        CC_index_val.clear()
        print(" AA 4 is : ", AA)


# Runner function that get tables and do proccess
BB_lengh_1 = len(BB)
rt = 0
while rt < BB_lengh_1:
    print(" rt 1 is : ", rt)
    print("BB[rt] is : ", BB[rt])
    list_setting(BB[rt])
    if len(DD) != 0:
        del BB[rt]
        for val_insert_BB in range(rt, rt + len(DD)):
            rr_BB = 0
            BB.insert(val_insert_BB, DD[rr_BB])
            rr_BB += 1
    BB_lengh_2 = len(BB)
    rt += 1
    if BB_lengh_1 != BB_lengh_2:
        rt = 0
        BB_lengh_1 = BB_lengh_2

print("BB 2 is : ", BB)
