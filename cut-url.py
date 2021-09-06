import pyshorteners

def banner():
    print(
        """
 ██████╗██╗   ██╗████████╗   ██╗   ██╗██████╗ ██╗     
██╔════╝██║   ██║╚══██╔══╝   ██║   ██║██╔══██╗██║     
██║     ██║   ██║   ██║█████╗██║   ██║██████╔╝██║     
██║     ██║   ██║   ██║╚════╝██║   ██║██╔══██╗██║     
╚██████╗╚██████╔╝   ██║      ╚██████╔╝██║  ██║███████╗
 ╚═════╝ ╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                          f̠̺̘m̫̦̫a̫̝͙t̡͙r̡͙̺i͍̠͜x̙̻̞ 2͉̦̼0͎͍2͓̪͜1̦̫͕  \n""")
banner()


try:
    st = pyshorteners.Shortener()
    url = str(input("✏️   Inserta la URL a cortar: "))
    short_url = st.dagd.short(url) #Acortamos el enlace.
    print("✂️   Enlace acortado: "+short_url)
except KeyboardInterrupt:
    print("\n🔴  Interrumpido por el usuario.")
except pyshorteners.exceptions.BadURLException:
    print("\n🔴  ERROR: Introduce una URL válida.")
finally: # Acabamos el programa.
    print("🏴  Saliendo de CUT-URL.")