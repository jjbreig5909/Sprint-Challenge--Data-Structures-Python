import time

############ Adding Binary Search Tree #############
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if self.value is None:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            elif target == self.left:
                return True
            else:
                return self.left.contains(target)
        if target >= self.value:
            if self.right is None: 
                return False
            elif target == self.right:
                return True
            else:
                return self.right.contains(target)

########### Done ending Binary Search Tree ###########

start_time = time.time()

f = open('names\list_names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names\list_names_2.txt", 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

new_tree = BSTNode(names_1[0])
for name_1 in names_1:
    new_tree.insert(name_1)

for name_2 in names_2:
        if new_tree.contains(name_2):
            duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

### Attempting Stretch Goal! ###

start_time = time.time()

f = open('names\list_names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names\list_names_2.txt", 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
set_names_1 = set(names_1)
set_names_2 = set(names_2)
# Replace the nested for loops below with your improvements
duplicates = set_names_1.intersection(set_names_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

