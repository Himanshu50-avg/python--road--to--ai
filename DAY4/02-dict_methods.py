marks={'amit':20,'himank':66}

# 1.items
print(marks.items())
# 2.keys()
print(marks.keys())
# 3.values()
print(marks.values())
# 4.update
marks.update({"amit":26})
print(marks)
# 5.get()
print(marks.get("amit"))
# 6.pop()
print(marks.pop("himank"))
# 7.pop.items()
print(marks.popitem())
# 7.clear(
marks.clear()
print(marks)
