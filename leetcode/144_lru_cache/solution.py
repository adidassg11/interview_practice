from math import inf

class LRUCache():
    def __init__(self, size):
        self.max_size = size
        self.lru_order = []  # [least_recent, ... , most_recent]
        self.key_data = {}  # {key:(val, pos_in_lru), ...}

    def __str__(self):
        ret_str = ''
        ret_str += 'LRU order: {}'.format(self.lru_order)
        ret_str += '\ndata: {}'.format(self.key_data)
        return ret_str

    def _try_get(self, key):
        # Get the return values if exists, let exception get thrown
        val, pos = self.key_data[key]

        # Update the LRU Cache
        self.lru_order.pop(pos)
        self.lru_order.append(key)

        # Update info about its position in LRU Cache
        self.key_data[key] = (val, len(self.lru_order) - 1)
        
        return val

    def get(self, key):
        try:
            return self._try_get(key)
        except KeyError:
            return -1

    def put(self, key, value):
        try:
            # If key already in cache, move to most recently used position
            existing_val = self._try_get(key)
            
            # Now just update value
            self.key_data[key] = (value, len(self.lru_order) - 1)
            
        except KeyError:
            # Key didn't exist, evict least recently used (if possible and necessary)
            # Here is where we have to worry about size limits
            if self.lru_order and len(self.lru_order) == self.max_size:
                evicted_key = self.lru_order.pop(0)
                self.key_data.pop(evicted_key)

            self.lru_order.append(key)
            self.key_data[key] = (value, len(self.lru_order) - 1)


lc = LRUCache(5)
print(lc)
print(lc.get(5))
lc.put(1,10)
print(lc)
lc.put(1,11)
print(lc)
lc.put(2,20)
print(lc)
lc.put(1,13)
print(lc)
lc.put(3,30)
print(lc)
lc.put(4,40)
print(lc)
lc.put(5,50)
print(lc)
lc.put(6,60)
print(lc)
lc.put(6,61)
print(lc)
lc.put(2,21)
print(lc)
