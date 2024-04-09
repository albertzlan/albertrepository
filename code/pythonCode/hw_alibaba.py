sstr = "20,2,5,2,10"
srcL = list(map(int, sstr.split(",")))
print(srcL)
dstL = []
imax = max(srcL)
for ii in range(len(srcL)):
    for jj in range(ii + 1, 2 * len(srcL)):
        idx = jj % len(srcL)
        print("ii=" + str(ii) + " jj=" + str(jj) + " idx=" + str(idx))
        if srcL[ii] == imax:
            dstL.append(-1)
            break
        elif srcL[ii] < srcL[idx]:
            dstL.append(srcL[idx])
            break
print(dstL)
