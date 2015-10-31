class HashTable:
    def __init__(self, bucket_cnt=0):
        self.bucket_count = bucket_cnt
        self.htable = []
        for i in range(0, bucket_cnt):
            self.htable.append([])

    def hash_function(self, key):
        count = 0
        for letter in key:
            count+=ord(letter)
        return count % self.bucket_count

    def add_entry(self, key, value):
        hash_val = self.hash_function(key)
        bucket = self.htable[hash_val]
        bucket.append([key, value])

    def retrieve_entry(self, key):
        hash_val = self.hash_function(key)
        bucket = self.htable[hash_val]
        for entry in bucket:
            if entry[0] == key:
                return entry[1]
        return None
    
# h_table = HashTable(20)
# h_table.add_entry("dog", 7)
# h_table.add_entry("goat", 8)
#
# print(h_table.htable)
#
# print(h_table.retrieve_entry("dog"))








