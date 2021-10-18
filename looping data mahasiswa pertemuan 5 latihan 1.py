
loop=int(input("Masukkan Nilai perulangan yang anda inginkan: "))
#PROCESS
for i in range(loop):
    print("Urutan Data Ke -",i+1)
    nim=input("Masukkan Nim anda: ")
    nilai_uts=int(input("Masukkan Nilai Uts anda: "))
    nilai_uas=int(input("Masukkan Nilai Uas anda: "))
    print("Nim anda adalah %s \t || Nilai Uts anda adalah %i \t || Nilai Uas anda adalah %i ||"%(nim,nilai_uts,nilai_uas))
    print("=============================================================================================\n")