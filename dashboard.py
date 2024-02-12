#import requirements
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

#Pengerjaan Andrata
def analisis_berat_produk(df_data_produk) :
    #Mengambil data produk
    berat_produk = df_data_produk['product_weight_g'].values
    
    #Cleaning data dengan menghapus nilai null pada 'products_dataset.csv'
    df_data_produk.dropna(subset=['product_category_name','product_name_lenght','product_description_lenght','product_photos_qty','product_weight_g','product_length_cm','product_height_cm','product_width_cm'], axis=0, inplace=True)

    df_data_produk.reset_index(drop=True, inplace=True)

    #Mengambil jumlah barang kategori ringan (500g - 1Kg)
    produk_ringan = berat_produk[(berat_produk >= 500) & (berat_produk < 1000)]

    #Mengambil jumlah barang kategori sedang (1Kg - 5Kg)
    produk_sedang = berat_produk[(berat_produk >= 1000) & (berat_produk < 5000)] 

    #Mengambil jumlah barang kategori berat (> 5Kg)
    produk_berat = berat_produk[berat_produk >= 5000]

    #Menghitung value dari kategori berat 'ringan','sedang','berat'
    jumlah_Produk_ringan = len(produk_ringan)
    jumlah_Produk_sedang = len(produk_sedang)
    jumlah_Produk_berat = len(produk_berat)

    # Menampilkan lima baris pertama dari data CSV
    st.header("Bentuk data produk")
    st.dataframe(df_data_produk.head())

    #Menjelaskan Pengkategorian Berat barang
    st.write("""Akan dilakukan pengkategorian berat barang untuk melihat produk dengan rentang berat berapa yang memiliki jumlah terbanyak.
             Berat produk akan dibagi menjadi 3 Kategori Yaitu :\n 1. Kategori 'Ringan' dengan rentang berat 500g - 1Kg.
             \n2. Kategori 'Sedang' dengan rentang berat 1Kg - 5Kg.\n 3. Kategori 'Berat' dengan rentang berat > 5Kg""")
    
    st.write('<hr>', unsafe_allow_html=True)

    #Grafik kategori berat produk
    data_berat_produk = pd.DataFrame({
        'Kategori': ['Ringan', 'Sedang', 'Berat'],
        'Rentang' : ['500g - 1Kg', '1Kg - 5Kg', '> 5Kg'],
        'Jumlah': [jumlah_Produk_ringan, jumlah_Produk_sedang, jumlah_Produk_berat]
    })

    #Pengkategorian berat produk
    st.header("Grafik berat produk")
    st.dataframe(data_berat_produk)

    # Presentasi jumlah produk per kategori dengan bar chart
    label = data_berat_produk['Kategori']
    data = data_berat_produk['Jumlah']

    fig, ax = plt.subplots()
    ax.bar(label, data, color=['green' if kategori == 'Ringan' else 
          'blue' if kategori == 'Sedang' else 'red' for kategori in label])
    ax.set_xlabel('Kategori')
    ax.set_ylabel('Jumlah')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #tampil         
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Berat Produk") :
        st.write("""Dari Grafik diatas, dapat dilihat bahwa produk dengan kategori berat 'Sedang' memiliki jumlah terbanyak yaitu sebanyak
                 9203 produk, disusul oleh produk dengan kategori 'Ringan' sebanyak 7085 produk, dan yang paling sedikit adalah produk
                 dengan kategori 'berat' dengan jumlah 4197 produk. Kita dapat pula melihat berapa perbandingan persentase tiap kategori melalui diagram pie. """) 


    st.write('<hr>', unsafe_allow_html=True)

    #Presentasi persentasi perbandingan data dengan pie chart
    # Data
    label = ['Ringan (500g - 1Kg)', 'Sedang (1Kg - 5Kg)', 'Berat (> 5Kg)']
    banyak_barang = [jumlah_Produk_ringan, jumlah_Produk_sedang, jumlah_Produk_berat]

    # Plot pie
    fig, ax = plt.subplots()
    ax.pie(banyak_barang, labels=label, autopct='%1.1f%%', shadow=True)

    # Tampil pie
    st.header('Perbandingan Berat Produk')
    st.pyplot(fig)

    with st.expander("Penjelasan Pie Perbandingan Berat produk") :
        st.write("""Dari pie diatas, dapat dilihat bahwa produk kategori 'Sedang' memiliki persentase terbesar yaitu sebanyak 44.9% (9203 produk),
                 disusul dengan kategori 'Ringan' sebanyak 34.6% (7085 produk), dan kategori 'Berat' sebanyak 20.5% (4197 produk).""")
        
    st.write("""Analisis ini dapat berguna bagi perusahaan apabila misalnya suatu perusahaan ingin membagi-bagi produk ke dalam beberapa kategori yang 
             diambil berdasarkan berat produknya. Hal ini bisa dijadikan pertimbangan pengambilan keputusan oleh sebuah perusahaan, misalnya kendaraan apa yang
             harus banyak dimiliki perusahaan untuk pengantaran paket produk, penambahan fitur klasifikasi berat produk di aplikasi e-commerce, 
             dll.""")
        
    #Deskripsi Anggota yang mengerjakan bagian ini
    st.write('<hr>', unsafe_allow_html=True)
    st.caption("10122250 - Muhammad Andrata Zharfan Mustika")

#Pengerjaan Elsiano       
def lama_pengiriman(df_data_order):
    #Cek apakah ada missing value atau tidak
    df_data_order_null = df_data_order.isnull().values.any()
    df_data_order.isnull().sum()

    #Cek apakah ada data duplikat atau tidak
    df_data_order_duplicate = df_data_order.duplicated().values.any()

    #Cleaning data products_dataset.csv
    df_data_order.dropna(subset=['order_approved_at','order_delivered_carrier_date','order_delivered_customer_date'], axis=0, inplace=True)
    df_data_order.reset_index(drop=True, inplace=True)

    #Mengubah kolom 'order_purchase_timestamp' dan 'order_delivered_customer_date' menjadi tipe data datetime
    df_data_order['order_purchase_timestamp'] = pd.to_datetime(df_data_order['order_purchase_timestamp'])
    df_data_order['order_delivered_customer_date'] = pd.to_datetime(df_data_order['order_delivered_customer_date'])
    
    #Menghitung berapa lama pembeli menerima barang setelah memesannya
    df_data_order['lama_pengiriman'] = (df_data_order['order_delivered_customer_date'] - df_data_order['order_purchase_timestamp']).dt.days

    #Menampilkan DataFrame dengan kolom tambahan 'lama_pengiriman'
    st.write("Tabel hasil perhitungan lama pengiriman :")
    df_data_beli = df_data_order['order_delivered_customer_date']
    df_data_sampai = df_data_order['order_purchase_timestamp']
    lama_kirim = df_data_order['lama_pengiriman']

    tabel_hasil = pd.DataFrame({
        'Tanggal pembelian' : df_data_beli,
        'Tanggal sampai' : df_data_sampai,
        'Lama Pengiriman' : lama_kirim
    })

    #Mengambil data lama pengiriman barang
    waktu_pengiriman = df_data_order['lama_pengiriman'].values

    #Mengambil jumlah barang dengan waktu pengiriman kurang dari 30 hari
    waktu_U30 = waktu_pengiriman[(waktu_pengiriman >= 1) & (waktu_pengiriman < 30)]
    jumlah_waktu_U30 = len(waktu_U30)

    #Mengambil jumlah barang dengan waktu pengiriman lebih dari sama dengan 30 hari
    waktu_A30 = waktu_pengiriman[(waktu_pengiriman >= 30)]
    jumlah_waktu_A30 = len(waktu_A30)

    #Memvisualisasikan data lama pengiriman
    fig, ax = plt.subplots()
    ax.hist(df_data_order['lama_pengiriman'], bins=30, color='lightgreen', edgecolor='black')
    ax.set_title('Histogram Lama Pengiriman')
    ax.set_xlabel('Lama Pengiriman (hari)')
    ax.set_ylabel('Frekuensi')
    ax.set_xlim(0, 80)

    #menampilkan tabel hasil perhitungan
    st.dataframe(tabel_hasil)

    #menampilkan hasil visualisasi data lama pengiriman
    st.write('Diagram Lama Pengiriman Paket Kepada Pelanggan')
    st.pyplot(fig)    

    #Banyak barang yang waktu pengirimannya kurang dari 30 hari dan lebih dari sama dengan 30 hari
    st.write('Banyak barang yang waktu pengirimannya lebih 30 hari =', jumlah_waktu_U30)
    st.write('Banyak barang yang waktu pengirimannya lebih dari sama dengan 30 hari =', jumlah_waktu_A30)

    with st.expander("Conclusion dari pertanyaan kedua") :
        st.write(
            """
            - Conclution pertanyaan 2 \n
                Berdasarkan histogram di atas dapat diketahui bahwa 
                banyak barang yang waktu sampainya kurang dari 30 hari lebih banyak 
                dibandingkan dengan barang yang waktu sampainya lebih dari 30 hari. 
                Dengan jumlah barang yang waktu sampainya kurang dari 30 hari adalah 91896, 
                sedangkan barang yang waktu sampainya lebih dari 30 hari adalah 4552. 
                Dengan demikian perusahaan tetap bisa memakai jasa ekspedisi yang sekarang digunakan 
                karena waktu pengirimannya masih dalam batas wajar.
            """
        )

    #Deskripsi Anggota yang mengerjakan bagian ini
    st.write('<hr>', unsafe_allow_html=True)
    st.caption("10122237 - Muhammad Elsiano Gibran Alkaf")

#Pengerjaan Silvia Meida
def reviews_order(df_data_reviews):
    #Cek apakah ada missing value atau tidak
    missing_values = df_data_reviews.isnull().values.any()
    df_data_reviews.isnull().sum()

    #Cek apakah ada data duplikat atau tidak
    df_data_reviews_duplicate = df_data_reviews.duplicated().values.any()

    #Menghitung Rating terbanyak yang diberikan oleh Konsumen
    rating_counts = df_data_reviews['review_score'].value_counts()
    most_common_rating = rating_counts.idxmax()
    most_common_rating_counts = rating_counts.max()

    # Menampilkan Rating tertinggi dengan Tabel
    st.subheader('Tabel Rating Konsumen')
    st.table(rating_counts)
    
    #Menampilkan Rating terbanyak yang diberikan oleh Konsumen
    st.write('Rating Tertinggi                         : ', most_common_rating)
    st.write('Jumlah Konsumen dengan Rating Tertinggi  : ', most_common_rating_counts)

    #Memvisualisasikan reviews order
    fig, ax = plt.subplots()
    rating_counts = df_data_reviews['review_score'].value_counts()
    labels = rating_counts.index
    sizes = rating_counts.values

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
    ax.axis('equal')  
    ax.set_title('Distribution of Ratings')
    
    #Menampilkan Pie Chart Rating Order
    st.subheader('Konsumen dengan Rating tertinggi ')
    st.pyplot(fig)

    with st.expander("Conclusion dari pie chart di atas") :
        st.write(
            """
                Berdasarkan Pie Chart di atas dapat diambil kesimpulan bahwa Skor Rating tertingginya adalah 5 dengan jumlah persentase nya 57.8%.
            """
        )

    #Deskripsi Anggota yang mengerjakan bagian ini
    st.write('<hr>', unsafe_allow_html=True)
    st.caption("10122250 - Silvia Meida")
    



#File CSV yang dibutuhkan
df_data_produk = pd.read_csv('products_dataset.csv')
df_data_order = pd.read_csv('orders_dataset.csv')
df_data_reviews = pd.read_csv('order_reviews_dataset.csv')

#Pemanggilan
with st.sidebar :
    selected = option_menu('Menu',['Dashboard','About'],
    icons =["easel2", "info-circle"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2,tab3 = st.tabs(["Pengkategorian Berat Produk", "Analisis Waktu Pengriman", "Analisis Rating Konsumen"])

    with tab1 :
        analisis_berat_produk(df_data_produk)
    with tab2 :
        lama_pengiriman(df_data_order)
    with tab3 :
          reviews_order(df_data_reviews)

else :
    if (selected == 'About') :
        st.title("Profile Mahasiswa")

        st.write('<hr>', unsafe_allow_html=True)
        st.write("NIM               : 10122250")
        st.write("NAMA              : Muhammad Andrata Zharfan Mustika")
        st.write("KELAS             : IF-7")
        st.write("BAGIAN PENGERJAAN : Pengkategorian Berat Produk")
        
        st.write('<hr>', unsafe_allow_html=True)
        st.write("NIM               : 10122237")
        st.write("NAMA              : Muhammad Elsiano Gibran Alkaf")
        st.write("KELAS             : IF-7")
        st.write("BAGIAN PENGERJAAN : Analisis Waktu Pengiriman")

        st.write('<hr>', unsafe_allow_html=True)
        st.write("NIM    : 10122246")
        st.write("NAMA   : Silvia Meida")
        st.write("KELAS  : IF-7")
        st.write("BAGIAN PENGERJAAN : Analisis Rating Konsumen")

        st.write('<hr>', unsafe_allow_html=True)
        st.caption("UAS Pemrograman Dasar Sains Data")