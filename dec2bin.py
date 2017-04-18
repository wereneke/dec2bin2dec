def bin_to_dec(a):
    b = str(a)
    dec = 0
    for power in range(len(b)):
       dec += int(b[-1-power])*2**power
    return dec

def dec_to_bin(a):
    power = []
    binar = []
    while a > 0:
        m = 0
        i = 0
        while m <= a:   #badam najwyzsza potege 2 mniejsza od a
            m = 2**i
            i += 1      
        a -= m/2
        power +=[i-2]    #tworze liste z potegami 2 ktore sumuja sie do a
    
    len_of_bin_number = power[0] + 1
    for i in range(len_of_bin_number): #robie liste zer dlugosci liczby dwojkowej
        binar += ['0']
    for i in power:                    #wstawiam 1 w odpowiednie miejsca
        binar[i] = '1'
    binar = ''.join(binar)
    return binar

def check(a):      #sprawdzam czy liczba rzeczywiście składa się z 0 i 1
    a = str(a)
    for l in a:
        if l != '0' and l != '1':
            return False
    return True



print('***Hello in decimal to binarual and reverse converter***')
print('to get conversion done enter the number and actual system after space\n')

while True:
    string_num = input()
    list_num = string_num.split(sep = ' ')
    
    try:
        num = int(list_num[0])
        system = int(list_num[1])
        if system == 2 or system == 10:        # CO JEZELI POJDZIE 5 2 ?????????????????????????????????? 
            break
        else:
            print('The number must be integer and system can only be 2 or 10')
    except Exception as e:
        print('Try like this\n101 2\nor\n5 10\n')

if system == 10:
    result = dec_to_bin(num)
    print('decimal %d equals to binarual %s' %(num, result))
else:
    while not check(num):
        num = input('number must consist onlu 0\'s ans 1\'s, enter it')
    num = int(num)
    result = bin_to_dec(num)
    print('binarual %d equals to decimal %s' %(num, result))