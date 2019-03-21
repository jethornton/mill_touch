=============
Configuration
=============

INI Options
^^^^^^^^^^^

.. code-block:: ini

    [DISPLAY]
    VCP = name             # Name of the VCP to use, or a .ui or .yml file.
    THEME = theme          # The Qt theme to use, fusion, windows etc.
    STYLESHEET = style.qss # QSS style sheet file, light.qss or dark.qss.
    SIZE = <W>x<H>         # Initial size of the window in pixels.
    POSITION = <X>x<Y>     # Initial position of the window in pixels.
    FULLSCREEN = bool      # Flag to start with window fullscreen.
    MAXIMIZE = bool        # Flag to start with window maximized.
    HIDE_MENU_BAR = bool   # Hides the menu bar, if present.
    HIDE_STATUS_BAR = bool # Hides the status bar, if present.
    CONFIRM_EXIT = bool    # Whether to show dialog to confirm exit.

    # Application Options
    [APPLICATIONS]
    LOG_LEVEL = level      # One of DEBUG, INFO, WARN, ERROR or CRITICAL.
    LOG_FILE = file        # Specifies the log file.
    CONFIG_FILE = file     # Specifies a machine specific YML config file.
    PREF_FILE = file       # Specifies the preference file.
    PERFMON = bool         # Monitor and log system performance.
    QT_API = api           # Qt Python binding to use, pyqt5 or pyside2.
    COMMAND_LINE_ARGS = <args>

    # VTK_BackPlot Options
    [VTK]
    MACHINE_BOUNDRY = bool # Boolean False to hide the machine boundry
    MACHINE_TICKS = bool   # Boolean False to hide the machine boundry ticks
    MACHINE_LABELS = bool  # Boolean False to hide the machine labels

    PROGRAM_BOUNDRY = bool # Boolean False to hide the program boundry
    PROGRAM_TICKS = bool   # Boolean False to hide the program boundry ticks
    PROGRAM_LABELS = bool  # Boolean False to hide the program labels

