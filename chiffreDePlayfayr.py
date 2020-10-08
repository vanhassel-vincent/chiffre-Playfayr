from math import *

#azertyuiopqsdfghjklmxcvbn
#zertpaiopysdfgmqklmhcvbnxc

#mon_fichier = open("cle2", "w")
#mon_fichier1 = open("chiffre2", "w")

def texte(a):
    a = a.replace('w','v')
    a = a.replace('?',"")
    a = a.replace('!',"")
    a = a.replace(',',"")
    a = a.replace('é',"e")
    a = a.replace('à',"a")
    a = a.replace('ç',"c")
    a = a.replace('è',"e")
    a = a.replace('ë',"e")
    a = a.replace('ô',"e")
    a = a.replace(" ","")
    a = a.replace('-',"")
    a = a.replace("_","")
    a = a.replace("'","")
    a = a.replace("ù","u")
    a = a.replace("<","")
    a = a.replace(">","")
    a = a.replace("(","")
    a = a.replace(")","")
    a = a.replace("/","")
    a = a.replace(".","")
    a = a.replace('œ',"oe")
    a = a.replace('’',"")
    a = a.replace("«","")
    a = a.replace("»","")
    a = a.lower()
    return(a)

def double(a):
    b = ""
    for f in range(len(a)):
        if a[f] == a[f-1]:
            b += 'x'+ a[f]
        else :
            b += a[f]
    return b

def parite(a):
    if len(a) % 2 == 1:
        a = a + 'x'
        return a
    else :
       return a

def clef():
    global h, a
    a = input("saisir 25 lettres de l'alphabet differentes sans w :")
    #a = mon_fichier
    a = texte(a)
    c = list(a)
    table = c[0:5], c[5:10], c[10:15], c[15:20], c[20:25]
    h = c
    return table

def afficher_tableau(plateau):
    for ligne in plateau:
        for d in ligne:
            print(d, end=' ')
        print("\n")

def position_clair(plateau):
    ligne1 = 0
    ligne2 = 0
    colonne1 = 0
    colonne2 =0
    global e, h
    z = e
    r = list(z)
    for g in range(0, 25):
        if h[g] == r[1]:
            ligne1 = floor(g / 5)
    for g in range(0, 25):
        if h[g] == r[0]:
            colonne1 = (g % 5)
    for g in range(0, 25):
        if h[g] == r[0]:
            ligne2 = floor(g / 5)
    for g in range(0, 25):
        if h[g] == r[1]:
            colonne2 = (g % 5)
    if colonne1 == colonne2:
        if ligne1 == 4:
            print(plateau[ligne1+1][colonne2] + plateau[0][colonne1], end='')
        elif ligne2 == 4:
            print(plateau[0][colonne2] + plateau[ligne2+1][colonne1], end='')
        else :
            print(plateau[ligne1+1][colonne1] + plateau[ligne2+1][colonne2], end='')

    elif ligne1 == ligne2:
        if colonne1 == 4:
            print(plateau[ligne1][0] + plateau[ligne2][colonne2+1], end='')
        elif colonne2 == 4:
            print(plateau[ligne1][colonne1+1] + plateau[ligne2][0], end='')
        else :
            print(plateau[ligne1][colonne1+1] + plateau[ligne2][colonne2+1], end='')

    else :
        print(plateau[ligne1][colonne1] + plateau[ligne2][colonne2], end='')

def chiffrement(plateau):
    global e, h
    z = 0
    m = input("saisir texte a chiffree :")
    m = texte(m)
    m = double(m)
    m = parite(m)
    while z < len(m):
        e = m[z]+m[z+1]
        position_clair(plateau)
        z += 2

def position_chiffre(plateau):
    ligne1 = 0
    ligne2 = 0
    colonne1 = 0
    colonne2 =0
    global n, h
    p = n
    s = list(p)
    for g in range(0, 25):
        if h[g] == s[1]:
            ligne1 = floor(g / 5)
    for g in range(0, 25):
        if h[g] == s[0]:
            colonne1 = (g % 5)
    for g in range(0, 25):
        if h[g] == s[0]:
            ligne2 = floor(g / 5)
    for g in range(0, 25):
        if h[g] == s[1]:
            colonne2 = (g % 5)
    if colonne1 == colonne2:
        if ligne1 == 0:
            print(plateau[ligne2-1][colonne2] + plateau[4][colonne1], end='')
        elif ligne2 == 0:
            print(plateau[4][colonne2] + plateau[ligne1-1][colonne1], end='')
        else :
            print(plateau[ligne2-1][colonne2] + plateau[ligne1-1][colonne1], end='')

    elif ligne1 == ligne2:
        if colonne1 == 0:
            print(plateau[ligne2][colonne2-1] + plateau[ligne1][4], end='')
        elif colonne2 == 0:
            print(plateau[ligne1][colonne2-1] + plateau[ligne2][4], end='')
        else :
            print(plateau[ligne2][colonne2-1] + plateau[ligne1][colonne1-1], end='')

    else :
        print(plateau[ligne2][colonne2] + plateau[ligne1][colonne1], end='')

def dechiffrement(plateau):
    global n
    z = 0
    ok = input("saisir texte a dechiffree :")
    #ok = mon_fichier1
    o = texte(ok)
    while z < len(o):
        n = o[z]+o[z+1]
        position_chiffre(plateau)
        z += 2

def main():
    v = input("voulez vous chiffrer un texte ? (oui/non) :")
    if v == 'oui' or v == '':
        plateau = clef()
        afficher_tableau(plateau)
        chiffrement(plateau)
    else :
        w = input("voulez vous dechiffrer un texte ? (oui/non) :")
        if w == 'oui' or v == '':
            plateau = clef()
            afficher_tableau(plateau)
            dechiffrement(plateau)
        else :
            return False

main()