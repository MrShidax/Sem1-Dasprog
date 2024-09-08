HH1, MM1, SS1 = map(int,input("Masukkan waktu stream (GMT+2) : ").split(":"))
HH2, MM2, SS2 = map(int,input("Masukkan waktu saat ini (GMT+7) : ").split(":"))
GMT7 = ((HH1 * 3600) + (MM1 * 60) + SS1) + (7 * 3600)
GMT2 = ((HH2 * 3600) + (MM2 * 60) + SS2) + (2 * 3600)
waktu = GMT7 - GMT2
if (waktu >= 0):
    HH3, MMSisa = divmod(waktu, 3600)
    MM3, SS3 = divmod(MMSisa, 60)
    print(f"{HH3:02}:{MM3:02}:{SS3:02}")
else:
    print("See you on the next Pear event!")


