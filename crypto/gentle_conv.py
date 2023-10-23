rb = "(D+V(D+V(D+V(D+V(D+V(D.+(D./(D.,(D.%(D.W(D+((D/((D//(D.+(D.R(D.%(D.*(D+((D.S(D./(D/%(D+V(D+V(D+V(D+V(D+V(D(V(D(Q(D.V(D.%(D.,(D--(D.V(D.)(D*((D.,(D.*(D/*(D,)(D.,(D/*(D.%(D-+(D**(D..(D/)(D./(D.+(D.)(D/)(D//(D.)(D.)(D*.(D.,(D.W(D.)(D..(D.*(D.+(D-%(D/)(D.S(D.+(D-,(D/)(D.*(D*-(D.+(D/*(D*%(D/$(D.,(D-Q(D/-(D/((D,Q(D-/(D-S(D-*(D-U(D-,(D*+(D,+(D.Q(D*.(D-S(D.*(D-V(D-Q(D.,(D,$(D(V(D(Q(D*/(D.-(D.+(D+U(D.$(D-U(D-/(D-U(D*)(D,((D-S(D.$(D*)(D**(D.%(D.%(D.-(D/Q(D-R(D-Q(D.$(D*%(D.U(D..(D.*(D,.(D,-(D.V(D,,(D/((D//(D**(D-V(D//(D.%(D*.(D.U(D.U(D-/(D*,(D/*(D,%(D-.(D*((D-V(D,%(D.S(D-/(D/$(D.R(D-*(D+S(D-V(D,)(D*+(D.%(D,.(D-/(D,)(D-.(D..(D-,(D-)(D/+(D(V(D(Q(D*)(D*.(D,/(D.$(D,*(D.,(D/%(D-R(D.W(D-+(D-)(D-U(D.)(D*,(D,+(D.-(D+S(D/((D--(D-*(D,,(D/-(D.+(D,((D,%(D-/(D*+(D/.(D+U(D.%(D-+(D.%(D/Q(D/,(D-W(D/Q(D*/(D*.(D/-(D/%(D-/(D.+(D.-(D.*(D*((D.U(D/%(D*/(D/$(D-.(D/+(D/,(D/.(D,Q(D+U(D,)(D*,(D.S(D-,(D.*(D.S(D,)(D,-(D*$(D(V(D(Q(D-R(D*.(D-U(D,/(D-)(D.W(D..(D/.(D..(D,%(D-.(D-$(D.S(D.V(D+U(D/)(D//(D/)(D.%(D..(D.)(D/)(D.)(D.+(D(V(D(Q(D+V(D+V(D+V(D+V(D+V(D./(D.W(D..(D+((D/((D//(D.+(D.R(D.%(D.*(D+((D.S(D./(D/%(D+V(D+V(D+V(D+V(D+V(D(Q(D(Q(D--(D-R(D-)(D-,(D,S(D*+(D--(D*)(D-*(D**(D-.(D*)(D-.(D-)(D-*(D**(D-*(D*.(D--(D*/(D-+(D*+(D-+(D**(D*$(D*/(D*-(D*,(D*.(D*/(D*%(D-.(D*-(D-*(D*.(D**(D*((D,V"
bin_list = []

for i in rb:
    bin_list.append(ord(i))


def gray_to_binary(n):
    mask = n >> 1
    while mask != 0:
        n ^= mask
        mask >>= 1
    return n
list_2 = []

for i in bin_list:
    list_2.append(gray_to_binary(int(bin(i)[2:],2)))
#print(list_2, end="")

for i in list_2:
    print(chr(i), end="")
    #output is hex in the form 0x..etc. Finished decoding in cyberchef, but can do it here too
