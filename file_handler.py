import csv

class FileHandlingTools(object):
    def __init__(self, path_to_transactions_file, path_to_name_mapping_file):
        self.path_to_transactions_file = path_to_transactions_file
        self.path_to_name_mapping_file = path_to_name_mapping_file
        
    def load_transactions(self):
        #TODO: This fucntion reads the transactions from the csv file and returns a list of transactions
        pass

    def id_to_name(self, id):
        #TODO: This function returns the name of the item given its id which is read from the mapping file.
            pass