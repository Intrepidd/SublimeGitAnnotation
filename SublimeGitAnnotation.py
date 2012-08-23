import sublime, sublime_plugin

class AnnotationListener(sublime_plugin.EventListener):
  def on_modified(self, view):
    print view.size()
