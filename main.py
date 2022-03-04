#Libary yang dibutuhkan untuk melakukan Tokenization, Stop Word, Stemming
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
nltk.download('punkt')
nltk.download('stopword')

#Function untuk record dataset excel ke program
def passing_raw_data():
    # Untuk pass data dari excel dapat menggunakan beberapa cara 
    # yaitu xlrd, openpyxls, atau pandas
    raw_data = pd.read_excel(
        'DatasetText.xlsx', sheet_name='Dataset', usecols='B')
    raw_data = raw_data.iloc[3000:3200]
    # Pandas memebentuk data menjad dataframe, maka ubah data 
    # menjadi bentuk list
    data = raw_data.values.tolist()
    return data

#Function untuk lower case semua dataset
def lower_case_folding(data):
    # Lakukan lower case pada setiap string dari setiap list
    lower_case_list = [[string.lower() for string in sublist]
                       for sublist in data]
    return lower_case_list

#Function untuk mendapatkan token-token dati dataset
def get_tokenizing(data):
    flat_list = []
    word_tokens = []
    # Proses tokenization mencakup lower case folding, data cleaning,
    # dan split per word
    # Tokenization memerlukan format string atau list
    # Oleh karena itu proses terlebih dahulu nested list dari dataset 
    # menjadi flatten list,
    # nested list yang diproses adalah hasil dari lower case folding
    for sublist in lower_case_folding(data):
        for item in sublist:
            # simpan data dalam satu buah variabel list
            flat_list.append(item)
    for sentence in flat_list:
        # Bersihkan data menggunakan library ReGex dengan function sub 
        # untuk mereturn nilai yang diinginkan saja "^" menyebabkan 
        # pengecualian nilai yang direturn
        # Jadi [^a-zA-Z\s-] regex akan mereturn seluruh nilai kecuali 
        # nilai a-z, A-Z, \s, dan "-". Nilai" tersebut akan di replace 
        # dengan "" (string kosong)
        per_word = re.sub('[^a-zA-Z\s-]', '', sentence)
        # Setelah data bersih lakukan tokenization
        per_word = word_tokenize(per_word)
        #Simpan data dalam satu list
        word_tokens = word_tokens + per_word
    return word_tokens

#Function untuk menghapus data kata yang tidak ada dalam stop word
def stop_word_removal(data,language):
    # Record data kata dalam stop word Sastrawi (data bahasa indonesia)
    stop_words = set(stopwords.words(language))
    word_tokens_no_stop_words = []
    #simpan data tanpa stop word yaitu data yang kata-lata tidak penting telah 
    # dihapus dari list
    word_tokens_no_stop_words = [w for w in data if not w in stop_words]
    return word_tokens_no_stop_words

#Function untuk melakukan stemming
def get_stemming(data):
    #Record stemmer dalam variable
    factory = StemmerFactory()
    #buat sebuah data stemmer
    stemmer = factory.create_stemmer()
    word_stemming = []
    for word in data:
        # For loop setiap data dalam list dan ubah data tersebut 
        # menjadi data stem
        output = stemmer.stem(word)
        #Simpan data hasil stem dalam sebuah variabel list
        word_stemming.append(output)
    return word_stemming

#Function untuk menghitung frekuensi kemunculan kata
def get_word_frequency(data):
    # Lakukan pengecekan frekuensi setiap kata dalam list
    word_frec = nltk.FreqDist(data)
    # Kembalikan data dan frekuensinya sebanyak yang 
    # diinginkan (value sementara 500 kata)
    return word_frec.most_common(500)


def design():
    print(f"\t\t*************************************************")
    print(f"\t\t*         -----------------------------         *")
    print(f"\t\t*             TEXT PREPROCESSING                *")
    print(f"\t\t*         -----------------------------         *")
    print(f"\t\t*         -----------------------------         *")
    print(f"\t\t*           Agung Adipurwa/2008561096           *")
    print(f"\t\t*        -----------------------------          *")
    print(f"\t\t*                                               *")
    print(f"\t\t*************************************************")


def main():
    #Record semua data terlebih dahulu dalam beberapa variable
    word = passing_raw_data();tkn_word = [];tkn_word = get_tokenizing(word)
    tkn_word_no_stpw = stop_word_removal(tkn_word,'indonesian')
    tkn_stemming = get_stemming(tkn_word_no_stpw)
    while(1):
        design()
        print("\n")
        print("1. Tokenization")
        print("2. Stop Word")
        print("3. Stemming")
        print("4. Word Frequency")
        asn = int(input("Masukan pilihan: "))
        print("\n")
        if asn == 1:
            print("Tokenization result:\n\n{}".format(tkn_word))
            print("\n\n")
        elif asn == 2:
            print("Stop word result:\n\n{}".format(tkn_word_no_stpw))
            print("\n\n")
        elif asn == 3:
            print("Stemming result:\n\n{}".format(tkn_stemming))
            print("\n\n")
        elif asn == 4:
            print("1. Frequency of Tokenization")
            print("2. Frequency of Stop Word")
            print("3. Frequency of Stemming")
            fasn = int(input("Masukkan pilihan: "))
            if fasn == 1:
                print("Frequency of Tokenization result:\n\n{}".format(
                    get_word_frequency(tkn_word)))
                print("\n\n\n")
            elif fasn == 2:
                print("Frequency of Stop Word result:\n\n{}".format(
                    get_word_frequency(tkn_word_no_stpw)))
                print("\n\n\n")
            elif fasn == 3:
                print("Frequency of Stemming result:\n\n{}".format(
                    get_word_frequency(tkn_stemming)))
                print("\n\n\n")
            else:
                print("Inputan salah")
        else:
            print("Inputan salah")


if __name__ == "__main__":
    main()
