from itertools import combinations


class RuleGenerator(object):

    def __init__(self, levels_itemset, num_transactions):
        self.levels_itemset = levels_itemset #frequent itemsets with their support counts
        self.num_transactions = num_transactions

    def generate_rules(self, confidence_threshold):
        #TODO: This function generates the association rules from the frequent itemsets and returns the list of rules.
        # rules are of the form (X, Y, support, confidence) which means X => Y [support, confidence]
        rules = []
        for itemset in self.levels_itemset:
            if len(itemset)==1:
                continue
            subsets = []
            self.subsets(itemset, subsets, [], []) #returns all the subset rules, then check 1 by 1 to see which rules have the proper confidence
            for subset in subsets:
                if len(subset[0]) == 0 or len(subset[1]) == 0:
                    continue
                conf = self.levels_itemset[itemset]/self.levels_itemset[tuple(subset[0])]
                if conf >= confidence_threshold:
                    rules.append([subset[0], subset[1], self.levels_itemset[itemset]/self.num_transactions, conf])
        return rules
    
    def subsets(self, itemset, res, curr, rest):
        #retrun all the subsets of a frquent itemset
        if len(itemset) == 0:
            res.append([curr,rest + list(itemset)]) #add the subset and the leftover subset to res as a tuple
            return
        self.subsets(itemset[1:], res, curr, rest + [itemset[0]])
        self.subsets(itemset[1:], res, curr + [itemset[0]], rest)

    
    def quality_prune(self, rules):
        #TODO: This function prunes the misleading rules by using the lift measure and returns the updated list of rules.
        # lift(X => Y) = "confidence(X => Y) / support(Y)" or "P(X and Y) / (P(X) * P(Y))"
        newRules = []
        
        for rule in rules:
            lift = rule[3] / (self.levels_itemset[tuple(rule[1])]/self.num_transactions)
            if lift > 1:
                newRules.append(rule)

        return newRules
