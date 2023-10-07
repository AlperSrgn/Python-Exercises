import sys
import random

#*************************************************************
"""DOSYA YOLU """
file_path = "cikti.txt"
"""DOSYA YOLU """
#*************************************************************


def oyun_tahtasi(minimum=5, maximum=10):
    size = random.randint(minimum, maximum)
    board = [[random.randint(0, 9) for i in range(size)] for i in range(size)]
    return board

def tahtayi_dosyaya_yaz(board, file_path):
    with open(file_path, "w") as dosya:
        for row in board:
            satir = " ".join(str(cell) for cell in row)
            dosya.write(satir + "\n")


def txt_oku(file_path):
    with open(file_path, "r") as file:
        board = [list(map(int, line.strip().split())) for line in file.readlines()]
    return board

def tahtayi_getir(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


def komsu_bul(board, row, col, visited):
    if (row, col) in visited:
        return []

    visited.add((row, col))
    komsular = [(row, col)]
    cevre_koordinat = [(-1, 0), (0, -1), (1, 0), (0, 1) ]

    for dr, dc in cevre_koordinat:
        r, c = row + dr, col + dc
        if ((0 <= r < len(board)) and (0 <= c < len(board[0])) and (board[r][c] == board[row][col])):
            komsular.extend(komsu_bul(board, r, c, visited))

    return komsular

def hucre_sil_kaydir(board, silinecek_hucre):
    for row, col in silinecek_hucre:
        board[row][col] = None

    for col in range(len(board[0])):
        dolu_hucre = [board[row][col] for row in range(len(board)) if board[row][col] is not None]
        bos_hucre = [' '] * (len(board) - len(dolu_hucre))
        yeni_hucre = bos_hucre + dolu_hucre

        for row in range(len(board)):
            board[row][col] = yeni_hucre[row]

    dolu_sutun = [col for col in zip(*board) if any(cell is not None for cell in col)]
    bos_sutun = [col for col in zip(*board) if all(cell is ' ' for cell in col)]
    yeni_tahta = [list(row) for row in zip(*(bos_sutun + dolu_sutun))]

    return yeni_tahta


board = oyun_tahtasi()
tahtayi_dosyaya_yaz(board, file_path)
board = txt_oku(file_path)


print("Başlangıç Tahtası:")
tahtayi_getir(board)

sum = 0
while True:
    row, col = map(int, input("Aralarında Boşluk Olacak Şekilde"
                              "\nSatır ve Sütun Değeri Girin ÖRN(1 2):  ").split())
    row -= 1
    col -= 1

    if ((0 <= row < len(board)) and (0 <= col < len(board[0]))):
        silinecek_hucre = komsu_bul(board, row, col, set())

        if len(silinecek_hucre) > 1:
            board = hucre_sil_kaydir(board, silinecek_hucre)
            print("\nOyun Tahtası:")
            tahtayi_getir(board)
            tahtayi_dosyaya_yaz(board, file_path)
        else:
            print("\n***KOMŞU DEĞERİ YOK*** \n-->TEKRAR DENE<--:")
            tahtayi_getir(board)
    else:
        print("Geçerli Bir Koordinat Girin")




