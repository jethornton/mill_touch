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
        self.toolButtonGroup.buttonClicked.connect(self.toolHandleKeys)
        self.toolBackSpace.clicked.connect(self.toolHandleBackSpace)

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
        text = self.mdiEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiHandleBackSpace(self):
        if len(self.mdiEntry.text()) > 0:
            text = self.mdiEntry.text()[:-1]
            self.mdiEntry.setText(text)

    def toolHandleKeys(self, button):
        char = str(button.text())
        text = self.toolOffsetLabel.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.toolOffsetLabel.setText(text)

    def toolHandleBackSpace(self):
        if len(self.toolOffsetLabel.text()) > 0:
            text = self.toolOffsetLabel.text()[:-1]
            self.toolOffsetLabel.setText(text)


    def on_exitBtn_clicked(self):
        self.app.quit()

