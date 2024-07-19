
def profitable(d1, d2):
    area = d1 * d2
    invest = area > 1000
    return invest

x = profitable(20, 10)
print(x)