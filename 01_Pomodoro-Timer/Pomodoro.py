from tkinter import *
import datetime

kerja = 25 # NOTE 25 menit
detik = 0 # nanti 25 menit akan diubah ke detik
running = False # mengecek apakah timer sedang berjalan atau di jeda?
after = None # membantu fungsin jeda(), untuk timer kalau mau dijeda
sisa_waktu = 0 

# 3. proses perhitungan mundur dalam pomodoro
def countdown(mundur) : 
    global after 
    global sisa_waktu
    # cari angka untuk tampilan menit
    # NOTE CARA KERJANYA => Gunakan operasi floor division(//), untuk membulatkan hasil bagi
    menit = mundur // 60

    # cari angka untuk tampilan detik
    # NOTE CARA KERJANYA => Gunakan operasi modulus (%), untuk mengambil sisa dari pembagian
    detik = mundur % 60

    # TAMBAHAN, Jika detik masuk dalam kondisi satu digit (1-9), tampilan nya ubah menjadi dua digit (01-09)
    if detik < 10 : 
        # NOTE HAL BARU! format string bisa di buat begini!
        detik = f"0{detik}"

    sisa_waktu = mundur

    # NOTE MENCETAK DI LAYAR TEKS WAKTU YANG BERJALAN
    waktu.itemconfig(tampilan_waktu,text= f"{menit}:{detik}")

    # Logika rekursif untuk perhitungan mundur pada timer (perhitungan mundur)
    if mundur > 0 : 
        # Penalaran = 1000 => 1000ms(milisecond) yang berarti 1 detik
        # countdown(), function coundown dipanggil ulang (rekursif)
        # mundur-1, angka(integer) yang dikirim oleh parameter (bernama mundur) dikurangi 1 
        # NOTE jadi setiap 1000ms/1detik, function ini akan memanggil function countdown, lalu dilakukan perintah mundur-1
        after = window.after(1000, countdown, mundur-1)
    else : 
        window.config(bg='red')
        running = False
        sisa_waktu = 0
        mulai.config(text='START')

        # --- LOGIKA BARU UNTUK MENCATAT DATA ---
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Buka file bernama 'data_belajar.csv', mode 'a' artinya Append (nambah baris di bawahnya)
        with open("data_belajar.csv", mode="a") as file:
            file.write(f"{waktu_sekarang},25,Selesai\n")
        # NOTE bagian ini digunakan untuk mencatat riwayat penggunaan timer pomodoro!

def start() :
    global running
    global sisa_waktu
    # Ubah waktu 25 menit jadi detik
    # dengan cara memanggil method countdown. panggil variable kerja lalu di kalikan dengan 60(detik)
    running = True
    mulai.config(text='JEDA')
    if sisa_waktu == 0 : 
        countdown(kerja * 60)
    else : 
        countdown(sisa_waktu)

    
def jeda() : 
    global running
    global after

    running = False
    mulai.config(text='LANJUT')

    if after is not None : 
        window.after_cancel(after)
        after = None

def toggle() : 
    if running : 
        jeda()
    else : 
        start()

def reset() : 
    global after 
    global running
    global sisa_waktu

    # NOTE Selalu lakukan pengecekan terlebih dahulu!
    if after is not None :
        window.after_cancel(after)
        after = None
    
    running = False
    mulai.config(text='START')
    sisa_waktu = 0

    waktu.itemconfig(tampilan_waktu, text= '25:00')

# =============== GUI ===============
window = Tk()
window.title('POMODORO TIMER')
window.config(bg='gray')

waguri = PhotoImage(file='Waguri_unya.png')
waguris = waguri.subsample(4,4)
icon = Label(window,image=waguris).grid(row=0,column=1)
judul = Label(window,text='Pomodoro Timer',font=('Arial', 30)).grid(row=1,column=1)
waktu = Canvas(width=200, height=200,bg='gray',highlightthickness=0) 
tampilan_waktu = waktu.create_text(100,100,text='00:00',fill='black',font=('Courier',30,'bold'))
waktu.grid(row=2,column=1)

# TOMBOL
mulai = Button(window,text='START',command=toggle)
mulai.grid(row=3,column=0)
ulang = Button(window,text='RESET',command= reset)
ulang.grid(row=3,column=2)


window.geometry('500x500')
window.mainloop()
