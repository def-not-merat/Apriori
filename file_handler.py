import csv

class FileHandlingTools(object):
    def __init__(self, path_to_transactions_file, path_to_name_mapping_file):
        self.path_to_transactions_file = path_to_transactions_file
        self.path_to_name_mapping_file = path_to_name_mapping_file
        
    def load_transactions(self):
        #TODO: This fucntion reads the transactions from the csv file and returns a list of transactions
        transactions = []
        with open(self.path_to_transactions_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row = list(dict.fromkeys(row))
                row.sort()
                row = [int(i) for i in row]
                transactions.append(row)
        return transactions

    def id_to_name(self, id):
        #TODO: This function returns the name of the item given its id which is read from the mapping file.
        with open(self.path_to_name_mapping_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    return row[1]
        return None