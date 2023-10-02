from itertools import combinations

class FrequentItemsetCalculator(object):
    def __init__(self, transactions, support_threshold):
        self.transactions = transactions
        self.support_threshold = support_threshold
        self.levels_itemset = {}
        self.lengths = []
        self.prev = {}
        
    def count_1_itemsets(self):
        #TODO: This function counts the support count for 1-itemsets and returns the frequent 1-itemsets
        L1_dict = {}
        for trans in self.transactions:
            for item in trans:
                if item in L1_dict:
                    L1_dict[item]+=1
                else:
                    L1_dict[item]=1
        L1={}
        for item in L1_dict:
            if L1_dict[item]>=self.support_threshold:
                L1[(item,)]=L1_dict[item]
        self.prev = L1
        self.levels_itemset=L1.copy()
        self.lengths.append(len(L1))
        return L1


    def generate_candidate(self, k):
        #TODO generate k-itemset candidates from (k-1)-itemset and prunes candidates based on apriori property and returns the list of candidates.
        prev_level = self.prev
        C_k = {} 
        keys = sorted(prev_level.keys())
        if k == 1:
            for i in range(len(keys)):
                for j in range(1,len(keys)-i):
                    C_k[(keys[i][0],keys[i+j][0])] = 0
            return C_k

        #check the first k-1 of itemsest against eachother to generate the candidates. 
        #(keep in mind everything is already sorted)
        for i in range(len(keys)-1):
            if keys[i][:-1] == keys[i+1][:-1]:
                for j in range (i+1,len(keys)):
                    if keys[i][:-1] != keys[j][:-1]:
                        break
                    cand = keys[i] + (keys[j][-1],)

                    if self.test_can(cand, prev_level): 
                        #if the first k-1 match, check if all the k-1 subsets exists in C_k to makes sure the new candidate holds the apriori property
                        C_k[cand] = 0
        return C_k

    def test_can(self, cand, prev_level):
        #checks every k-1 subset of cand against prev level to make sure it holds apriori property
        for i in range (len(cand)):
            test = cand[0:i] + cand [i+1:]
            if test not in prev_level:
                return False
        return True     
                    
    
    # def candidate_helper(self, t, curr, l, C_k):
    #     #this recursivly checks EVERY length l SUBSET of transaction t and counts it apearance in C_K
    #     #if lenght of t is long enough, there would be a recursion stack overflow
    #     #DONT USE THIS ONE, THIS IS JUST HERE TO SHOW HOW NOT TO DO IT :p
    #     if len(curr) == l:
    #         if tuple(curr) in C_k:
    #             C_k[tuple(curr)]+=1
    #         return
    #     if l>len(t)+len(curr):
    #         return
    #     self.candidate_helper(t[1:], curr + [t[0]], l, C_k)
    #     self.candidate_helper(t[1:], curr, l, C_k)

    # def helper(self,C_k):
    #     #this one checks every candidate against every transactions 1 by 1 to get the counts of apearance.
    #     #it works but its SUPER slow (uses the sorted property to linearly check every item in candidate against every item in a transaction)
    #     #DONT USE THIS. use helper_2
    #     item_n = -1
    #     for item in C_k:
    #         item_n+=1
    #         if(item_n%1000==0):
    #             print("item", item_n, len(C_k))
    #         t_n = 0
    #         for t in self.transactions:
    #             if self.isInItem(item,t, 0, 0):
    #                 C_k[item]+=1

    # def isInItem(self, item, t, item_c, t_c):
    #     #checks if the item is in transaction t. if it is, count it
    #     if item_c==len(item):
    #         return True
    #     while t_c<len(t):
    #         if t[t_c]==item[item_c]:
    #             return self.isInItem(item, t, item_c + 1, t_c + 1)
    #         t_c+=1
    #     return False

        

    def helper_2(self, C_k):
        #counts the number of apearnace of candidates in all transactions
        #turns a transaction in to a set. checks every candidate againest this set to see if the itemes apeare.
        #updates the count of C_k
        item_n = -1
        for t in self.transactions:
            item_n+=1
            if(item_n%500==0):
                print("transaction", item_n, len(self.transactions))
            dic = set()
            for item in t:
                dic.add(item)
            for key in C_k.keys():
                exists = True
                for i in key:
                    if i not in dic:
                        exists = False
                if exists:
                    C_k[key] += 1


    def count_support(self, C_k):
        #TODO: This fucntion counts the support for each candidates in C_k and after checking the support threshold, returns the frequent itemsets of level k.
        
        if len(C_k)==0:
            return {}

        keys = C_k.keys()
        k = len(list(keys)[0])
        print("counting level:", k)

        self.helper_2(C_k)
       
        L_k = {}
        for i in keys:
            #return the candidates that satisfy the support
            if C_k[i] >= self.support_threshold:
                L_k[i] = C_k[i]
        self.prev = L_k
        self.levels_itemset.update(L_k)
        self.lengths.append(len(L_k))
        return L_k

        