# can dictionary have duplicate keys? ->
# No,never. only the first key is used and value overrides/ updates.
# python will never give an error.


p = {"a": "sit", "b": "run", "c": "stand", "b": "play"}
print(p)
