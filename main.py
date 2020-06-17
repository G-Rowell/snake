###############################################################################

#Local imports
import board
import qtSub

##Library imports
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
#from PyQt5.QtGui import QPalette, QColor

###############################################################################

app = QApplication([])

window = qtSub.MainWindow()
window.show()

# Start the event loop
app.exec_()
