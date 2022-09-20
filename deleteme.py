from googlesearch import search

names = ["Tuan Sy Tran", "Uyenchi Ho"]

for name in names:
    print(f"{name}:")
    for j in search(name, tld="co.in", num=20, stop=20, pause=2):
        print("  " + j)