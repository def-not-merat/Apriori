from itertools import combinations
import math

from file_handler import FileHandlingTools
from rule_processor import RuleGenerator

class FrequentItemsetCalculator(object):
    def __init__(self, transactions, support_threshold):
        self.transactions = transactions
        self.support_threshold = support_threshold
        self.levels_itemset = {}
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

        for i in range(len(keys)-1):
            # print (keys)
            if keys[i][:-1] == keys[i+1][:-1]:
                for j in range (i+1,len(keys)):
                    if keys[i][:-1] != keys[j][:-1]:
                        # print ("for:",i,j)
                        break
                    cand = keys[i] + (keys[j][-1],)

                    if self.test_can(cand, prev_level):
                        C_k[cand] = 0
        return C_k

    def test_can(self, cand, prev_level):
        for i in range (len(cand)):
            test = cand[0:i] + cand [i+1:]
            if test not in prev_level:
                # print (cand, "rej", test)
                return False
        return True
                
                
                    
    
    def candidate_helper(self, t, curr, l, C_k):
        # print (curr)
        if len(curr) == l:
            # print ("l=cur")
            if tuple(curr) in C_k:
                C_k[tuple(curr)]+=1
            return
        if l>len(t)+len(curr):
            # print("over")
            return
        self.candidate_helper(t[1:], curr + [t[0]], l, C_k)
        self.candidate_helper(t[1:], curr, l, C_k)
        
    def count_support(self, C_k):
        #TODO: This fucntion counts the support for each candidates in C_k and after checking the support threshold, returns the frequent itemsets of level k.
        for t in transactions:
            self.candidate_helper(t, [], len(list(C_k.keys())[0]), C_k) 
        keys = C_k.keys()
        L_k = {}
        for i in keys:
            if C_k[i] >= self.support_threshold:
                L_k[i] = C_k[i]
        self.prev = L_k
        self.levels_itemset.update(L_k)
        return L_k

file_handler = FileHandlingTools('data.csv', 'mapping.csv')
transactions = file_handler.load_transactions()
frequent_itemsets_calc = FrequentItemsetCalculator(transactions, math.ceil(0.3 * len(transactions)))
prev_level = frequent_itemsets_calc.count_1_itemsets()
# print(prev_level)
C_2 = frequent_itemsets_calc.generate_candidate(1)
L_2 = frequent_itemsets_calc.count_support(C_2)
# print("l", L_2)

C_3 = frequent_itemsets_calc.generate_candidate(2)
L_3 = frequent_itemsets_calc.count_support(C_3)

# print (C_3)
print (frequent_itemsets_calc.levels_itemset)
rule_generator = RuleGenerator(frequent_itemsets_calc.levels_itemset, len(transactions))
rules = rule_generator.generate_rules(0.1)
print (rules)
# rules = rule_generator.quality_prune(rules)

        