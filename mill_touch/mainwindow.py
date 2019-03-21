from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

G2 = """G2 Coordinated Clockwise Helical Motion at Feed Rate
Center Format G2 axes offsets <P>
XY plane (G17)\nZ = helix\nI = X offset\nJ = Y offset\n
XZ plane (G18)\nY = helix\nI = X offset\nK = Z offset\n
YZ plane (G19)\nX = helix\nJ = Y offset\nK = Z offset\n
P = Number of Turns\n
Radius Format G2 axes R <P>
R = Radius from Current Position
"""

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.coordOffsetGroup.buttonClicked.connect(self.offsetHandleKeys)
        self.mdiButtonGroup.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiBackSpace.clicked.connect(self.mdiHandleBackSpace)
        self.toolButtonGroup.buttonClicked.connect(self.toolHandleKeys)
        self.toolBackSpace.clicked.connect(self.toolHandleBackSpace)
        self.mdiSmartButtonGroup.buttonClicked.connect(self.mdiSmartHandleKeys)
        self.mdiLoadParameters.clicked.connect(self.mdiSmartSetLabels)
        self.mdiSmartBackspace.clicked.connect(self.mdiSmartHandleBackSpace)

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
        words = {'G0':['X', 'Y', 'Z'],
            'G1':['X', 'Y', 'Z'],
            'G2':['X', 'Y', 'Z', 'I', 'J', 'K', 'R', 'P'],
            'G3':['X', 'Y', 'Z', 'I', 'J', 'K', 'R', 'P'],
            'G4':['P'],
            'G5':['I', 'J', 'P', 'Q'],
            'G5.1':['I', 'J'],
            'G5.2':['P', 'L'],
            'G10':['L'],
            'G10L1':['R', 'I', 'J', 'Q'],
            'G10L2':['P', 'X', 'Y', 'Z', 'R'],
            'G10L10':['P', 'R', 'I', 'J', 'Q'],
            'G10L11':['P', 'R', 'I', 'J', 'Q'],
            'G10L20':['P', 'X', 'Y', 'Z'],
            'G33':['X', 'Y', 'Z', 'K', '$'],
            'G33.1':['X', 'Y', 'Z', 'K', '$'],
            'G38.2':['X', 'Y', 'Z'],
            'G38.3':['X', 'Y', 'Z'],
            'G38.4':['X', 'Y', 'Z'],
            'G38.5':['X', 'Y', 'Z'],
            'G41':['D'],
            'G41.1':['D', 'L'],
            'G42':['D'],
            'G42.1':['D', 'L'],
            'G43':['H'],
            'G43.1':['X', 'Y', 'Z'],
            'G43.2':['H'],
            'G52':['X', 'Y', 'Z'],
            'G53':['X', 'Y', 'Z'],
            'G64':['P', 'Q'],
            'G73':['X', 'Y', 'Z', 'R', 'Q', 'L'],
            'G74':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
            'G76':['P', 'Z', 'I', 'J', 'K', 'Q', 'H', 'E', 'L', '$'],
            'G81':['X', 'Y', 'Z', 'R', 'L'],
            'G82':['X', 'Y', 'Z', 'R', 'L', 'P'],
            'G83':['X', 'Y', 'Z', 'R', 'L', 'Q'],
            'G84':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
            'G85':['X', 'Y', 'Z', 'R', 'L'],
            'G86':['X', 'Y', 'Z', 'R', 'L', 'P', '$'],
            'G89':['X', 'Y', 'Z', 'R', 'L', 'P'],
            'G92':['X', 'Y', 'Z'],
            'G96':['D', 'S', '$'],
            'G97':['S', '$'],}

        desc = {'G0':'Coordinated Motion at Rapid Rate',
            'G1':'Coordinated Motion at Feed Rate',
            'G2':'Coordinated Clockwise Helical Motion at Feed Rate',
            'G3':'Coordinated Counterclockwise Helical Motion at Feed Rate',
            'G4':'Dwell',
            'G5':'Cubic Spline',
            'G5.1':'Quadratic B-Spline',
            'G5.2':'NURBS, add control point',
            'G7':'Diameter Mode (lathe)',
            'G8':'Radius Mode (lathe)',
            'G10L1':'Set Tool Table Entry',
            'G10L2':'Set Tool Table, Calculated, Workpiece',
            'G10L10':'Set Tool Table, Calculated, Fixture',
            'G10L11':'Coordinate System Origin Setting',
            'G10L20':'Coordinate System Origin Setting Calculated',
            'G17':'Plane Select XY',
            'G18':'Plane Select XZ',
            'G19':'Plane Select YZ',
            'G17.1':'Plane Select UV',
            'G17.2':'Plane Select WU',
            'G17.3':'Plane Select VW',
            'G20':'Set Units to Inch',
            'G21':'Set Units to Millimeters',
            'G28':'Go to Predefined Position',
            'G28.1':'Set Predefined Position',
            'G30':'Go to Predefined Position',
            'G30.1':'Set Predefined Position',
            'G33':'Spindle Synchronized Motion',
            'G33.1':'Rigid Tapping',
            'G38.2':'Probing Toward Workpiece, Signal Error',
            'G38.3':'Probing Toward Workpiece',
            'G38.4':'Probing Away Workpiece, Signal Error',
            'G38.5':'Probing Away Workpiece',
            'G40':'Cancel Cutter Compensation',
            'G41':'Cutter Compensation, Left of Programmed Path',
            'G41.1':'Dynamic Cutter Compensation, Left of Programmed Path',
            'G42':'Cutter Compensation, Right of Programmed Path',
            'G42.1':'Dynamic Cutter Compensation, Right of Programmed Path',
            'G43':'Use Tool Length Offset from Tool Table',
            'G43.1':'Dynamic Tool Length Offset',
            'G43.2':'Apply additional Tool Length Offset',
            'G49':'Cancel Tool Length Offset',
            'G52':'Local Coordinate System Offset',
            'G53':'Move in Machine Coordinates',
            'G54':'Select Coordinate System 1',
            'G55':'Select Coordinate System 2',
            'G56':'Select Coordinate System 3',
            'G57':'Select Coordinate System 4',
            'G58':'Select Coordinate System 5',
            'G59':'Select Coordinate System 6',
            'G59.1':'Select Coordinate System 7',
            'G59.2':'Select Coordinate System 8',
            'G59.3':'Select Coordinate System 9',
            'G61':'Exact Path Mode',
            'G61.1':'Exact Stop Mode',
            'G64':'Path Control Mode with Tolerance',
            'G73':'Drilling Cycle with Chip Breaking',
            'G74':'Left-hand Tapping Cycle with Dwell',
            'G76':'Multi-pass Threading Cycle (Lathe)',
            'G80':'Cancel Motion Modes',
            'G81':'Drilling Cycle',
            'G82':'Drilling Cycle with Dwell',
            'G83':'Drilling Cycle with Peck',
            'G84':'Right-hand Tapping Cycle with Dwell',
            'G85':'Boring Cycle, No Dwell, Feed Out',
            'G86':'Boring Cycle, Stop, Rapid Out',
            'G89':'Boring Cycle, Dwell, Feed Out',
            'G90':'Absolute Distance Mode',
            'G90.1':'Absolute Distance Mode IJK Arc Offsets',
            'G91':'Incremental Distance Mode',
            'G91.1':'Incremental Distance Mode IJK Arc Offsets',
            'G92':'Coordinate System Offset',
            'G92.1':'Reset G92 Offsets, Reset Parameters',
            'G92.2':'Reset G92 Offsets, Keep Parameters ',
            'G92.3':'Restore G92 Offsets',
            'G93':'Feed Rate Inverse Time Mode',
            'G94':'Feed Rate Units per Minute Mode',
            'G95':'Feed Rate Units per Revolution Mode',
            'G96':'Spindle Control Constant Surface Speed Mode',
            'G97':'Spindle Control RPM Mode',
            'G98':'Canned Cycle Return Level',
            'G99':'Canned Cycle Return Level',}

        gcodeHelp = {'G0':'Coordinated Motion at Rapid Rate',
            'G1':'Coordinated Motion at Feed Rate',
            'G2':G2,
            'G3':'Coordinated Counterclockwise Helical Motion at Feed Rate',
            'G4':'Dwell',
            'G5':'Cubic Spline',
            'G5.1':'Quadratic B-Spline',
            'G5.2':'NURBS, add control point',
            'G7':'Diameter Mode (lathe)',
            'G8':'Radius Mode (lathe)',
            'G10L1':'Set Tool Table Entry',
            'G10L2':'Set Tool Table, Calculated, Workpiece',
            'G10L10':'Set Tool Table, Calculated, Fixture',
            'G10L11':'Coordinate System Origin Setting',
            'G10L20':'Coordinate System Origin Setting Calculated',
            'G17':'Plane Select XY',
            'G18':'Plane Select XZ',
            'G19':'Plane Select YZ',
            'G17.1':'Plane Select UV',
            'G17.2':'Plane Select WU',
            'G17.3':'Plane Select VW',
            'G20':'Set Units to Inch',
            'G21':'Set Units to Millimeters',
            'G28':'Go to Predefined Position',
            'G28.1':'Set Predefined Position',
            'G30':'Go to Predefined Position',
            'G30.1':'Set Predefined Position',
            'G33':'Spindle Synchronized Motion',
            'G33.1':'Rigid Tapping',
            'G38.2':'Probing Toward Workpiece, Signal Error',
            'G38.3':'Probing Toward Workpiece',
            'G38.4':'Probing Away Workpiece, Signal Error',
            'G38.5':'Probing Away Workpiece',
            'G40':'Cancel Cutter Compensation',
            'G41':'Cutter Compensation, Left of Programmed Path',
            'G41.1':'Dynamic Cutter Compensation, Left of Programmed Path',
            'G42':'Cutter Compensation, Right of Programmed Path',
            'G42.1':'Dynamic Cutter Compensation, Right of Programmed Path',
            'G43':'Use Tool Length Offset from Tool Table',
            'G43.1':'Dynamic Tool Length Offset',
            'G43.2':'Apply additional Tool Length Offset',
            'G49':'Cancel Tool Length Offset',
            'G52':'Local Coordinate System Offset',
            'G53':'Move in Machine Coordinates',
            'G54':'Select Coordinate System 1',
            'G55':'Select Coordinate System 2',
            'G56':'Select Coordinate System 3',
            'G57':'Select Coordinate System 4',
            'G58':'Select Coordinate System 5',
            'G59':'Select Coordinate System 6',
            'G59.1':'Select Coordinate System 7',
            'G59.2':'Select Coordinate System 8',
            'G59.3':'Select Coordinate System 9',
            'G61':'Exact Path Mode',
            'G61.1':'Exact Stop Mode',
            'G64':'Path Control Mode with Tolerance',
            'G73':'Drilling Cycle with Chip Breaking',
            'G74':'Left-hand Tapping Cycle with Dwell',
            'G76':'Multi-pass Threading Cycle (Lathe)',
            'G80':'Cancel Motion Modes',
            'G81':'Drilling Cycle',
            'G82':'Drilling Cycle with Dwell',
            'G83':'Drilling Cycle with Peck',
            'G84':'Right-hand Tapping Cycle with Dwell',
            'G85':'Boring Cycle, No Dwell, Feed Out',
            'G86':'Boring Cycle, Stop, Rapid Out',
            'G89':'Boring Cycle, Dwell, Feed Out',
            'G90':'Absolute Distance Mode',
            'G90.1':'Absolute Distance Mode IJK Arc Offsets',
            'G91':'Incremental Distance Mode',
            'G91.1':'Incremental Distance Mode IJK Arc Offsets',
            'G92':'Coordinate System Offset',
            'G92.1':'Reset G92 Offsets, Reset Parameters',
            'G92.2':'Reset G92 Offsets, Keep Parameters ',
            'G92.3':'Restore G92 Offsets',
            'G93':'Feed Rate Inverse Time Mode',
            'G94':'Feed Rate Units per Minute Mode',
            'G95':'Feed Rate Units per Revolution Mode',
            'G96':'Spindle Control Constant Surface Speed Mode',
            'G97':'Spindle Control RPM Mode',
            'G98':'Canned Cycle Return Level',
            'G99':'Canned Cycle Return Level',}


        text = self.mdiSmartEntry.text() or '0'
        if text != '0':
            if text in words:
                for index, value in enumerate(words[text]):
                    getattr(self, 'gcodeParameter_' + str(index)).setText(value)
            else:
                for index in range(6):
                    getattr(self, 'gcodeParameter_' + str(index)).setText('')
            if text in desc:
                self.gcodeDescription.setText(desc[text])
            else:
                self.gcodeDescription.setText('')
            if text in gcodeHelp:
                self.gcodeHelpLabel.setText(gcodeHelp[text])
            else:
                self.gcodeHelpLabel.setText('')
        else:
            for index in range(6):
                getattr(self, 'gcodeParameter_' + str(index)).setText('')

    def mdiSmartHandleBackSpace(self):
        if len(self.mdiSmartLabel.text()) > 0:
            text = self.mdiSmartLabel.text()[:-1]
            self.mdiSmartLabel.setText(text)

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

