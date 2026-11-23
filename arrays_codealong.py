'''
codes = ["abc123", "xyz789", "q1w2e3"]
codes.remove("xyz789")
print(codes)

target = "nope"
if target in codes:
    codes.remove(target)
else:
    print(target, "not found, nothing removed")

a = [1,2,3]
b= a
b.append(912)
print('a:' , a)
print('b:',b)

print("--- step 4 ---")
c = [1, 2, 3]
d = c.copy()
d.append(99)
print("c:", c)
print("d:", d)
print("same list?", c is d)
print("b same as a?", a is b)
'''
'''
print("--- step 7 ---")
def with_new_code(lst):
    result = lst.copy()
    result.append("new")
    return result


print("original:", original)
print("updated:", updated)
'''

print("--- step 9 ---")
grid = [[0] * 3] * 3
print("before:", grid)

grid[0][0] = 5
print("after:", grid)