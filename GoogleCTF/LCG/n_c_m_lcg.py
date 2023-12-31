import math

def calc_det(i, j, X):
    a1 = X[i] - X[0]
    b1 = X[i + 1] - X[1]
    a2 = X[j] - X[0]
    b2 = X[j + 1] - X[1]
    det = a1 * b2 - a2 * b1
    return abs(det)

def GCD(a, b):

    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b

def modInverse(a, m):
    if GCD(a, m) != 1:
        return None  #if not releatively prime no modinv
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1,
            u2 - q * v2,
            u3 - q * v3,
            v1,
            v2,
            v3,
        )
    return u1 % m

def main():
    while True:
        try:
            X = [
                211286818345627549183608678726370412218029639873054513839005340650674982169404937862395980568550063504804783328450267566224937880641772833325018028629959635,
                2166771675595184069339107365908377157701164485820981409993925279512199123418374034275465590004848135946671454084220731645099286746251308323653144363063385,
                6729272950467625456298454678219613090467254824679318993052294587570153424935267364971827277137521929202783621553421958533761123653824135472378133765236115,
                2230396903302352921484704122705539403201050490164649102182798059926343096511158288867301614648471516723052092761312105117735046752506523136197227936190287,
                4578847787736143756850823407168519112175260092601476810539830792656568747136604250146858111418705054138266193348169239751046779010474924367072989895377792,
                7578332979479086546637469036948482551151240099803812235949997147892871097982293017256475189504447955147399405791875395450814297264039908361472603256921612,
                2550420443270381003007873520763042837493244197616666667768397146110589301602119884836605418664463550865399026934848289084292975494312467018767881691302197,
            ]

            Det_X = []
            Det_X.append(calc_det(1, 2, X))
            Det_X.append(calc_det(2, 3, X))
            Det_X.append(calc_det(3, 4, X))
            Det_X.append(calc_det(4, 5, X))

            found_p = math.gcd(math.gcd(Det_X[0], Det_X[1]), math.gcd(Det_X[2], Det_X[3]))

            # To find 'a' and 'c' we need to solve the 
            mod_inv_a = modInverse((X[2] - X[3]), found_p) 
            found_a = ((X[3] - X[4]) * mod_inv_a) % found_p
            
            found_c = (X[4] - found_a * X[3]) % found_p
           
            print("n = %d\nm = %d\nc = %d\n" % (found_p, found_a, found_c))
            break
        except TypeError:
            pass

if __name__ == "__main__":
    main()
