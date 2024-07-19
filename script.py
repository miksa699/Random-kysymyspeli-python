# MMMMMMMM               MMMMMMMM  iiii  kkkkkkkk                                                   66666666  999999999     
# M:::::::M             M:::::::M i::::i k::::::k                                                  6::::::6 99:::::::::99   
# M::::::::M           M::::::::M  iiii  k::::::k                                                 6::::::699:::::::::::::99 
# M:::::::::M         M:::::::::M        k::::::k                                                6::::::69::::::99999::::::9
# M::::::::::M       M::::::::::Miiiiiii  k:::::k    kkkkkkk  ssssssssss     aaaaaaaaaaaaa      6::::::6 9:::::9     9:::::9
# M:::::::::::M     M:::::::::::Mi:::::i  k:::::k   k:::::k ss::::::::::s    a::::::::::::a    6::::::6  9:::::9     9:::::9
# M:::::::M::::M   M::::M:::::::M i::::i  k:::::k  k:::::kss:::::::::::::s   aaaaaaaaa:::::a  6::::::6    9:::::99999::::::9
# M::::::M M::::M M::::M M::::::M i::::i  k:::::k k:::::k s::::::ssss:::::s           a::::a 6::::::::6666699::::::::::::::9
# M::::::M  M::::M::::M  M::::::M i::::i  k::::::k:::::k   s:::::s  ssssss     aaaaaaa:::::a6::::::::::::::6699999::::::::9 
# M::::::M   M:::::::M   M::::::M i::::i  k:::::::::::k      s::::::s        aa::::::::::::a6::::::66666:::::6    9::::::9  
# M::::::M    M:::::M    M::::::M i::::i  k:::::::::::k         s::::::s    a::::aaaa::::::a6:::::6     6:::::6  9::::::9   
# M::::::M     MMMMM     M::::::M i::::i  k::::::k:::::k  ssssss   s:::::s a::::a    a:::::a6:::::6     6:::::6 9::::::9    
# M::::::M               M::::::Mi::::::ik::::::k k:::::k s:::::ssss::::::sa::::a    a:::::a6::::::66666::::::69::::::9     
# M::::::M               M::::::Mi::::::ik::::::k  k:::::ks::::::::::::::s a:::::aaaa::::::a 66:::::::::::::669::::::9      
# M::::::M               M::::::Mi::::::ik::::::k   k:::::ks:::::::::::ss   a::::::::::aa:::a  66:::::::::66 9::::::9       
# MMMMMMMM               MMMMMMMMiiiiiiiikkkkkkkk    kkkkkkksssssssssss      aaaaaaaaaa  aaaa    666666666  99999999        
                                                                                                                

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import threading

def soita_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

jasoittoon = threading.Thread(target=soita_mp3, args=("music/koolmusik.mp3",))
jasoittoon.daemon = True
jasoittoon.start()

def sammuta(): pass

L, K = 1280, 720
kikuli, kakeli = 400, 100

def näytä_popuppi():
    # Luo popuppi
    PR = "WM_DELETE_WINDOW"
    popuppi = tk.Toplevel(paskanali)
    popuppi.title("Täytä tyhjä kohta.")
    popuppi.geometry(f"{kikuli}x{kakeli}")
    popuppi.protocol(PR, sammuta)

    # Tekee kyssärin
    kusi_kyssäri_teksti = tk.Label(popuppi, text="____ olen homoseksuaali.")
    kusi_kyssäri_teksti.pack()

    # Muutamat napit siihe mitä voi painella
    def nappia_pantu(napin_teksti):
        messagebox.showinfo("Odotin sulta vähän enemmän.", f"Vastauksesi: {napin_teksti} olen homoseksuaali.")
        popuppi.destroy()
        paskanali.destroy()

    valinnantynkä1 = tk.Button(popuppi, text="Kyllä", command=lambda: nappia_pantu("Kyllä"))
    valinnantynkä1.pack(side=tk.BOTTOM)

    valinnantynkä2 = tk.Button(popuppi, text="Ei", command=lambda: nappia_pantu("Ei"))
    valinnantynkä2.pack(side=tk.BOTTOM)

    valinnantynkä3 = tk.Button(popuppi, text="Ehkä", command=lambda: nappia_pantu("Ehkä"))
    valinnantynkä3.pack(side=tk.BOTTOM)

    # Siis en tiiä miks mut kokopaska meni aluks rikki jos tätä ei ollu ni turha poistaa ku toimii hyvi
    paskanali.wait_window(popuppi)

def alotanisti():
    # Piilota päämenu
    paskanali.withdraw()

    # Näytä se popuppi
    näytä_popuppi()

# Luo alotusikkuna
paskanali = tk.Tk()
paskanali.title("super duper miksa69 ameising paska pyhton skripti... Vittu meen ampumaan itteni.")
paskanali.geometry(f"{L}x{K}")

# Luo freimi
jokupaska = tk.Frame(paskanali)
jokupaska.pack()

# Lataa PNG kuva ja vaihda kokoa
kuvantynkä = Image.open("images/omppu.png")
kuvantynkä = kuvantynkä.resize((600, 400))  # reso on 600 X 400

kuva = ImageTk.PhotoImage(kuvantynkä)

# isoteksti tosiaaan
pippelikikkeli = tk.Label(jokupaska, text="Tervetuloa haluatko paskoa allesi ohjelmaan.", font=("Impact", 24))
pippelikikkeli.pack(pady=20)

kuvateksti = tk.Label(jokupaska, image=kuva)
kuvateksti.pack(pady=20)

# Alotus nappi
alota = tk.Button(jokupaska, text="aloita_nappi_.exe", command=alotanisti, font=("Impact", 36), height=1, width=16)
alota.pack(pady=20)

def sammuta():
    pass

paskanali.protocol("WM_DELETE_WINDOW", sammuta)

paskanali.mainloop()
