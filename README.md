# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Database:
User: postgres
Pass: jjm123

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000. Sejak awal berdirinya, perusahaan ini telah tumbuh pesat dengan kehadiran lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Perusahaan ini dikenal karena inovasinya dalam menyediakan produk atau layanan yang berkualitas tinggi, dengan fokus pada kepuasan pelanggan dan efisiensi operasional.

### Permasalahan Bisnis

Walaupun telah menjadi perusahaan besar dengan banyak karyawan, Jaya Jaya Maju menghadapi tantangan utama, yaitu tingginya tingkat churn atau keluar karyawan (attrition rate) yang melebihi 10%. Ini menjadi perhatian utama bagi manajemen, terutama departemen Human Resources (HR), yang berusaha untuk memahami dan mengurangi faktor-faktor yang menyebabkan karyawan keluar.

### Cakupan Proyek

- Membuat Business Dashboard dengan Metabase
- Menganalisis Data
- Membuat model Machine Learning untuk memprediksi Attriction

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:

Menginstall dan mengimport library yang tercantum dalam requirements.txt

## Business Dashboard

Dashboard Jaya Jaya Maju dirancang untuk membantu manajemen dan departemen HR dalam mengelola karyawan, memantau faktor-faktor yang mempengaruhi tingkat attrition (rasio karyawan yang keluar), dan membuat keputusan yang berbasis data. Berikut adalah elemen-elemen utama dari dashboard tersebut beserta fungsinya:
**Fungsi dan Tujuan dari Setiap Elemen:**
- KPI Attrition Rate: Memberikan gambaran umum apakah perusahaan telah berhasil mengurangi tingkat attrition berdasarkan data historis.
- Bar Chart dan Pie Chart: Memberikan visualisasi yang jelas tentang bagaimana berbagai faktor (seperti departemen, usia, atau tingkat pendidikan) berkontribusi terhadap karyawan yang keluar.
- Heatmap: Membantu dalam mengidentifikasi faktor yang paling berkontribusi pada tingkat attrition dengan mengelompokkan faktor-faktor utama secara visual.
- Trend Analysis: Menampilkan pola peningkatan atau penurunan tingkat attrition dari waktu ke waktu, memberikan wawasan tentang efektivitas strategi yang diterapkan perusahaan.

## Conclusion

Proyek yang dikerjakan bersama Jaya Jaya Maju bertujuan untuk mengatasi tantangan tingginya tingkat attrition (rasio karyawan yang keluar) dengan menggunakan pendekatan data-driven. Beberapa langkah utama yang diambil meliputi analisis data, pengembangan model machine learning, dan pembuatan dashboard bisnis yang interaktif untuk memantau faktor-faktor yang mempengaruhi attrition.
**Kesimpulan dan Dampak Proyek:**
- Peningkatan Efisiensi: Proyek membantu mempercepat proses analisis data dan menghasilkan wawasan yang lebih tajam dalam waktu yang lebih singkat.
- Kinerja Manajemen: Dashboard membantu manajemen dalam melacak dan memantau faktor-faktor utama yang mempengaruhi tingkat attrition secara sistematis.
- Pengurangan Attrition: Dengan penggunaan model prediksi dan visualisasi yang efektif, perusahaan memiliki peluang yang lebih besar untuk mengelola karyawan dengan lebih baik dan mengurangi tingkat attrition yang tinggi.

### Rekomendasi Action Items (Optional)

Untuk mengatasi Attrition Rate yang tinggi, perusahaan dapat mengikuti saran berikut:
- Memperhatikan karyawan dengan waktu kerja diperusahaan <10 tahun
> Karena waktu <10 tahun bekerja diperusahaan merupakan waktu dengan Attrition Rate yang tinggi
- Meningkatkan Environment Satisfaction agar tingkat attrition berkurang. 
> Pada chart Environment Satisfaction vs Attrition, dapat diketahui bahwa 20% karyawan mengundurkan diri karena lingkungan yang kurang memuaskan
- Memperhatikan dan meningkatkan kesejahteraan karyawan khususnya pada Sales Department
> Karena Sales Department memiliki Attrition Rate yang paling tinggi
- Meningkatkan Training Time, terutama untuk karyawan yang baru lulus atau dengan umur <25 tahun
> Terdapat korelasi antara karyawan <25 tahun dengan Training Times
