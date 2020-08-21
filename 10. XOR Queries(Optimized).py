#https://leetcode.com/discuss/interview-question/797724/Google-Online-Challenge-Intern-2021-(Coding-Questions-%3A-2-or-Time-%3A-60-mins)

def queries(T,Q,query):

    list=[0]
    ##Suppose we have inserted 6, 3, 2 in the list and then xor everything with 4, 5,
    # then it is same as XOR-ing with X = XOR(4,5).

    #For Query 1, XOR with request[i]. we will not XOR every element in the trie
    #with xi.instead, we will just update X = XOR(x, xi)


    X=0 #x is total xor so far

    for request in query:
        if request[0]=="0": #insert in list #For Query 0 : dont insert num in list, but we will insert number xor X (is ensures that when print the whole list, it will cancel out the previous XORs.
                            #so our list will contain for the 2nd example {0,6,3,(3 XOR(4)),}
            list.append((int(request[1])^X)) #
        else: #its one perform xor on all items in query ^
            X=X^int(request[1])

    #xow ill XOR all with the final X var
    list = [i ^ X for i in list]
    list.sort()
    print(list)




queries(1,5,["06", "03", "02","14","15"]) #[1, 2, 3, 7]
queries(1,5,["06", "03", "02","14","03","15","12"]) #[0, 1, 3, 4, 5]

"""Question 2:

You are given a list S that initially contains a single value 0. You must perform Q queries of the following types:

0 X : Insert X in the list
1 X : For every element A in S, replace it by A XOR X.
After performing Q queries, print all the values of the list in increasing order of their values.

Input format :

The first line contains a single integer T denoting the number of test cases
The first line of each test case contains a single integer Q denoting the number of queries.
Next Q lines of each test case contains queries of two types.
Output format:
For each test case, print space seperated values of S in increasing order of their values in a new line.

Constraints:

1 <= T <= 100
1 <= Q <= 10^6
0 <= X <= 10^9
The sum of Q over all test cases does not exceed 10^6.

Sample Input :
1
5
0 6
0 3
0 2
1 4
1 5

Sample Output : 1 2 3 7"""

"""
Input: Q = 10, S=0
3 --> 0
1 7 ---> S={0,7}
3 --> 0
2 4 --> S={4, 3}
2 8 --> S={12, 11}
2 3 --> S{15, 8}
1 10 --> S
1 3
3
2 1
Output: 0 0 3


The minimum is 0.
The number 7 added to S –> {0, 7}.
The minimum is still 0.
All of the numbers in S are changed to their xor with 4 –> {4, 3}.
All of the numbers in S are changed to their xor with 8 –> {12, 11}.
All of the numbers in S are changed to their xor with 3 –> {15, 8}.
The number 10 added to S –> {15, 8 ,10}.
The number 3 added to S –> {15, 8, 10, 3}.
The minimum is now 3.
All of the numbers in S are changed to their xor with 1 –> {14, 9, 11, 2}."""