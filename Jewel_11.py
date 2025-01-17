# Dictonaries:
band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}
band2 = dict(vocals = "Plant", guitar = "Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items:
print(band["vocals"])
print(band["guitar"])
print(band.get("vocals"))
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values:
print(band.values())

# List of key/value pairs as tuples:
print(band.items())

# Verify a key exists or not:
print("guitar" in band)
print("triangle" in band)

# Change Values:
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem()) # Tuple
print(band)

# Delete and Clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy Dictonaries:
#band2 = band #create a reference
#print("Bad copy!")
#print(band2)
#print(band)

#band2["drums"] = "Dave"
#print(band)

band2 = band.copy()
band2 ["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function:
band3 = dict(band)
print("Good copy!")
print(band3)

