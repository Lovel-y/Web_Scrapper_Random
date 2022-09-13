import webbrowser, sys
from PySide6 import QtCore, QtWidgets
#Mis Modulos
from Modulos import Numero_Random_Rango
from Scrapper_Anime import Anime_Scrapper

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.Random_Photo_prnt = QtWidgets.QPushButton("Foto Aleatoria")
        self.anime_Random = QtWidgets.QPushButton("Anime Random")
        self.setWindowTitle("OstaMinzador")   
             
        #Seteo de los botones
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.anime_Random)
        self.layout.addWidget(self.Random_Photo_prnt) 

        self.anime_puntaje = QtWidgets.QLabel( '', alignment=QtCore.Qt.AlignCenter)
        self.anime_info = QtWidgets.QLabel( '', alignment=QtCore.Qt.AlignCenter)
        self.anime_link = QtWidgets.QLabel( '', alignment=QtCore.Qt.AlignCenter)
        self.anime_link.setOpenExternalLinks(True)
        
        #Acciones de los botones
        self.anime_Random.clicked.connect(self.anime_Button)
        self.Random_Photo_prnt.clicked.connect(self.Random_Photo)
        self.layout.addWidget(self.anime_link)
        self.layout.addWidget(self.anime_puntaje)
        self.layout.addWidget(self.anime_info)
        
    #Funciones
    @QtCore.Slot()
    def anime_Button(self):
        return_De_Array = Anime_Scrapper()
        self.anime_link.setText(return_De_Array[2])
        self.anime_puntaje.setText(return_De_Array[0])
        self.anime_info.setText(return_De_Array[1])

    def Random_Photo(self):
        Random_Link_Photo = "https://prnt.sc/" + str(Numero_Random_Rango(999999))
        webbrowser.open_new_tab(Random_Link_Photo)

#Inicializador de la ventana
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(300, 100)
    widget.show()

    sys.exit(app.exec())