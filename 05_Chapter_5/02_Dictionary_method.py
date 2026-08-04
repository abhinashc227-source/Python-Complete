a = {
    "Name" : "Abhinash",
      "marks":100,
      "Age": 20,
      "Code": 100

}

print(a.items())
print(a.keys())
print(a.update({"Age":"Abhi"}))
print(a)
print(a.get("Name"))    # So in the output gave none
print(a["Name"])        # where this output will be give error this difference between both
print(a.pop("Age"))
