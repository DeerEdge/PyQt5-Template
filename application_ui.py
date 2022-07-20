# Import PyQt5's widgets to be used throughout the program
from PyQt5 import QtWidgets

# A class is created that holds all functions of the program
class ui_main_window(object):
    # This function setups up a basic window where widgets can be added
    def setup_window(self, main_window):
        main_window.setObjectName("main_window")
        # The size of the window is specified using "resize()"
        main_window.resize(850, 650)

        # The bottom bar of a window is added using the QStatusBar widget
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

if __name__ == "__main__":
    import sys
    # An application is created
    app = QtWidgets.QApplication(sys.argv)
    # A main window is created for the application
    main_window = QtWidgets.QMainWindow()
    # The user interface sets up the main window class
    ui = ui_main_window()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())