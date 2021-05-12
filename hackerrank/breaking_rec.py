def breaking(scores=[]):
    maxi=mini=scores[0]
    lmin=lmax=0
    for i in scores:
        if i>maxi:
            maxi=i
            lmax+=1
        elif i<mini:
            mini=i
            lmin+=1
    return [lmax,lmin]

print(*(breaking([10,5,20,20,4,5,2,25,1])))