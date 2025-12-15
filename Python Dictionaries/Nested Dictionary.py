myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# Extract the year of child3;
for key in myfamily:
    if key == "child3":
        for key1 in myfamily[key]:
            if key1 == "year":
                print(myfamily["child3"]["year"]) # this will print the value for the year.