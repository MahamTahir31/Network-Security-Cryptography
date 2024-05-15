def circularbyteleftshift(w, b):
    if(b == 1):
        w = [w[1], w[2], w[3], w[0]]
    elif(b == 2):
        w = [w[2], w[3], w[0], w[1]]
    elif(b == 3):
        w = [w[3], w[0], w[1], w[2]]
    return w

def roundconstant(i):
    if (i == 1):
        return "01"
    elif (i == 2):
        return "02"
    elif (i == 3):
        return "04"
    elif (i == 4):
        return "08"
    elif (i == 5):
        return "10"
    elif (i == 6):
        return "20"
    elif (i == 7):
        return "40"
    elif (i == 8):
        return "80"
    elif (i == 9):
        return "1B"
    elif (i == 10):
        return "36"

def sbox(w):
    box = [[ '63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'], ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'], ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'], ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'], ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'], ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'], ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'], ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'], ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'], ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'], ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'], ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'], ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'], ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'], ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'], ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]
    return [box[int(w[0][0], 16)][int(w[0][1], 16)], box[int(w[1][0], 16)][int(w[1][1], 16)], box[int(w[2][0], 16)][int(w[2][1], 16)], box[int(w[3][0], 16)][int(w[3][1], 16)]]

def addRoundconstants(w, r):
    return format(int(w, 16) ^ int(roundconstant(r), 16), 'x').upper()
                                
def keyschedule(khext, r):
    w = []
    w.append([khext[0]+khext[1], khext[2]+khext[3], khext[4]+khext[5], khext[6]+khext[7]])
    w.append([khext[8]+khext[9], khext[10]+khext[11], khext[12]+khext[13], khext[14]+khext[15]])
    w.append([khext[16]+khext[17], khext[18]+khext[19], khext[20]+khext[21], khext[22]+khext[23]])
    w.append([khext[24]+khext[25], khext[26]+khext[27], khext[28]+khext[29], khext[30]+khext[31]])
    gf = circularbyteleftshift(w[3], 1)
    gf = sbox(gf)
    gf = [addRoundconstants(gf[0], r), gf[1], gf[2], gf[3]]
    w.append([format(int(w[0][0], 16) ^ int(gf[0], 16), 'x').upper(), format(int(w[0][1], 16) ^ int(gf[1], 16), 'x').upper(), format(int(w[0][2], 16) ^ int(gf[2], 16), 'x').upper(), format(int(w[0][3], 16) ^ int(gf[3], 16), 'x').upper()])
    w.append([format(int(w[4][0], 16) ^ int(w[1][0], 16), 'x').upper(), format(int(w[4][1], 16) ^ int(w[1][1], 16), 'x').upper(), format(int(w[4][2], 16) ^ int(w[1][2], 16), 'x').upper(), format(int(w[4][3], 16) ^ int(w[1][3], 16), 'x').upper()])
    w.append([format(int(w[5][0], 16) ^ int(w[2][0], 16), 'x').upper(), format(int(w[5][1], 16) ^ int(w[2][1], 16), 'x').upper(), format(int(w[5][2], 16) ^ int(w[2][2], 16), 'x').upper(), format(int(w[5][3], 16) ^ int(w[2][3], 16), 'x').upper()])
    w.append([format(int(w[6][0], 16) ^ int(w[3][0], 16), 'x').upper(), format(int(w[6][1], 16) ^ int(w[3][1], 16), 'x').upper(), format(int(w[6][2], 16) ^ int(w[3][2], 16), 'x').upper(), format(int(w[6][3], 16) ^ int(w[3][3], 16), 'x').upper()])
    for i in range(4, 8):
        for j in range(0,4):
            if (len(w[i][j]) != 2):
                w[i][j] = "0"+w[i][j][0]
    return (w[4][0][0] + w[4][0][1] + w[4][1][0] + w[4][1][1] + w[4][2][0] + w[4][2][1] + w[4][3][0] + w[4][3][1] + w[5][0][0] + w[5][0][1] + w[5][1][0] + w[5][1][1] + w[5][2][0] + w[5][2][1] + w[5][3][0] + w[5][3][1] + w[6][0][0] + w[6][0][1] + w[6][1][0] + w[6][1][1] + w[6][2][0] + w[6][2][1] + w[6][3][0] + w[6][3][1] + w[7][0][0] + w[7][0][1] + w[7][1][0] + w[7][1][1] + w[7][2][0] + w[7][2][1] + w[7][3][0] + w[7][3][1])

def addroundkey(k, m):
    w = []
    w.append([k[0]+k[1], k[2]+k[3], k[4]+k[5], k[6]+k[7]])
    w.append([k[8]+k[9], k[10]+k[11], k[12]+k[13], k[14]+k[15]])
    w.append([k[16]+k[17], k[18]+k[19], k[20]+k[21], k[22]+k[23]])
    w.append([k[24]+k[25], k[26]+k[27], k[28]+k[29], k[30]+k[31]])

    x = []
    x.append([m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]])
    x.append([m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]])
    x.append([m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]])
    x.append([m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]])
    
    return (format(int(w[0][0][0], 16) ^ int(x[0][0][0], 16), 'x') + format(int(w[0][0][1], 16) ^ int(x[0][0][1], 16), 'x') + format(int(w[0][1][0], 16) ^ int(x[0][1][0], 16), 'x') + format(int(w[0][1][1], 16) ^ int(x[0][1][1], 16), 'x') + format(int(w[0][2][0], 16) ^ int(x[0][2][0], 16), 'x') + format(int(w[0][2][1], 16) ^ int(x[0][2][1], 16), 'x') + format(int(w[0][3][0], 16) ^ int(x[0][3][0], 16), 'x') + format(int(w[0][3][1], 16) ^ int(x[0][3][1], 16), 'x') + format(int(w[1][0][0], 16) ^ int(x[1][0][0], 16), 'x') + format(int(w[1][0][1], 16) ^ int(x[1][0][1], 16), 'x') + format(int(w[1][1][0], 16) ^ int(x[1][1][0], 16), 'x') + format(int(w[1][1][1], 16) ^ int(x[1][1][1], 16), 'x') + format(int(w[1][2][0], 16) ^ int(x[1][2][0], 16), 'x') + format(int(w[1][2][1], 16) ^ int(x[1][2][1], 16), 'x') + format(int(w[1][3][0], 16) ^ int(x[1][3][0], 16), 'x') + format(int(w[1][3][1], 16) ^ int(x[1][3][1], 16), 'x') + format(int(w[2][0][0], 16) ^ int(x[2][0][0], 16), 'x') + format(int(w[2][0][1], 16) ^ int(x[2][0][1], 16), 'x') + format(int(w[2][1][0], 16) ^ int(x[2][1][0], 16), 'x') + format(int(w[2][1][1], 16) ^ int(x[2][1][1], 16), 'x') + format(int(w[2][2][0], 16) ^ int(x[2][2][0], 16), 'x') + format(int(w[2][2][1], 16) ^ int(x[2][2][1], 16), 'x') + format(int(w[2][3][0], 16) ^ int(x[2][3][0], 16), 'x') + format(int(w[2][3][1], 16) ^ int(x[2][3][1], 16), 'x') + format(int(w[3][0][0], 16) ^ int(x[3][0][0], 16), 'x') + format(int(w[3][0][1], 16) ^ int(x[3][0][1], 16), 'x') + format(int(w[3][1][0], 16) ^ int(x[3][1][0], 16), 'x') + format(int(w[3][1][1], 16) ^ int(x[3][1][1], 16), 'x') + format(int(w[3][2][0], 16) ^ int(x[3][2][0], 16), 'x') + format(int(w[3][2][1], 16) ^ int(x[3][2][1], 16), 'x') + format(int(w[3][3][0], 16) ^ int(x[3][3][0], 16), 'x') + format(int(w[3][3][1], 16) ^ int(x[3][3][1], 16), 'x')).upper()

def sboxmatrix(m):
    w = []
    w.append(sbox([m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]]))
    w.append(sbox([m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]]))
    w.append(sbox([m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]]))
    w.append(sbox([m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]]))
    return (w[0][0] + w[0][1] + w[0][2] + w[0][3] + w[1][0] + w[1][1] + w[1][2] + w[1][3] + w[2][0] + w[2][1] + w[2][2] + w[2][3] + w[3][0] + w[3][1] + w[3][2] + w[3][3])

def shiftrow(m):
    w = []
    w.append([m[0]+m[1], m[8]+m[9], m[16]+m[17], m[24]+m[25]])
    w.append(circularbyteleftshift([m[2]+m[3], m[10]+m[11], m[18]+m[19], m[26]+m[27]], 1))
    w.append(circularbyteleftshift([m[4]+m[5], m[12]+m[13], m[20]+m[21], m[28]+m[29]], 2))
    w.append(circularbyteleftshift([m[6]+m[7], m[14]+m[15], m[22]+m[23], m[30]+m[31]], 3))
    return (w[0][0] + w[1][0] + w[2][0] + w[3][0] + w[0][1] + w[1][1] + w[2][1] + w[3][1] + w[0][2] + w[1][2] + w[2][2] + w[3][2] + w[0][3] + w[1][3] + w[2][3] + w[3][3])

def mult(s, m):
    w = []
    for i in range(0, 4):
        if(s[i] == "03"):
            if(2*int(m[i], 16) > 255):
                mbin = bin(2*int(m[i], 16))[2:].zfill(8)[-8:]
                w.append(format((int(mbin, 2)^27) ^ int(m[i], 16), 'x'))
            else:
                w.append(format(2*int(m[i], 16) ^ int(m[i], 16), 'x'))
        elif(s[i] == "02"):
            if(2*int(m[i], 16) > 255):
                mbin = bin(2*int(m[i], 16))[2:].zfill(8)[-8:]
                w.append(format(int(mbin, 2)^27, 'x'))
            else:
                w.append(format(2*int(m[i], 16), 'x'))
        elif(s[i] == "01"):
            w.append(m[i])
    r = format(int(w[0], 16) ^ int(w[1], 16) ^ int(w[2], 16) ^ int(w[3], 16), 'x').upper()
    if (len(r) != 2):
        return ("0"+r)
    else:
        return r

def mixcolumn(m):
    w = []
    w.append([mult(["02", "03", "01", "01"], [m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]]), mult(["02", "03", "01", "01"], [m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]]), mult(["02", "03", "01", "01"], [m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]]), mult(["02", "03", "01", "01"], [m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]])])
    w.append([mult(["01", "02", "03", "01"], [m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]]), mult(["01", "02", "03", "01"], [m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]]), mult(["01", "02", "03", "01"], [m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]]), mult(["01", "02", "03", "01"], [m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]])])
    w.append([mult(["01", "01", "02", "03"], [m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]]), mult(["01", "01", "02", "03"], [m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]]), mult(["01", "01", "02", "03"], [m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]]), mult(["01", "01", "02", "03"], [m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]])])
    w.append([mult(["03", "01", "01", "02"], [m[0]+m[1], m[2]+m[3], m[4]+m[5], m[6]+m[7]]), mult(["03", "01", "01", "02"], [m[8]+m[9], m[10]+m[11], m[12]+m[13], m[14]+m[15]]), mult(["03", "01", "01", "02"], [m[16]+m[17], m[18]+m[19], m[20]+m[21], m[22]+m[23]]), mult(["03", "01", "01", "02"], [m[24]+m[25], m[26]+m[27], m[28]+m[29], m[30]+m[31]])])

    return (w[0][0] + w[1][0] + w[2][0] + w[3][0] + w[0][1] + w[1][1] + w[2][1] + w[3][1] + w[0][2] + w[1][2] + w[2][2] + w[3][2] + w[0][3] + w[1][3] + w[2][3] + w[3][3])

def main():
    ptext = input('[*] Enter plaintext message (128 bits | 16 length): ').encode('utf-8')
    ktext = input('[*] Enter encryption key (128 bits | 16 length): ').encode('utf-8')
    # ptext = "Two One Nine Two".encode('utf-8')
    # ktext = "Thats my Kung Fu".encode('utf-8')

    if(len(ptext) == 16 and len(ktext) == 16):
        phext = ptext.hex().upper()
        khext = ktext.hex().upper()
        print("[*] Encryption KEY (in hex): %s" % khext)
        print("[*] Plain text MSG (in hex): %s" % phext)
        k = []
        k.append(khext)
        print("RoundKey [0]: %s" % k[0])
        for x in range(0, 10):
            k.append(keyschedule(k[x], x+1))
            print("RoundKey [%d]: %s" % (x+1, k[x+1]))

        m = []
        m.append(phext)
        print("Encipher Round [0]")
        m.append(addroundkey(k[0], m[0]))
        print("Add RoundKey: %s" % m[1])
        x = 1
        mx = 1
        while(mx <= 10):
            print("Encipher Round [%d]" % (mx))
            m.append(sboxmatrix(m[x]))
            x += 1
            print("Substitute Byte: %s" % m[x])
            m.append(shiftrow(m[x]))
            x += 1
            print("Shift Row: %s" % m[x])
            if(mx != 10):
                m.append(mixcolumn(m[x]))
                x += 1
                print("Mix Column: %s" % m[x])
            m.append(addroundkey(k[mx], m[x]))
            x += 1
            print("Add RoundKey: %s" % m[x])
            mx += 1

        print("[*] Cipher text MSG (in hex): %s" % m[x])
    else:
        print('Error: Plaintext message is not 128 bits | 16 length.')

if _name_ == "_main_":
    main()