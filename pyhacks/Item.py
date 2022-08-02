class Item:
    def __init__(self, item, counter):
        if type(item) == str:
            self.item = {"counter": counter, "content": item}
        elif type(item) == dict:
            item["counter"] = counter
            self.item = item
        else:
            raise Exception("item is not str or dict")
    
    def __str__(self):
        return str(self.item)

    def verify_key(self, key_name):
        if type(key_name)!=str:
            raise Exception(f"Key type excpected to be str but got {type(key_name)}")
        if key_name in self.item:
            return True
        else:
            raise Exception(f"Key {key_name} doesn't exist in item: {self.item}")

    def verify_keys(self, keys):
        if type(keys)!=list:
            raise Exception(f"Keys type excpected to be list but got {type(keys)}")
        for key in keys:
            self.verify_key(key)
        return True
        
    def has_key(self, key_name):
        return key_name in self.item

    def get(self, key_name):
        return self.item.get(key_name)
    
    def keys(self):
        return self.item.keys()
    
    def set(self, key_name, value):
        self.item[key_name] = value

        