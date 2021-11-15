import threading
import time
import random
import socket
import matplotlib.pyplot as plt
import numpy as np
import math
import numpy.ma as ma
import itertools
import sys
import imageio


# In order to show the operation of each step, the figure larger than 10*10 will be very slow
def create_gif(image_list, gif_name, duration):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    n=0
    f=imageio.imread(image_list[-1])
    while n<20:
        frames.append(f)
        n=n+1
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def maze(d, minenumb):   # Generate minesweeper matrix
    m = np.random.binomial(1, 0, size=(d, d))
    random_list = list(itertools.product(range(0, d), range(0, d)))
    minelist = random.sample(random_list, minenumb)
    # print(minelist)
    while minelist:
        rr, cc = minelist.pop()
        m[rr, cc] = -1
    # print(minelist)

    i = 0
    while i < d:
        j = 0
        while j < d:
            if m[i, j] == 1:
                m[i, j] = -1
            j = j + 1
        i = i + 1

    i = 0
    while i < d:
        j = 0
        while j < d:
            if m[i, j] == 0:
                # 四角
                k = 0
                if i == 0 and j == 0:
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k
                if i == 0 and j == d - 1:
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i == d - 1 and j == d - 1:
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i == d - 1 and j == 0:
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k
                # 除四角的四边
                if i == 0 and j != 0 and j != d - 1:
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i != 0 and i != d - 1 and j == 0:
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i == d - 1 and j != 0 and j != d - 1:
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i != 0 and i != d - 1 and j == d - 1:
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k

                if i != 0 and i != d - 1 and j != 0 and j != d - 1:
                    if m[i - 1, j] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i - 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j - 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j + 1] == -1:
                        k = k + 1
                        pass
                    if m[i + 1, j] == -1:
                        k = k + 1
                        pass
                    m[i, j] = k
            j = j + 1
        i = i + 1

    # plt.matshow(m, cmap=plt.cm.gray)
    # plt.show()
    return m


# Determine the location of the grid
def judge(r, c):
    if r == 0 and c == 0:  # Upper left
        p = [[0, 1], [1, 1], [1, 0]]
    elif r == d - 1 and c == 0:  # Bottom left
        p = [[d - 2, 0], [d - 2, 1], [d - 1, 1]]
    elif r == 0 and c == d - 1:  # Upper right
        p = [[0, d - 2], [1, d - 2], [1, d - 1]]
    elif r == d - 1 and c == d - 1:  # Bottom right
        p = [[d - 1, d - 2], [d - 2, d - 2], [d - 2, d - 1]]
    elif r == 0:  # Upper
        p = [[0, c + 1], [0, c - 1], [1, c + 1], [1, c - 1], [1, c]]
    elif r == d - 1:  # Bottom
        p = [[d - 1, c + 1], [d - 1, c - 1], [d - 2, c + 1], [d - 2, c - 1], [d - 2, c]]
    elif c == 0:  # left
        p = [[r + 1, 0], [r - 1, 0], [r + 1, 1], [r - 1, 1], [r, 1]]
    elif c == d - 1:  # right
        p = [[r + 1, d - 1], [r - 1, d - 1], [r + 1, d - 2], [r - 1, d - 2], [r, d - 2]]
    else:  # normal
        p = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1], [r + 1, c + 1], [r - 1, c + 1], [r + 1, c - 1],
             [r - 1, c - 1]]
    return p


def udlr(mzopen, index):
    x, y = index[0], index[1]
    l = []
    if x > 0:
        l.append([x - 1, y])
    if y > 0:
        l.append([x, y - 1])
    if x < len(mzopen) - 1:
        l.append([x + 1, y])
    if y < len(mzopen) - 1:
        l.append([x, y + 1])
    return l


# 2.2 partone
def improved_agent(mzopen, mzanswer):
    for i in range(len(mzopen)):
        for j in range(len(mzopen[0])):
            if mzopen[i, j] < 0 or mzopen[i, j] > 8: continue
            around = udlr(mzopen, [i, j])
            space = []  # The remaining grids around the target
            number = []
            while around:  # Judging around
                cell = around.pop(0)
                rr, cc = cell
                if mzopen[rr, cc] == 9:
                    space.append([rr, cc])  # Get what is not open around the target
                if 0 <= mzopen[rr, cc] < 9:
                    number.append([rr, cc])
            if len(space) != 0 and len(number) != 0:
                n = len(number)
                while n > 0:
                    n = n - 1
                    g1 = number.pop(0)
                    mzopen = logic_decide(mzopen, mzanswer, g1, [i, j])
    return mzopen


# TODO: Assume the value of g1 is always larger or equal than that of g2. in mzopen, 9 is undecided, -1 represents
#  mines, and -2 represents flags for mines.
#  t1, t2:total grids around g1 and g2; type: list
#  a1, a2, ac: unknown area of only around g1, g2, and common area; type: list
#  m1, m2, mc: mines only in a1, a2, or common area; type: int
#  s1, s2: suspected mines in corresponding unknown areas; type: int
def logic_decide(mzopen, mzanswer, g1, g2):
    global addFlags
    global addNums
    t1 = judge(g1[0], g1[1])
    t2 = judge(g2[0], g2[1])
    tc = [val for val in t1 if val in t2]
    a1, a2 = find_nine(mzopen, t1), find_nine(mzopen, t2)
    if len(a1) > len(a2) or mzopen[g1[0], g1[1]] > mzopen[g2[0], g2[1]]:
        temp = list.copy(g1)
        g1 = list.copy(g2)
        g2 = list.copy(temp)
        temp = list.copy(t1)
        t1 = list.copy(t2)
        t2 = list.copy(temp)
        temp = list.copy(a1)
        a1 = list.copy(a2)
        a2 = list.copy(temp)
    if a1 == a2:
        return mzopen
    ac = [val for val in a1 if val in a2]
    if len(ac) < 2:
        return mzopen
    temp1 = list.copy(a1)
    temp2 = list.copy(a2)
    for i in range(len(a1)):
        for j in range(len(ac)):
            if a1[i] == ac[j]:
                temp1.remove(ac[j])
    for i in range(len(a2)):
        for j in range(len(ac)):
            if a2[i] == ac[j]:
                temp2.remove(ac[j])
    a1 = list.copy(temp1)
    a2 = list.copy(temp2)
    m1, m2, mc = find_negative(mzopen, t1), find_negative(mzopen, t2), find_negative(mzopen, tc)
    s1 = mzopen[g1[0], g1[1]] - mc - m1
    s2 = mzopen[g2[0], g2[1]] - mc - m2
    difference = [item for item in a2 if not item in a1]
    if s1 == s2 and len(a1) == 0:
        for each in difference:
            mzopen[each[0], each[1]] = mzanswer[each[0], each[1]]
            print(each[0], each[1], "open", mzanswer[each[0], each[1]])
            addNums.append(each)
    if s2 - s1 == len(difference):
        for each in difference:
            mzopen[each[0], each[1]] = -2
            mzopen = logic_decide(mzopen, mzanswer, g1, g2)
            print(each[0], each[1], "mark")
            addFlags.append(each)
    return mzopen


def find_nine(mzopen, lst):
    l = []
    for each in lst:
        if mzopen[each[0], each[1]] == 9:
            l.append(each)
    return l  # list of not open grid


def find_negative(mzopen, lst):
    l = []
    for each in lst:
        if mzopen[each[0], each[1]] < 0:
            l.append(each)
    return len(l)  # mines


def zhoubian(i,j,d):
    if i==0 and j==0:
        return[(i,j+1),(i+1,j+1),(i+1,j)]
    if i==0 and j==d-1:
        return[(i,j-1),(i+1,j-1),(i+1,j)]
    if i==d-1 and j==d-1:
        return[(i,j-1),(i-1,j-1),(i-1,j)]
    if i==d-1 and j==0:
        return[(i,j+1),(i-1,j+1),(i-1,j)]
    if i==0 and j!=0 and j!=d-1:
        return[(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]

    if i!=0 and i!=d-1 and j==0:
        return[(i-1,j),(i+1,j+1),(i-1,j+1),(i,j+1),(i+1,j)]

    if i==d-1 and j!=0 and j!=d-1:
        return[(i-1,j),(i-1,j+1),(i-1,j-1),(i,j+1),(i,j-1)]
    if i!=0 and i!=d-1 and j==d-1:
        return[(i-1,j-1),(i+1,j-1),(i,j-1),(i+1,j),(i-1,j)]

    if i!=0 and i!=d-1 and j!=0 and j!=d-1:
        return[(i-1,j),(i-1,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j),(i+1,j-1),(i+1,j+1)]


def issubset(li1,li2):
    count=0
    fat=[]
    for zb1 in li1:
        if zb1 not in li2:
            return False, fat
    for zb2 in li2:
        if zb2 not in li1:
            fat.append(zb2)
    return True,fat


def takelast(elem):
    return elem[-1]


def mazeopenTopose(mazeopen,d):
    poss={}
    i=0
    while i<d:
        j=0
        while j<d:
            poss[(i,j)]=mazeopen[i,j]
            j=j+1
            pass
        pass
        i=i+1
    pos=poss.copy()
    return pos

# 2.2 parttwo
def imporveAgent(poss,d,leishu):
    faa=[]
    for n in poss.keys():
        if poss[n]!=9 and poss[n]!=-1 and poss[n]!=-2:
            i,j=n
            zbia=zhoubian(i,j,d)
            count=0
            bom=0
            fan=[]
            for k in zbia:
                if poss[k]!=9:
                    if poss[k]==-1 or poss[k]==-2:
                        bom=bom+1
                        pass
                    else:
                        count=count+1
                else:
                    fan.append(k)
                pass
            if len(fan)!=0:
                fan.append(poss[n]-bom)
                faa.append(fan)
            pass

    for lis in faa:
        for lis2 in faa:
            if lis!=lis2:
                li=lis.copy()
                dizhi=li.pop()
                li2=lis2.copy()
                dier=li2.pop()
                whe, wh=issubset(li,li2)

                if whe and len(wh)!=0:
                    wh.append(dier-dizhi)
                    faa.remove(lis2)
                    faa.append(wh)
                pass

    xuyfanhui=[]
    for khx in faa:
        if khx[-1]==len(khx)-1 and khx[-1]!=0:
            khx.pop()
            for m in khx:

                poss[m]=-2
                addFlags.append(m)
                xuyfanhui.append(m)
    if len(xuyfanhui)!=0:
        return "m",xuyfanhui,poss
        pass

    for khx in faa:
        if khx[-1]==0:
            khx.pop()
            if len(khx)!=0:
                kh=khx.copy()
                faa.remove(khx)
                addNums.extend(kh)
                return "k",kh,poss
            else:
                faa.remove(khx)

    for khx in faa:
        if len(khx)==1:
            faa.remove(khx)

    for khx in faa:
        if len(khx)!=0 and len(khx)!=1:
            shaa=khx[-1]
            xiaa=len(khx)-1
            if xiaa!=0:
                gailv=shaa/xiaa
                khx.append(gailv)
    bon=0
    count=0
    for n in poss.keys():
        if poss[n]==-1 or poss[n]==-2:
            bon=bon+1
        if poss[n]==9:
            count=count+1
    for khx in faa:
        if len(khx) or len(khx)==1 or len(khx)==2:
            faa.remove(khx)
    #Better decision
    # this part is used to make better decision.
    # We will determine whether there is a set of unopen cell which pick randomly from it is obviously better
    # than pick randomly from whole unopen cells
    if len(faa)!=0:
        faa.sort(key=takelast)
        hha=faa[0]
        gl=(leishu-bon)/count
        if hha[-1]<gl and not hha:# if the unopen cells in this set is obviously better than pick randomly from whole unopen cells
            ha=hha.copy()
            faa.remove(hha)
            ha.pop()
            ha.pop()
            suij = random.sample(ha.keys(), 1)
            si=[]
            si.append(suij)#pick one cell from this set
            print(si)
            addNums.extend(si)
            return "k",si,poss
    ba=[]
    return "k",ba,poss


def possTomazeopen(d,poss):
    firstLayer =np.random.binomial(1, 0, size=(d, d))
    i=0
    while i<d:
        j=0
        while j<d:
            firstLayer[i,j]=poss[(i,j)]
            j=j+1
            pass
        i=i+1
        pass
    return firstLayer

# 2.2 parttwo
def jiekou(dd,leishu,mzopen, mzanswer):
    poa=mazeopenTopose(mzopen,dd)
    g,h,poa=imporveAgent(poa,dd,leishu)
    mzopen=possTomazeopen(dd,poa)
    if g == "k":
        if len(h) != 0:
            for zb in h:
                i, j = zb
                mzopen[i, j] = mzanswer[i, j]
                if mzanswer[i, j]==-1:
                    score=score-1
                pass
            pass
        pass
    return mzopen

# anything related to safecellsleft is global information part
def solver(mzopen, mzanswer, undealposition):
    global score
    global addFlags
    global addNums
    sr, sc = undealposition
    mzopen[sr, sc] = mzanswer[sr, sc]
    cleared = [undealposition]  # The order we open the grid(excluding flags)
    flags = []
    corner = 3
    remainmine = a[1]
    if remainmine == 0:  # open all , no more mines
        for i in range(0, d):
            for j in range(0, d):
                if mzopen[i, j] == 9:
                    mzopen[i, j] = mzanswer[i, j]
                    cleared.append([i, j])
                    print("Marked all the mines in advance open all remains")
        return mzopen

    safecellsleft = d*d - a[1]
    if mzopen[sr, sc] != -1:
        safecellsleft = safecellsleft - 1
    if safecellsleft == 0:
        for i in range(0, d):
            for j in range(0, d):
                if mzopen[i, j] == 9:
                    mzopen[i, j] = -2
                    flags.append([i, j])
                    print("All the safety grids are opened mark all remains")
        return mzopen

    while mzopen[sr, sc] == -1:
        score = score - 1
        print("Deduct points", sr, sc)
        print(score)
        remainmine = remainmine - 1
        if remainmine == 0:  # open all , no more mines
            for i in range(0, d):
                for j in range(0, d):
                    if mzopen[i, j] == 9:
                        mzopen[i, j] = mzanswer[i, j]
                        cleared.append([i, j])
                        print("Marked all the mines in advance open all remains")
            return mzopen
        if corner == 3 and mzopen[0, d - 1] != 9:
            corner = corner - 1  # 2
        if corner == 2 and mzopen[d - 1, 0] != 9:
            corner = corner - 1  # 1
        if corner == 1 and mzopen[d - 1, d - 1] != 9:
            corner = corner - 1  # 0

        if corner == 3:
            corner = corner - 1
            if mzopen[0, d - 1] == 9:
                sr = 0
                sc = d - 1
                mzopen[sr, sc] = mzanswer[sr, sc]
                cleared.append([sr, sc])
                if mzopen[sr, sc] != -1:
                    safecellsleft = safecellsleft - 1
                    if safecellsleft == 0:
                        for i in range(0, d):
                            for j in range(0, d):
                                if mzopen[i, j] == 9:
                                    mzopen[i, j] = -2
                                    flags.append([i, j])
                                    print("All the safety grids are opened mark all remains")
                        return mzopen
                print("corner open")

        elif corner == 2:
            corner = corner - 1
            if mzopen[d - 1, 0] == 9:
                sr = d - 1
                sc = 0
                mzopen[sr, sc] = mzanswer[sr, sc]
                cleared.append([sr, sc])
                if mzopen[sr, sc] != -1:
                    safecellsleft = safecellsleft - 1
                    if safecellsleft == 0:
                        for i in range(0, d):
                            for j in range(0, d):
                                if mzopen[i, j] == 9:
                                    mzopen[i, j] = -2
                                    flags.append([i, j])
                                    print("All the safety grids are opened mark all remains")
                        return mzopen
                print("corner open")

        elif corner == 1:
            corner = corner - 1
            if mzopen[d - 1, d - 1] == 9:
                sr = d - 1
                sc = d - 1
                mzopen[sr, sc] = mzanswer[sr, sc]
                cleared.append([sr, sc])
                if mzopen[sr, sc] != -1:
                    safecellsleft = safecellsleft - 1
                    if safecellsleft == 0:
                        for i in range(0, d):
                            for j in range(0, d):
                                if mzopen[i, j] == 9:
                                    mzopen[i, j] = -2
                                    flags.append([i, j])
                                    print("All the safety grids are opened mark all remains")
                        return mzopen
                print("corner open")

        else:
            rrr = random.randint(0, d - 1)
            ccc = random.randint(0, d - 1)
            while mzopen[rrr, ccc] != 9:
                rrr = random.randint(0, d - 1)
                ccc = random.randint(0, d - 1)
            print("random position", rrr, ccc)
            mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
            cleared.append([rrr, ccc])
            if mzopen[rrr, ccc] != -1:
                safecellsleft = safecellsleft - 1
                if safecellsleft == 0:
                    for i in range(0, d):
                        for j in range(0, d):
                            if mzopen[i, j] == 9:
                                mzopen[i, j] = -2
                                flags.append([i, j])
                                print("All the safety grids are opened mark all remains")
                    return mzopen
            while mzopen[rrr, ccc] == -1:
                score = score - 1
                print("Deduct points", rrr, ccc)
                print(score)
                remainmine = remainmine - 1
                if remainmine == 0: # open all , no more mines
                    for i in range(0, d):
                        for j in range(0, d):
                            if mzopen[i, j] == 9:
                                mzopen[i, j] = mzanswer[i, j]
                                cleared.append([i, j])
                                print("Marked all the mines in advance open all remains")
                    return mzopen

                while mzopen[rrr, ccc] != 9:
                    rrr = random.randint(0, d - 1)
                    ccc = random.randint(0, d - 1)
                mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                print("random position", rrr, ccc)
                cleared.append([rrr, ccc])
                sr=rrr
                sc=ccc
            if mzopen[rrr, ccc] != -1:
                safecellsleft = safecellsleft - 1
                if safecellsleft == 0:
                    for i in range(0, d):
                        for j in range(0, d):
                            if mzopen[i, j] == 9:
                                mzopen[i, j] = -2
                                flags.append([i, j])
                                print("All the safety grids are opened mark all remains")
                    return mzopen



    while 9 in mzopen:
        if remainmine == 0:  # open all , no more mines
            for i in range(0, d):
                for j in range(0, d):
                    if mzopen[i, j] == 9:
                        mzopen[i, j] = mzanswer[i, j]
                        cleared.append([i, j])
                        print("Marked all the mines in advance open all remains")
            return mzopen

        if safecellsleft == 0:
            for i in range(0, d):
                for j in range(0, d):
                    if mzopen[i, j] == 9:
                        mzopen[i, j] = -2
                        flags.append([i, j])
                        print("All the safety grids are opened mark all remains")
            return mzopen

        ggstandard = mzopen.copy()
        for i in range(0, d):
            for j in range(0, d):
                if mzopen[i, j] == 9:
                    continue
                row = i
                col = j
                aroundlist = judge(row, col)  # only use for check the mines and flags
                targetaround = []  # The remaining girds around the target
                mcounter = 0
                remain = 0
                while aroundlist:
                    cell = aroundlist.pop(0)
                    rr, cc = cell
                    if mzopen[rr, cc] == -1 or mzopen[rr, cc] == -2:  # how many mines and flags around
                        mcounter = mcounter + 1
                    if mzopen[rr, cc] == 9:
                        remain = remain + 1  # grids left around target
                        targetaround.append([rr, cc])  # Get what's left around the target

                # print(remain)

                if len(targetaround) == 0:  # no remain grids around this target
                    continue

                # we know all the mine positions open the remain grids around
                if mzopen[row, col] == mcounter or mzopen[row, col] == 0:
                    while targetaround:
                        temp = targetaround.pop(0)
                        tr, tc = temp
                        mzopen[tr, tc] = mzanswer[tr, tc]
                        cleared.append(temp)
                        safecellsleft = safecellsleft - 1

                # we know all the remain grids around are mines mark them all
                elif mzopen[row, col] == remain + mcounter and mzopen[row, col] != 0:  # 已知剩下的全是雷
                    while targetaround:
                        temp = targetaround.pop(0)
                        tr, tc = temp
                        mzopen[tr, tc] = -2  # -2 for flags
                        flags.append(temp)  # save the flags
                        remainmine = remainmine - 1
                else:
                    pass

        if np.array_equal(ggstandard, mzopen):  # if need 2.2
            standard = mzopen.copy()
            print(" ")
            print("before: ")
            print(mzopen)
            print(" --==--")
            logicresult = improved_agent(mzopen, mzanswer)          # 2.2 partone
            print(" ")
            print("after: ")
            print(logicresult)
            print(" --==--")
            mzopen = jiekou(int(a[0]), int(a[1]), mzopen, mzanswer)  # 2.2 parttwo
            logicresult = mzopen
            print(" ")
            print("afterling: ")
            print(logicresult)
            print(" --==--")
            if np.array_equal(standard, logicresult):  # if need random
                print("yes need random")   # yes random
                if corner != 0:  # try corner first
                    print(corner, "conner numbers")
                    if corner == 3 and mzopen[0, d - 1] != 9:
                        corner = corner - 1  # 2
                    if corner == 2 and mzopen[d - 1, 0] != 9:
                        corner = corner - 1  # 1
                    if corner == 1 and mzopen[d - 1, d - 1] != 9:
                        corner = corner - 1  # 0
                    if corner == 3:
                        corner = corner - 1
                        if mzopen[0, d - 1] == 9:
                            sr = 0
                            sc = d - 1
                            mzopen[sr, sc] = mzanswer[sr, sc]
                            cleared.append([sr, sc])
                            if mzopen[sr, sc] != -1:
                                safecellsleft = safecellsleft - 1
                                if safecellsleft == 0:
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = -2
                                                flags.append([i, j])
                                                print("All the safety grids are opened mark all remains")
                                    return mzopen
                            if mzopen[sr, sc] == -1:
                                score = score - 1
                                print("Deduct points", sr, sc)
                                print(score)
                                remainmine = remainmine - 1
                                if remainmine == 0:  # open all , no more mines
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = mzanswer[i, j]
                                                cleared.append([i, j])
                                                print("Marked all the mines in advance open all remains")
                                    return mzopen
                                corner = corner - 1  # 1
                                sr = d - 1
                                sc = 0
                                mzopen[sr, sc] = mzanswer[sr, sc]
                                cleared.append([sr, sc])
                                if mzopen[sr, sc] != -1:
                                    safecellsleft = safecellsleft - 1
                                    if safecellsleft == 0:
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = -2
                                                    flags.append([i, j])
                                                    print("All the safety grids are opened mark all remains")
                                        return mzopen
                                if mzopen[sr, sc] == -1:
                                    score = score - 1
                                    print("Deduct points", sr, sc)
                                    print(score)
                                    remainmine = remainmine - 1
                                    if remainmine == 0:  # open all , no more mines
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = mzanswer[i, j]
                                                    cleared.append([i, j])
                                                    print("Marked all the mines in advance open all remains")
                                        return mzopen
                                    corner = corner - 1  # 0
                                    sr = d - 1
                                    sc = d - 1
                                    mzopen[sr, sc] = mzanswer[sr, sc]
                                    cleared.append([sr, sc])
                                    if mzopen[sr, sc] != -1:
                                        safecellsleft = safecellsleft - 1
                                        if safecellsleft == 0:
                                            for i in range(0, d):
                                                for j in range(0, d):
                                                    if mzopen[i, j] == 9:
                                                        mzopen[i, j] = -2
                                                        flags.append([i, j])
                                                        print("All the safety grids are opened mark all remains")
                                            return mzopen
                                    if mzopen[sr, sc] == -1:  # random
                                        score = score - 1
                                        print("Deduct points", sr, sc)
                                        print(score)
                                        remainmine = remainmine - 1
                                        if remainmine == 0:  # open all , no more mines
                                            for i in range(0, d):
                                                for j in range(0, d):
                                                    if mzopen[i, j] == 9:
                                                        mzopen[i, j] = mzanswer[i, j]
                                                        cleared.append([i, j])
                                                        print("Marked all the mines in advance open all remains")
                                            return mzopen
                                        rrr = random.randint(0, d - 1)
                                        ccc = random.randint(0, d - 1)
                                        while mzopen[rrr, ccc] != 9:
                                            rrr = random.randint(0, d - 1)
                                            ccc = random.randint(0, d - 1)
                                        mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                        print("Random position", rrr, ccc)
                                        cleared.append([rrr, ccc])
                                        if mzopen[rrr, ccc] != -1:
                                            safecellsleft = safecellsleft - 1
                                            if safecellsleft == 0:
                                                for i in range(0, d):
                                                    for j in range(0, d):
                                                        if mzopen[i, j] == 9:
                                                            mzopen[i, j] = -2
                                                            flags.append([i, j])
                                                            print("All the safety grids are opened mark all remains")
                                                return mzopen
                                        while mzopen[rrr, ccc] == -1:
                                            score = score - 1
                                            print("Deduct points", rrr, ccc)
                                            print(score)
                                            remainmine = remainmine - 1
                                            if remainmine == 0:  # open all , no more mines
                                                for i in range(0, d):
                                                    for j in range(0, d):
                                                        if mzopen[i, j] == 9:
                                                            mzopen[i, j] = mzanswer[i, j]
                                                            cleared.append([i, j])
                                                            print("Marked all the mines in advance open all remains")
                                                return mzopen
                                            while mzopen[rrr, ccc] != 9:
                                                rrr = random.randint(0, d - 1)
                                                ccc = random.randint(0, d - 1)
                                            mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                            cleared.append([rrr, ccc])
                                            if mzopen[rrr, ccc] != -1:
                                                safecellsleft = safecellsleft - 1
                                                if safecellsleft == 0:
                                                    for i in range(0, d):
                                                        for j in range(0, d):
                                                            if mzopen[i, j] == 9:
                                                                mzopen[i, j] = -2
                                                                flags.append([i, j])
                                                                print("All the safety grids are opened mark all remains")
                                                    return mzopen
                    elif corner == 2:
                        corner = corner - 1
                        if mzopen[d - 1, 0] == 9:
                            sr = d - 1
                            sc = 0
                            mzopen[sr, sc] = mzanswer[sr, sc]
                            cleared.append([sr, sc])
                            if mzopen[sr, sc] == -1:
                                score = score - 1
                                print("Deduct points", sr, sc)
                                print(score)
                                remainmine = remainmine - 1
                                if remainmine == 0:  # open all , no more mines
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = mzanswer[i, j]
                                                cleared.append([i, j])
                                                print("Marked all the mines in advance open all remains")
                                    return mzopen
                                corner = corner - 1  # 0
                                sr = d - 1
                                sc = d - 1
                                mzopen[sr, sc] = mzanswer[sr, sc]
                                cleared.append([sr, sc])
                                if mzopen[sr, sc] != -1:
                                    safecellsleft = safecellsleft - 1
                                    if safecellsleft == 0:
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = -2
                                                    flags.append([i, j])
                                                    print("All the safety grids are opened mark all remains")
                                        return mzopen
                                if mzopen[sr, sc] == -1:  # Random
                                    score = score - 1
                                    print("Deduct points", sr, sc)
                                    print(score)
                                    remainmine = remainmine - 1
                                    if remainmine == 0:  # open all , no more mines
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = mzanswer[i, j]
                                                    cleared.append([i, j])
                                                    print("Marked all the mines in advance open all remains")
                                        return mzopen
                                    rrr = random.randint(0, d - 1)
                                    ccc = random.randint(0, d - 1)
                                    while mzopen[rrr, ccc] != 9:
                                        rrr = random.randint(0, d - 1)
                                        ccc = random.randint(0, d - 1)
                                    mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                    print("Random position", rrr, ccc)
                                    cleared.append([rrr, ccc])
                                    if mzopen[rrr, ccc] != -1:
                                        safecellsleft = safecellsleft - 1
                                        if safecellsleft == 0:
                                            for i in range(0, d):
                                                for j in range(0, d):
                                                    if mzopen[i, j] == 9:
                                                        mzopen[i, j] = -2
                                                        flags.append([i, j])
                                                        print("All the safety grids are opened mark all remains")
                                            return mzopen
                                    while mzopen[rrr, ccc] == -1:
                                        score = score - 1
                                        print("Deduct points", rrr, ccc)
                                        print(score)
                                        remainmine = remainmine - 1
                                        if remainmine == 0:  # open all , no more mines
                                            for i in range(0, d):
                                                for j in range(0, d):
                                                    if mzopen[i, j] == 9:
                                                        mzopen[i, j] = mzanswer[i, j]
                                                        cleared.append([i, j])
                                                        print("Marked all the mines in advance open all remains")
                                            return mzopen
                                        while mzopen[rrr, ccc] != 9:
                                            rrr = random.randint(0, d - 1)
                                            ccc = random.randint(0, d - 1)
                                        mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                        cleared.append([rrr, ccc])
                                        if mzopen[rrr, ccc] != -1:
                                            safecellsleft = safecellsleft - 1
                                            if safecellsleft == 0:
                                                for i in range(0, d):
                                                    for j in range(0, d):
                                                        if mzopen[i, j] == 9:
                                                            mzopen[i, j] = -2
                                                            flags.append([i, j])
                                                            print("All the safety grids are opened mark all remains")
                                                return mzopen

                    elif corner == 1:
                        corner = corner - 1
                        if mzopen[d - 1, d - 1] == 9:
                            sr = d - 1
                            sc = d - 1
                            mzopen[sr, sc] = mzanswer[sr, sc]
                            cleared.append([sr, sc])
                            if mzopen[sr, sc] != -1:
                                safecellsleft = safecellsleft - 1
                                if safecellsleft == 0:
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = -2
                                                flags.append([i, j])
                                                print("All the safety grids are opened mark all remains")
                                    return mzopen
                            if mzopen[sr, sc] == -1:  # Random
                                score = score - 1
                                print("Deduct points", sr, sc)
                                print(score)
                                remainmine = remainmine - 1
                                if remainmine == 0:  # open all , no more mines
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = mzanswer[i, j]
                                                cleared.append([i, j])
                                                print("Marked all the mines in advance open all remains")
                                    return mzopen
                                rrr = random.randint(0, d - 1)
                                ccc = random.randint(0, d - 1)
                                while mzopen[rrr, ccc] != 9:
                                    rrr = random.randint(0, d - 1)
                                    ccc = random.randint(0, d - 1)
                                mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                print("Random position", rrr, ccc)
                                cleared.append([rrr, ccc])
                                if mzopen[rrr, ccc] != -1:
                                    safecellsleft = safecellsleft - 1
                                    if safecellsleft == 0:
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = -2
                                                    flags.append([i, j])
                                                    print("All the safety grids are opened mark all remains")
                                        return mzopen
                                while mzopen[rrr, ccc] == -1:
                                    score = score - 1
                                    print("Deduct points", rrr, ccc)
                                    print(score)
                                    remainmine = remainmine - 1
                                    if remainmine == 0:  # open all , no more mines
                                        for i in range(0, d):
                                            for j in range(0, d):
                                                if mzopen[i, j] == 9:
                                                    mzopen[i, j] = mzanswer[i, j]
                                                    cleared.append([i, j])
                                                    print("Marked all the mines in advance open all remains")
                                        return mzopen
                                    while mzopen[rrr, ccc] != 9:
                                        rrr = random.randint(0, d - 1)
                                        ccc = random.randint(0, d - 1)
                                    mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                                    cleared.append([rrr, ccc])
                                    if mzopen[rrr, ccc] != -1:
                                        safecellsleft = safecellsleft - 1
                                        if safecellsleft == 0:
                                            for i in range(0, d):
                                                for j in range(0, d):
                                                    if mzopen[i, j] == 9:
                                                        mzopen[i, j] = -2
                                                        flags.append([i, j])
                                                        print("All the safety grids are opened mark all remains")
                                            return mzopen

                    else:
                        print("no corner anymore")
                        rrr = random.randint(0, d - 1)
                        ccc = random.randint(0, d - 1)
                        while mzopen[rrr, ccc] != 9:
                            rrr = random.randint(0, d - 1)
                            ccc = random.randint(0, d - 1)
                        mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                        print("Random position", rrr, ccc)
                        cleared.append([rrr, ccc])
                        if mzopen[rrr, ccc] != -1:
                            safecellsleft = safecellsleft - 1
                            if safecellsleft == 0:
                                for i in range(0, d):
                                    for j in range(0, d):
                                        if mzopen[i, j] == 9:
                                            mzopen[i, j] = -2
                                            flags.append([i, j])
                                            print("All the safety grids are opened mark all remains")
                                return mzopen
                        while mzopen[rrr, ccc] == -1:
                            score = score - 1
                            print("Deduct points", rrr, ccc)
                            print(score)
                            remainmine = remainmine - 1
                            if remainmine == 0:  # open all , no more mines
                                for i in range(0, d):
                                    for j in range(0, d):
                                        if mzopen[i, j] == 9:
                                            mzopen[i, j] = mzanswer[i, j]
                                            cleared.append([i, j])
                                            print("Marked all the mines in advance open all remains")
                                return mzopen
                            while mzopen[rrr, ccc] != 9:
                                rrr = random.randint(0, d - 1)
                                ccc = random.randint(0, d - 1)
                            mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                            cleared.append([rrr, ccc])
                            if mzopen[rrr, ccc] != -1:
                                safecellsleft = safecellsleft - 1
                                if safecellsleft == 0:
                                    for i in range(0, d):
                                        for j in range(0, d):
                                            if mzopen[i, j] == 9:
                                                mzopen[i, j] = -2
                                                flags.append([i, j])
                                                print("All the safety grids are opened mark all remains")
                                    return mzopen

                else:  # corner = 0
                    rrr = random.randint(0, d - 1)
                    ccc = random.randint(0, d - 1)
                    while mzopen[rrr, ccc] != 9:
                        rrr = random.randint(0, d - 1)
                        ccc = random.randint(0, d - 1)
                    mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                    print("Random position", rrr, ccc)
                    cleared.append([rrr, ccc])
                    if mzopen[rrr, ccc] != -1:
                        safecellsleft = safecellsleft - 1
                        if safecellsleft == 0:
                            for i in range(0, d):
                                for j in range(0, d):
                                    if mzopen[i, j] == 9:
                                        mzopen[i, j] = -2
                                        flags.append([i, j])
                                        print("All the safety grids are opened mark all remains")
                            return mzopen
                    while mzopen[rrr, ccc] == -1:
                        score = score - 1
                        print("Deduct points", rrr, ccc)
                        print(score)
                        remainmine = remainmine - 1
                        print(remainmine)
                        if remainmine == 0:  # open all , no more mines
                            for i in range(0, d):
                                for j in range(0, d):
                                    if mzopen[i, j] == 9:
                                        mzopen[i, j] = mzanswer[i, j]
                                        cleared.append([i, j])
                                        print("Marked all the mines in advance open all remains")
                            return mzopen
                        while mzopen[rrr, ccc] != 9:
                            rrr = random.randint(0, d - 1)
                            ccc = random.randint(0, d - 1)
                        mzopen[rrr, ccc] = mzanswer[rrr, ccc]  # get random
                        cleared.append([rrr, ccc])
                        if mzopen[rrr, ccc] != -1:
                            safecellsleft = safecellsleft - 1
                            if safecellsleft == 0:
                                for i in range(0, d):
                                    for j in range(0, d):
                                        if mzopen[i, j] == 9:
                                            mzopen[i, j] = -2
                                            flags.append([i, j])
                                            print("All the safety grids are opened mark all remains")
                                return mzopen
            else:
                while addFlags:
                    te = addFlags.pop(0)
                    if te not in flags:
                        flags.append(te)
                        remainmine = remainmine - 1
                while addNums:
                    cleared.append(addNums.pop(0))
                    safecellsleft = safecellsleft - 1

    print("Completed normally")
    # print(remainmine)
    print(cleared, "cleared")  # The order we open the grid
    print(flags)  # The order we marked

    # gif maker if u dont need it just dont run it. it is slow
    # firstLayer = np.mat(np.ones((int(a[0]),int(a[0]))))
    # p=[]
    # cou=0
    # for zbiu in cleared:
    #     i,j=zbiu
    #     firstLayer[i,j]=0
    #     firstLayer=ma.masked_array(firstLayer, firstLayer<0.5)
    #     plt.imshow(mzanswer,interpolation='nearest',cmap=plt.cm.Reds)
    #     plt.imshow(firstLayer,interpolation='nearest',cmap=plt.cm.gray_r)
    #     plt.text(x=j, y=i, s=mzanswer[i,j])
    #     filename = "./mine" + str(cou) + ".png"
    #     plt.savefig(filename)
    #     fn=filename.lstrip('./')
    #     p.append(fn)
    #     cou=cou+1
    #     pass
    # for zbiu in flags:
    #     i,j=zbiu
    #     firstLayer[i,j]=0
    #     firstLayer=ma.masked_array(firstLayer, firstLayer<0.5)
    #     plt.imshow(mzanswer,interpolation='nearest',cmap=plt.cm.Reds)
    #     plt.imshow(firstLayer,interpolation='nearest',cmap=plt.cm.gray_r)
    #     plt.text(x=j, y=i, s="M")
    #     filename = "./mine" + str(cou) + ".png"
    #     plt.savefig(filename)
    #     fn=filename.lstrip('./')
    #     p.append(fn)
    #     cou=cou+1
    #     pass
    # create_gif(p,'./mine.gif',  1)
    print(len(cleared))
    print(len(flags))
    print("final score", score, "/", a[1])
    return mzopen


if __name__ == "__main__":
    # ss=0
    #for k in range(0,1):
    print("Please input in that form: dim numOfMines")
    a = list(map(float, input(' ').split()))
    mat = maze(int(a[0]), int(a[1]))
    d = int(a[0])
    print(mat)
    print(" ")
    op = np.random.randint(9, 10, [d, d])
    # print(op)
    score = int(a[1])
    addFlags = []
    addNums = []

    startpoint = [0, 0]
    result = solver(op, mat, startpoint)
    print("final score", score, "/", a[1])
    print("----")
    #print(ss/50)
    # print(" ")
    # print("gg")
