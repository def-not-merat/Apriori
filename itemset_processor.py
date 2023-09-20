from itertools import combinations


class FrequentItemsetCalculator(object):
    def __init__(self, transactions, support_threshold):
        self.transactions = transactions
        self.support_threshold = support_threshold
        self.levels_itemset = {}
        
    def count_1_itemsets(self):
        #TODO: This function counts the support count for 1-itemsets and returns the frequent 1-itemsets
        pass
        #return L1


    def generate_candidate(self, k):
        #TODO generate k-itemset candidates from (k-1)-itemset and prunes candidates based on apriori property and returns the list of candidates.
        pass 
        #return C_k
        
    def count_support(self, C_k):
        #TODO: This fucntion counts the support for each candidates in C_k and after checking the support threshold, returns the frequent itemsets of level k.
        pass
        #return L_k

        