#Sözlüğü Başlatabilirsiniz
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

while True:

    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word == 'P':
        break  # Kullanıcı 'q' girerse döngüyü sonlandır

    if word in meme_dict:
        print("Kelimenin Karşılığı:",meme_dict[word])
    else:
        print("Bu kelime sözlükte bulunmuyor.")
