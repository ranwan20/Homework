def Square_root_1():
    c = 2
    i = 0
    g = 0
    for j in range(c + 1):
        if j * j > c and g == 0:
            g = j - 1
    while abs(g * g - c) > 0.0001:
        g += 0.00001
    print("%.5f"%(g))

def Square_root_2():
    c = 2
    m_max = c
    m_min = 0
    g = (m_min + m_min)/2
    while abs(g * g - c) > 0.00000000001:
        if(g * g < c):
            m_min = g
        else:
            m_max = g
        g = (m_min + m_max)/2
    print("%.13f"%(g))

def Square_root_3():
    c = 2
    g = c/2
    while abs(g * g - c) > 0.00000000001:
        g = (g + c/g)/2
    print("%.13f"%(g))

Square_root_1()
Square_root_2()
Square_root_3()