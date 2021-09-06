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

st = pyshorteners.Shortener()
url = str(input("✏️   Inserta la URL a cortar: "))
short_url = st.dagd.short(url) #Acortamos el enlace.
print("✂️   Enlace acortado: "+short_url)