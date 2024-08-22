def geometric_progression(a, r, n):
    return [a * r**i for i in range(n)]
gp = geometric_progression(2, 3, 5)  
print(gp)  
