from itertools import combinations


class RuleGenerator(object):

    def __init__(self, levels_itemset, num_transactions):
        self.levels_itemset = levels_itemset #frequent itemsets with their support counts
        self.num_transactions = num_transactions

    def generate_rules(self, confidence_threshold):
        #TODO: This function generates the association rules from the frequent itemsets and returns the list of rules.
        # rules are of the form (X, Y, support, confidence) which means X => Y [support, confidence]
        pass
        #return rules
    
    def quality_prune(self, rules):
        #TODO: This function prunes the misleading rules by using the lift measure and returns the updated list of rules.
        # lift(X => Y) = "confidence(X => Y) / support(Y)" or "P(X and Y) / (P(X) * P(Y))"
        pass
        #return rules
