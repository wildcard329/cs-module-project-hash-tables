"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
values = {}
results_1 = {}
results_2 = {}

def f(x):
    return x * 4 + 6

# Your code here
for num in q:
    values[f(num)] = num

def return_sumdif(s):
    a = []
    b = []
    c = [] 
    d = []
    for num in s:
        a.append(f(num))
        b.append(f(num))
        c.append(f(num))
        d.append(f(num))

    for i in range(len(a)):
        for j in range(len(b)):
            results_1[a[i] + b[j]] = (a[i], b[j])

    for i in range(len(c)):
        for j in range(len(d)):
            results_2[c[i] - c[j]] = (c[i], d[j])
    
    for key in results_1:
        for item in results_2:
            if key == item:
                results_a = results_1.get(key)[0]
                results_b = results_1.get(key)[1]
                results_c = results_2.get(key)[0]
                results_d = results_2.get(key)[1]
                print(f"f({values.get(results_a)}) + f({values.get(results_b)}) = f({values.get(results_c)}) - f({values.get(results_d)}) \t{results_a} + {results_b} = {results_c} - {results_d}")


return_sumdif(q)
