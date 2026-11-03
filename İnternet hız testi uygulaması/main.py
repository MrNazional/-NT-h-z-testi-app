import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from speedtest import Speedtest

from SpeedTestWindow import *
#----------------------------------------------------------------------------------------------------------------------------------
#------------------------------------- Pencere Oluşturma ve Pencere Görüntüleme ---------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_SpeedTestWindow()
ui.setupUi(window)
window.show()

st = Speedtest()

def start_to_test():
    ui.statusbar.showMessage("Teste Başlandı....", 12000)
    downloadSpeed = st.download()/1000000
    uploadSpeed = st.upload()/1000000
    ui.prbDownload.setValue(int(downloadSpeed))
    ui.prbUpload.setValue(int(uploadSpeed))
    ui.lneDownload.setText(f"{downloadSpeed:.2f} Mbps")
    ui.lneUpload.setText(f"{uploadSpeed:.2f} Mbps")
    ui.statusbar.showMessage("Teste Başarıyla Tamamlandı....", 12000)
    
ui.pbTesteBasla.clicked.connect(start_to_test)

sys.exit(app.exec_())