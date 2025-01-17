# Nested dictonaries:
band = {
    "vocals" : "Coverdale",
    "guitar" : "Page"
}

member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}
member2 = {
    "name" : "Page",
    "instrument" : "guitar"
}
band = {
    "member1" : member1,
    "member2" : member2
}
print(band)
print(band["member1"]["name"])
print(band["member2"]["name"])
print(band["member1"]["instrument"])
print(band["member2"]["instrument"])
