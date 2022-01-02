def barisan():
    a=int(input('a = '))
    b=int(input('b = '))
    print(f'Un = {a-b}+{b}n')
    Un=[]
    while True:
        n=int(input('n = '))
        for n in range(1,n+1,1):
            Un.append((a-b)+(b*n))
        print(Un)
        break

def rumus():
    m=[]
    i=int(input('Suku Diket = '))
    for j in range(1,1+i,1):
        suku=int(input('Suku ke = {} '.format(j)))
        m.append(suku)
    a=m[0]
    b=m[1]-m[0]
    print('Un = {} + {}n'.format(a-b,b))

def diket():
    c=int(input('U ke : '))
    d=int(input(''))
    e=int(input('U ke : '))
    f=int(input(''))
    Uken= int(input('Un = '))
    bcd=(((f)-(d))/((e-1)-(c-1)))
    awl=d-((c-1)*bcd)
    print('a = {}'.format(awl))
    print('b = {}'.format(bcd))
    g=awl+((Uken-1)*bcd)
    print(g)

def Sn(): #total
    a1=int(input('a = ')) #awal
    b1=int(input('b = ')) #beda
    n1=int(input('U ke = '))
    total=((n1/2)*(2*a1+(n1-1)*b1))
    print(total)

def geometri():
    a2=int(input('a = '))
    r=int(input('r = '))
    n2=int(input('U ke = '))
    if r < 1:
        Total = a2*((1 - (r ** n2))/(1 - r))
        print(Total)
    elif r > 1:
        Total = a2*(((r ** n2) - 1) / (r - 1))
        print(Total)


def GLBB_v0():
    vt= int(input('kecepatan akhir(m/s) = '))
    a = int(input('percepatan(m/s^2) = '))
    t= int(input('waktu(s) = '))
    v0 = vt - ( a * t )
    print(v0, 'm/s')

def GLBB_vt():
    v0 = int(input('kecepatan awal(m/s) = '))
    a = int(input('percepatan(m/s^2) = '))
    t = int(input('waktu(s) = '))
    vt = v0 + (a * t)
    print(vt, ' m/s')

def GLBB_s():
    v0 = int(input('kecepatan awal(m/s) = '))
    a = int(input('percepatan(m/s^2) = '))
    t = int(input('waktu(s) = '))
    s=((v0 * t) + (1/2 * a * t**2))
    print(s, ' m')

