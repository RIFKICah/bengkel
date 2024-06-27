import os
import streamlit as st

# Judul Halaman
st.title("**Toko Online Hebat**")

# Deskripsi Toko
st.write("Selamat datang di Toko Online Hebat! Kami menyediakan berbagai macam produk berkualitas dengan harga terbaik.")

# Kategori Produk
st.header("Kategori Produk")
kategori_produk = ["Elektronik", "Pakaian", "Peralatan Rumah Tangga", "Mainan"]
pilihan_kategori = st.selectbox("Pilih Kategori", kategori_produk)

# Produk Terbaru
st.header("Produk Terbaru")
# Placeholder untuk menampilkan produk terbaru
# (Anda perlu mengimplementasikan logika untuk mengambil data produk terbaru)
st.write("Produk terbaru akan ditampilkan di sini.")

# Penawaran Spesial
st.header("Penawaran Spesial")
# Placeholder untuk menampilkan penawaran spesial
# (Anda perlu mengimplementasikan logika untuk mengambil data penawaran spesial)
st.write("Penawaran spesial akan ditampilkan di sini.")

# Ajakan Bertindak
st.header("Ajakan Bertindak")
st.write("Belanja sekarang dan dapatkan diskon 10%!")
st.button("Belanja Sekarang", key="shop_now")


# Menampilkan foto berjejer ke samping (2 kolom)
st.header("Produk Terbaru")

# Ambil data foto terbaru (asumsikan Anda memiliki daftar path lokal ke gambar)
foto_terbaru = [
    os.path.join('12.png'),
    os.path.join('12.png'),
    os.path.join('12.png'),
]

# Bagi data foto menjadi 2 kolom
kolom1, kolom2 = st.columns(2)

# Tampilkan foto di setiap kolom
for i in range(len(foto_terbaru)):
    if i % 2 == 0:
        kolom1.image(foto_terbaru[i])
    else:
        kolom2.image(foto_terbaru[i])