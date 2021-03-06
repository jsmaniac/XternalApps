import sys

import ExternalAppsList

import StealSplash
StealSplash.steal()

myIcon = """
        /* XPM */
        static char * icon_xpm[] = {
        "16 16 15 1",
        " 	c None",
        ".	c #FFFFFF",
        "+	c #E8E5E5",
        "@	c #897578",
        "#	c #9B8B8D",
        "$	c #75575C",
        "%	c #C9C3C4",
        "&	c #FF89DA",
        "*	c #FF96DA",
        "=	c #FFA2DA",
        "-	c #FFACDA",
        ";	c #FFB2DA",
        ">	c #FFEAF3",
        ",	c #FFB9DA",
        "'	c #FF9DDA",
        "................",
        "..........+@....",
        ".........#$%....",
        "........$$$.....",
        ".......%$$%.....",
        ".......&%.......",
        "......*&........",
        ".....=&.........",
        "....-&.....&....",
        "...;&>....&&....",
        "..,'&.....&&....",
        "..&&.....&..&...",
        ".........&&&&...",
        "........&...&...",
        ".......&.....&..",
        "................"};
        """

class XternalAppsWorkbench(Workbench):
    """Subclasses must implement the appName attribute"""
    global myIcon
    global XternalAppsWorkbench
    global ExternalAppsList

    def __init__(self):
        self.MenuText = "XternalApps: " + self.appName
        self.ToolTip = "Embeds " + self.appName + " in FreeCAD"
        self.Icon = ExternalAppsList.apps[self.appName].Icon
        super(XternalAppsWorkbench, self).__init__()

    def Initialize(self):
        # Load commands
        import AppCommand
        import ToolCommand
        import Embed
        Embed.ExternalApps()
        AppCommand.createCommands(self.appName)
        ToolCommand.createCommands(self.appName)

        # List of commands for this workbench
        self.list = ['ExternalAppsOpen' + self.appName + 'Command'] \
                    + ['ExternalAppsTool' + self.appName + toolName + 'Command'
                       for toolName in ExternalAppsList.apps[self.appName].Tools]

        # Create menus and toolbars
        self.appendMenu("ExternalApplications", self.list)
        self.appendToolbar("ExternalApplications", self.list)

    def Activated(self):
        pass

    def Deactivated(self):
        pass

    #def ContextMenu(self):
    #    pass

    def GetClassName(self):
        return "Gui::PythonWorkbench"

def addAppWorkbench(appName):
    workbenchClass = type(
        "XternalApps" + appName + "Workbench",
        (XternalAppsWorkbench,), { 'appName': appName })
    Gui.addWorkbench(workbenchClass())

for appName in ExternalAppsList.apps:
    addAppWorkbench(appName)
