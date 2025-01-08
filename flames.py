ladka = input("Teri Hero:")
ladki = input("Meri Jaan:")
if(ladka==ladki):
    print("Idhu vanavil kootam, Epadithano two different name venum")
for ltr in ladka:
    if ltr in ladki:
        ladka = ladka.replace(ltr, "", 1)
        ladki = ladki.replace(ltr, "", 1)
remaining_count = len(ladka) + len(ladki)
current_index =0 
flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
while len(flames) > 1:
    index = (remaining_count + current_index - 1) % len(flames)
    flames.remove(flames[index])
    current_index = index
print(flames[0]) 