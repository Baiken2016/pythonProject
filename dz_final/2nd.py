from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cached_dict = OrderedDict()

    @property
    def cache(self):
        if self.key in self.cached_dict:
            return self.cached_dict.move_to_end(self.key, last=True)

        return self.cached_dict

    @cache.setter
    def cache(self, new):
        if len(self.cached_dict) >= self.capacity:
            self.cached_dict.popitem(last=False)

        self.cached_dict[new[0]] = new[1]

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cached_dict.items():
            print(f"{key} : {value}")

    def get(self, key):
        return self.cached_dict.get(key)


cache = LRUCache(6)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.cache = ("key4", "value4")
cache.cache = ("key5", "value5")
cache.cache = ("key6", "value6")
cache.print_cache()
cache.get("key2")
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key7", "value7")
cache.print_cache()
