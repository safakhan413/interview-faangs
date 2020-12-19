class HashTable:

    def insert(self,hash_table, key, value):
        hash_key = hash(key) % len(hash_table)
        print(hash_key)
        key_exists = False
        bucket = hash_table[hash_key]
        for i, kv in enumerate(bucket):
            print('im kv', kv)
            k, v = kv
            if key == k:
                print(key)
                print(k)
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self,hash_table, key):
        hash_key = hash(key) % len(hash_table)
        bucket = hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def search(self,hash_table, key):
        hash_key = hash(key) % len(hash_table)
        bucket = hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self,hash_table, key):
        hash_key = hash(key) % len(hash_table)
        key_exists = False
        bucket = hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

h = HashTable()
hash_table = [[] for _ in range(10)]
print(hash_table)
h.insert(hash_table, 10, 'Nepal')
h.insert(hash_table, 25, 'USA')
h.insert(hash_table, 20, 'India')

print('search result',h.search(hash_table,25))
print (hash_table)