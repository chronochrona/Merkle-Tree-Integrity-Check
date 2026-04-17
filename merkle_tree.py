import hashlib

def get_file_hash(filename):
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        content = f.read()
        hasher.update(content)
    return hasher.hexdigest()

def compute_top_hash(files):
    current_layer = []
    for f in files:
        current_layer.append(get_file_hash(f))
    
    while len(current_layer) > 1:
        next_layer = []
        
        if len(current_layer) % 2 != 0:
            current_layer.append(current_layer[-1])
            
        for i in range(0, len(current_layer), 2):
            combined_string = current_layer[i] + current_layer[i+1]
            # Hash the combined pair
            new_hash = hashlib.sha1(combined_string.encode()).hexdigest()
            next_layer.append(new_hash)
            
        current_layer = next_layer
        
    return current_layer[0]

filenames = ["test1.txt", "test2.txt", "test3.txt", "test4.txt"]

for name in filenames:
    with open(name, "w") as f: f.write("Initial data for " + name)
original_hash = compute_top_hash(filenames)
print("Original Top Hash:", original_hash)
print("\nModifying test2.txt...")
with open("test2.txt", "w") as f: f.write("Modified data!")
new_hash = compute_top_hash(filenames)
print("New Top Hash:     ", new_hash)
equality = original_hash == new_hash
if equality:
    print("The original and new hash are the same")
else:
    print("The original and new hash are NOT the same")
