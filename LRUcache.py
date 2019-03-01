/*Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

*/


class LRUCache(dict):
	def __init__(self, cap):
		self.remaining = cap
		
	def get(self, key):
		if key not in self:
			return -1
		val = self.pop(key) # pop and re-insert to keep the order
		self[key] = val
		return val
		
	def put(self, key, value):
		if key in self:
			self.pop(key)
		else:
			if self.remaining > 0: self.remaining -= 1
			else: self.pop(next(iter(self))) # cache is full, remove least recently used key which is the first key 
		self[key] = value
