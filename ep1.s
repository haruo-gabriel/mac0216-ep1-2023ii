global _start

section .data
  ENTER: equ 0x0a
  STDIN: equ 0
  STDOUT: equ 1

  INPUT_TAM_MAX: equ 100000

  vetorMagico: db 122, 77, 153, 59, 173, 107, 19, 104, 123, 183, 75, 10, 114, 236, 106, 83, 117, 16, 189, 211, 51, 231, 143, 118, 248, 148, 218, 245, 24, 61, 66, 73, 205, 185, 134, 215, 35, 213, 41, 0, 174, 240, 177, 195, 193, 39, 50, 138, 161, 151, 89, 38, 176, 45, 42, 27, 159, 225, 36, 64, 133, 168, 22, 247, 52, 216, 142, 100, 207, 234, 125, 229, 175, 79, 220, 156, 91, 110, 30, 147, 95, 191, 96, 78, 34, 251, 255, 181, 33, 221, 139, 119, 197, 63, 40, 121, 204, 4, 246, 109, 88, 146, 102, 235, 223, 214, 92, 224, 242, 170, 243, 154, 101, 239, 190, 15, 249, 203, 162, 164, 199, 113, 179, 8, 90, 141, 62, 171, 232, 163, 26, 67, 167, 222, 86, 87, 71, 11, 226, 165, 209, 144, 94, 20, 219, 53, 49, 21, 160, 115, 145, 17, 187, 244, 13, 29, 25, 57, 217, 194, 74, 200, 23, 182, 238, 128, 103, 140, 56, 252, 12, 135, 178, 152, 84, 111, 126, 47, 132, 99, 105, 237, 186, 37, 130, 72, 210, 157, 184, 3, 1, 44, 69, 172, 65, 7, 198, 206, 212, 166, 98, 192, 28, 5, 155, 136, 241, 208, 131, 124, 80, 116, 127, 202, 201, 58, 149, 108, 97, 60, 48, 14, 93, 81, 158, 137, 2, 227, 253, 68, 43, 120, 228, 169, 112, 54, 250, 129, 46, 188, 196, 85, 150, 6, 254, 180, 233, 230, 31, 76, 55, 18, 9, 32, 82, 70


section .bss
  inputVetor: resb INPUT_TAM_MAX + 1 ; cada char é 1 byte
  inputTam: resw 1
  inputResto: resb 1
  inputMod16: resw 1

  novoBloco: resb 16
  novoValor: resb 1

section .text
_start:
  ; lê input
  mov eax, STDIN
  mov edi, inputVetor
  ; mov esi, INPUT_TAM_MAX
  mov edx, esi
  syscall

  ; armazena o tamanho do input
  mov ecx, inputVetor
  xor eax, eax
  mov al, [ecx]
  cmp al, 0
  je _erroInput
  mov [inputTam], eax


; PASSO 1
  ; calcula (16 - inputTam % 16)
  mov eax, [inputTam]
  xor edx, edx
  mov ebx, 16
  div ebx
  mov [inputMod16], eax
  mov ebx, 16
  sub ebx, edx
  mov [inputResto], ebx

  ; aumenta o vetor de input
  mov ecx, inputTam
  add ecx, [inputResto]

  mov eax, [inputVetor]
  mov ebx, [inputTam]
  add eax, ebx
  mov eax, 0x0
  xor rsi, rsi ; i
  _loopPasso1: ; preenche o vetor de input com inputResto
    inc rsi
    cmp rsi, [inputResto]
    jle _loopPasso1


; PASSO 2
; preenche o novoBloco com zeros
  xor al, al ; novoValor

; for i in range(inputMod16):
  _loopiPasso2:

;   for j in range(16):
  _loopjPasso2:
;     novoValor = vetorMagico[(saidaPassoUm[i*16 + j]) ^ novoValor] ^ novoBloco[j]
;     novoBloco[j] = novoValor
; mov eax, [inputVetor + ]
  

; PASSO 3


; PASSO 4

_erroInput:
  ; Handle input error
  ; ...
  jmp _sair

_sair:
  mov eax, 60
  xor edi, edi
  syscall

