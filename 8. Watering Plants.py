def wateringPlants(plants, cap1, cap2):

    p1=0
    refills=0
    p2=len(plants)-1
    water1=0
    water2=0  #[2,4,5,1,2],5,7
    while p1<=p2:#0,4 / 1,3 /1,2
        print('p1',p1)
        print('p2',p2)
        print('water1',water1)
        print('water2',water2)
        if p1!=p2:
            if water1<plants[p1]: #0<2, 5<2, 3<4, 5<4
                refills+=1 #r=1 , refills=3
                water1=cap1 #w1=5 #5
            else:
                water1-=plants[p1] #w1=3, w1=1
                p1+=1 #p1=2, p=3

            if water2<plants[p2] and p1!=p2: #0<2, 7<2, 5<1
                refills+=1 #r=2
                water2=cap2 #w2=7
            else:
                water2-=plants[p2] #w2=5, w2=4
                p2-=1 #4, p2=3

        if p1==p2:
            print('yes p1==p2')
            if (water2+water1)<plants[p1]:
                refills+=1
                if cap2>cap1:
                    water2=cap2
                else:
                    water1=cap1
            else:
                  p1+=1
                  p2-=1
        print('refills',refills)#2, 2, 3
    return refills

assert (wateringPlants([2,4,5,1,2],5,7)==3)