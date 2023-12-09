global vetorMagico
vetorMagico = [122, 77, 153, 59, 173, 107, 19, 104, 123, 183, 75, 10,
114, 236, 106, 83, 117, 16, 189, 211, 51, 231, 143, 118, 248, 148, 218,
245, 24, 61, 66, 73, 205, 185, 134, 215, 35, 213, 41, 0, 174, 240, 177,
195, 193, 39, 50, 138, 161, 151, 89, 38, 176, 45, 42, 27, 159, 225, 36,
64, 133, 168, 22, 247, 52, 216, 142, 100, 207, 234, 125, 229, 175, 79,
220, 156, 91, 110, 30, 147, 95, 191, 96, 78, 34, 251, 255, 181, 33, 221,
139, 119, 197, 63, 40, 121, 204, 4, 246, 109, 88, 146, 102, 235, 223,
214, 92, 224, 242, 170, 243, 154, 101, 239, 190, 15, 249, 203, 162, 164,
199, 113, 179, 8, 90, 141, 62, 171, 232, 163, 26, 67, 167, 222, 86, 87,
71, 11, 226, 165, 209, 144, 94, 20, 219, 53, 49, 21, 160, 115, 145, 17,
187, 244, 13, 29, 25, 57, 217, 194, 74, 200, 23, 182, 238, 128, 103,
140, 56, 252, 12, 135, 178, 152, 84, 111, 126, 47, 132, 99, 105, 237,
186, 37, 130, 72, 210, 157, 184, 3, 1, 44, 69, 172, 65, 7, 198, 206,
212, 166, 98, 192, 28, 5, 155, 136, 241, 208, 131, 124, 80, 116, 127,
202, 201, 58, 149, 108, 97, 60, 48, 14, 93, 81, 158, 137, 2, 227, 253,
68, 43, 120, 228, 169, 112, 54, 250, 129, 46, 188, 196, 85, 150, 6, 254,
180, 233, 230, 31, 76, 55, 18, 9, 32, 82, 70]

def passoUm(s): # funcionando
  saidaPassoUm = []
  for i in range(len(s)):
    saidaPassoUm.append(ord(s[i]))
  for i in range(16 - len(s)%16):
    saidaPassoUm.append(16 - len(s)%16)
  n = len(saidaPassoUm)//16
  return saidaPassoUm, n

def passoDois(saidaPassoUm, n): # funcionando
  novoBloco = [0] * 16
  novoValor = 0
  for i in range(n):
    for j in range(16):
      novoValor = vetorMagico[(saidaPassoUm[i*16 + j]) ^ novoValor] ^ novoBloco[j]
      novoBloco[j] = novoValor
  saidaPassoDois = saidaPassoUm + novoBloco
  return saidaPassoDois

def passoTres(saidaPassoDois, n): # funcionando
  saidaPassoTres = [0] * 48
  for i in range(n+1):
    for j in range(16):
      saidaPassoTres[16+j] = saidaPassoDois[i*16 + j]
      saidaPassoTres[2*16+j] = saidaPassoTres[16+j] ^ saidaPassoTres[j]
    temp = 0
    for j in range(18):
      for k in range(48):
        temp = saidaPassoTres[k] ^ vetorMagico[temp]
        saidaPassoTres[k] = temp
      temp = (temp + j) % 256
  return saidaPassoTres

def passoQuatro(saidaPassoTres): # funcionando
  saidaPassoQuatro = ''
  for i in range(16):
    saidaPassoQuatro += hex(saidaPassoTres[i])[2:]
  return saidaPassoQuatro

def hash(s): # funcionando
  saidaPassoUm, n  = passoUm(s)
  saidaPassoDois = passoDois(saidaPassoUm, n)
  saidaPassoTres = passoTres(saidaPassoDois, n)
  saidaPassoQuatro = passoQuatro(saidaPassoTres)
  return saidaPassoQuatro

def main():
  #s = input()
  s = "Ola mundo!"

  # saidaPassoUm, n  = passoUm(s)
  # print("Saída do passo 1: ", saidaPassoUm)
  # saidaPassoDois = passoDois(saidaPassoUm, n)
  # print("Saída do passo 2: ", saidaPassoDois, n)
  # saidaPassoTres = passoTres(saidaPassoDois, n)
  # print("Saída do passo 3: ", saidaPassoTres)
  # saidaPassoQuatro = passoQuatro(saidaPassoTres)
  # print("Saída do passo 4: ", saidaPassoQuatro)

  # print("----------------------------------")

  # print("Saída do hash: ", hash(s))
  print(hash(s))

if __name__ == '__main__':
  main()