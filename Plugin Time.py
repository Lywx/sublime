import datetime, getpass
import sublime, sublime_plugin
 
class TimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        date = "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.view.run_command("insert_snippet", { "contents": date } )

class TimeListCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        date = "%s" % datetime.datetime.now().strftime("%Y %m %d %H %M %S")
        self.view.run_command("insert_snippet", { "contents": date } )
