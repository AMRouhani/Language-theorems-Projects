# input part of user
print("This program make DFAs minimize")
alpha_bet = []
number_of_alphabet = 0
states = []
number_of_states = 0
final_states = []

a = "start"
while "finish" not in a:
    a = input("please enter your alphabet : ")
    print(" if you finished your work enter \" finish \" ")
    if "finish" in a:
        break
    alpha_bet.append(a)

# get alohabets info
number_of_alphabet = len(alpha_bet)
print("number_of_alphabet : ", number_of_alphabet)
print("alpha_bet : ", alpha_bet)

#get states info
s = int(input(" please enter your number of states : "))
for i in range(s):
    states.append("q" + str(i))

number_of_states = len(states)

#print situation to until now
print("number_of_states : ", number_of_states)
print(" states are : ", states)

# get final states from user
f = "start"
while "finish" not in f:
    f = input("please enter your final states just number without space: ")
    print(" if you finished your work enter \" finish \" ")
    if "finish" in f:
        break
    final_states.append("q" + f)

print(" final states are : ", final_states)

# make list of tables and their edge
def array_maker(m, n):
    A = []
    for kk in range(m):
        v = []
        for k in range(n):
            if k == 0:
                x = states[kk]
                v.append(x)
            else:
                y = input("Please enter your state \""
                          + states[kk] + "\" that use \" "
                          + alpha_bet[k - 1] + "\" transition  to go : ")
                v.append(y)
        A.append(v)
    return A

# create Delta table
Delta_table = array_maker(number_of_states, number_of_alphabet + 1)

print("Delta_table : ", Delta_table, end="\n")

reachable_state_checking = []

p = 0

# this function check if every state is in right group or not
def reach_state_check(Q):
    global p
    state_index = states.index(Q)
    if Q not in reachable_state_checking:
        reachable_state_checking.append(Q)
        for i_1 in range(1, number_of_alphabet + 1, 1):
            p = Delta_table[state_index][i_1]
            if p not in reachable_state_checking:
                reach_state_check(p)


# chacke right stats groups and sort them
reach_state_check("q0")
sorted(reachable_state_checking)
print("reachable_state_checking : ", reachable_state_checking)

Delta_table_lengh = len(Delta_table)

#clean and control Delta table status
zz = 0
while zz < Delta_table_lengh:
    if Delta_table[zz][0] not in reachable_state_checking:
        del Delta_table[zz]
        z = 0
        Delta_table_lengh = len(Delta_table)
    else:
        zz += 1

print("Delta _ table is : ", Delta_table)

#check final stasts and clean it
for zz in final_states:
    if zz not in reachable_state_checking:
        final_states.remove(zz)

# create unfinal states and fill it table
unfinal_states = []
for ll in range(len(Delta_table)):
    if Delta_table[ll][0] not in final_states:
        unfinal_states.append(Delta_table[ll][0])

# esential list
AA = []
BB = []
CC = []
DD = []
BB_last_adder = []
BB.append(unfinal_states)
BB.append(final_states)

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
    checker_list_1 = list(dict.fromkeys(list_2))
    sorted(checker_list_1)
    if len(checker_list_1) > 1:
        for mm in checker_list_1:
            for nn, jj, kk in zip(list_2, list_3, list_4):
                if mm == nn:
                    EE.append(jj)
                    SS.append(kk)
            FF.append(EE.copy())
            WW.append(SS.copy())
            EE.clear()
            SS.clear()
        return FF, WW
    else:
        FF.append(list_3)
        WW.append(list_4)
        return FF, WW

# def check lengh of input 
def lengh_checker(list_lengh):
    for qw in range(list_lengh):
        CC_adder, DD_adder = list_checker(AA[qw], CC[qw], DD[qw])
        if CC_adder[0] != CC[qw]:
            del AA[qw]
            del CC[qw]
            del DD[qw]
            CC_repeat = []
            for val_insert_c in range(len(CC_adder)):
                CC_repeat.append(CC_adder[val_insert_c].copy())
            CC.extend(CC_repeat.copy())
            DD_repeat = []
            for val_insert_d in range(len(DD_adder)):
                DD_repeat.append(DD_adder[val_insert_d].copy())
            DD.extend(DD_repeat.copy())
            return "finish"
        else:
            del AA[qw]
            del CC[qw]
            del DD[qw]
    return "no_problem 1 "

# fil groups of states
def list_setting(list_1):
    AB = []
    AC = []
    CC_index_val = []
    for kp in range(number_of_alphabet):
        for ko in list_1:
            vc = index_2d_find(Delta_table, ko, "0")
            CC_index_val.append(Delta_table[vc][0])
            aa = Delta_table[vc][kp + 1]
            AC.append(aa)
            bb = index_2d_find(BB, str(aa))
            AB.append(bb)
        AA.append(AB.copy())
        CC.append(AC.copy())
        DD.append(CC_index_val.copy())
        AA_lengh_1 = len(AA)
        mode_check = lengh_checker(AA_lengh_1)
        if mode_check == "finish":
            break
        AB.clear()
        AC.clear()
        CC_index_val.clear()

# run time part of program
BB_lengh_1 = len(BB)
rt = 0
while rt < BB_lengh_1:
    if len(BB[rt]) > 1:
        list_setting(BB[rt])
    if len(DD) != 0:
        del BB[rt]
        BB.extend(DD.copy())
        DD.clear()
    BB_lengh_2 = len(BB)
    rt += 1
    if BB_lengh_1 != BB_lengh_2:
        rt = 0
        BB_lengh_1 = BB_lengh_2

print("T is : ", BB)
