import numpy as np

# demonstrate the cauchy-schwartz inequality and show the condition for equality
# c-s inequality -> dot(a,b) <= norm(a)norm(b)

# I will generate two random vectors of the same length at each run of the program and show the inequlaity is true
v1 = np.random.randn(3)
v2 = np.random.randn(3)

print("v1 = ", v1, "v2 = ", v2)
dot = abs(np.dot(v1, v2))
n_ab = np.linalg.norm(v1) * np.linalg.norm(v2)

print("absolute value of dot product of v1 and v2 = ", dot)
print("norm of v1 * norm of v2 = ", n_ab)
if (dot <= n_ab):
    print("abs(dot(v1, v2)) <= norm(v1)*norm(v2)")
else:
    print("code must be wrong bc the inequality must always be true")

print(
    "the case for equality would be that the cosine of angle between the two vectors is 1 or -1, in other words: theta is 0 or pi radians")

# finding a set of pairs of vectors for which the equality is true
# someequalityvecs = [ [x = np.random.randint(20, size = 3), y = np.random.randint(20, size = 3)] for i in range(100) if (abs(np.dot(x, y)) <= np.linalg.norm(x)* np.linalg.norm(y))]
# someequalityvecs = [[a,b,c], [x,y,z]]
