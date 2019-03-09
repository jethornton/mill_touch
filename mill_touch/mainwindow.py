from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.coordOffsetGroup.buttonClicked.connect(self.offsetHandleKeys)
        self.mdiButtonGroup.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiBackSpace.clicked.connect(self.mdiHandleBackSpace)

    def offsetHandleKeys(self, button):
        char = str(button.text())
        text = self.cordOffsetLbl.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.cordOffsetLbl.setText(text)

    def mdiHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiLabel.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiLabel.setText(text)

    def mdiHandleBackSpace(self):
        if len(self.mdiLabel.text()) > 0:
            text = self.mdiLabel.text()[:-1]
            self.mdiLabel.setText(text)


    def on_exitBtn_clicked(self):
        self.app.quit()

