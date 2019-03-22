from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

# Setup Help Text
import mill_touch.helptext as helptext

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.coordOffsetGroup.buttonClicked.connect(self.offsetHandleKeys)
        self.toolButtonGroup.buttonClicked.connect(self.toolHandleKeys)
        self.toolBackSpace.clicked.connect(self.toolHandleBackSpace)
        self.mdiSmartButtonGroup.buttonClicked.connect(self.mdiSmartHandleKeys)
        self.mdiLoadParameters.clicked.connect(self.mdiSmartSetLabels)
        self.mdiSmartBackspace.clicked.connect(self.mdiSmartHandleBackSpace)
        self.gcodeHelpBtn.clicked.connect(self.tabForward)
        self.mdiBackBtn.clicked.connect(self.tabBack)

    def tabForward(parent):
        parent.mdiStackedWidget.setCurrentIndex(parent.mdiStackedWidget.currentIndex() + 1)
    def tabBack(parent):
        parent.mdiStackedWidget.setCurrentIndex(parent.mdiStackedWidget.currentIndex() - 1)

    def mdiSmartHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiSmartEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiSmartEntry.setText(text)

    def mdiSmartSetLabels(self):
        # get smart and figure out what axes are used

        text = self.mdiSmartEntry.text() or '0'
        if text != '0':
            words = helptext.gcode_words()
            if text in words:
                self.mdiSmartClear()
                print(type(words[text]))
                for index, value in enumerate(words[text], start=1):
                    getattr(self, 'gcodeParameter_' + str(index)).setText(value)
            else:
                self.mdiSmartClear()
            titles = helptext.gcode_titles()
            if text in titles:
                self.gcodeDescription.setText(titles[text])
            else:
                self.mdiSmartClear()
            self.gcodeHelpLabel.setText(helptext.gcode_descriptions(text))
        else:
            self.mdiSmartClear()

    def mdiSmartClear(self):
        for index in range(1,13):
            getattr(self, 'gcodeParameter_' + str(index)).setText('')
        self.gcodeDescription.setText('')
        self.gcodeHelpLabel.setText('')

    def mdiSmartHandleBackSpace(self):
        if len(self.mdiSmartEntry.text()) > 0:
            text = self.mdiSmartEntry.text()[:-1]
            self.mdiSmartEntry.setText(text)

    def offsetHandleKeys(self, button):
        char = str(button.text())
        text = self.cordOffsetLbl.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.cordOffsetLbl.setText(text)

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

