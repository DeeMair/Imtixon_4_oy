"""2.Masala"""

matnlar = ["  salom  ", "dunYo", "   dasturlash  ", "Uqitish    "]
yangi=[matn.strip().capitalize() for matn in matnlar]

count = len(yangi)  #count dganim GPT mas domla boshqacha yaxshiroq nom topalmadim (soni, sanash, boshqala) rosa xuni korinadida
print("tozalangan matn", yangi)
print("Sozlar soni", count)


