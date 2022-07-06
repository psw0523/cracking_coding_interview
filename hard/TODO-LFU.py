'''
Problem
Asked by Google.

Impelement an LFU(Least Frequently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods.
- set(key, value)
sets key to value. If there are already n items in the cache and we are adding a new item,
then it should also remove the least frequently used item.
If there is a tie, the the least recently used key should be removed.
- get(key)
gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

'''
Solution

Use priority queue(binary heap) for maintaining least freq/recent tree

class LFUObject
  key
  value,
  freq
  next
  prev
  incFreq()

class HashTable
  add(LFUObject)
  remove(LFUObject)
  removeLeastFreq()

N 5

set(1, A)
  lfuObject = LFUObject(1, A, 1, least)
  map[1] = lfuObject
  hashTable.add(lfuObject)
set(2, B)
set(3, C)
get(1)
set(4, D)
get(2)
  lfuObject = map[2]
  hashTable.remove(lfuObject)
      lfuObject.prev.next = lfuObject.next
      lfuObject.next.prev = lfuObject.prev
  lfuObject.incFreq()
  hashTable.add(lfuObject)
  return lfuObject
set(5, E)
set(6, F)
  hashTable.removeLeastFreq()
    => C removed



1 F->E->D
2 B->A


class Cache(N)

N
least = 0
HashTable hashTable

set(key, value):
   if len(cache) > N:
      hashTable.remove()
       

get(key):

'''
class LFUOjbect:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = None
        self.prev = None

    def incFreq(self):
        self.freq += 1

    def link(self, new):
        if self.next != None:
            self.next.prev = new
        new.next = self.next
        self.next = new 
        new.prev = self

    def unlink(self):
        if self.prev != None:
            self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

    def __repr__(self):
        print("key", key, "value", value)

# TODO DoubleLinkedList needed

# TODO use DoubleLinkedList as value of map
class HashTable():
    def __init__(self):
        self.map = dict()

    def add(self, lfu):
        if lfu.freq in self.map.keys():
            head = self.map[lfu.freq]
            lfu.link(head)
        self.map[lfu.freq] = lfu

    def remove(self, lfu):
        if lfu.freq in self.map.keys():
            if lfu == self.map[lfu.freq]: # change 
                self.map[lfu.freq] = lfu.next
                if self.map[lfu.freq] == None:
                    self.map.pop()
        lfu.unlink()

    # TODO
    def removeLeastFreq(self):
        for k in self.map.keys():
            lfu = self.map[k]
            self.remove(lfu)
            return lfu

    def __repr__(self):
        for k in self.map.keys():
            lfu = self.map[k]
            print("freq", k, "====>")
            print(lfu)


class Cache():
    def __init__(self, N):
        self.hashTable = HashTable()
        self.N = N
        self.nums = 0
        self.map = dict()

    def set(key, value):
        if self.nums == self.N:
            self.hashTable.removeLeastFreq()
            self.map.pop()
        lfu = LFUObject(key, value, 1)
        self.hashTable.add(lfu)
        self.map[key] = lfu

    def get(key):
        if key in self.map.keys():
            lfu = self.map[key]
            self.hashTable.remove(lfu)
            lfu.incFreq()
            self.hashTable.add(lfu)
            return lfu.value
        else:
            return None
