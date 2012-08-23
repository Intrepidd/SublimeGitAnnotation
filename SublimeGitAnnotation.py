import sublime, sublime_plugin

class AnnotationListener(sublime_plugin.EventListener):
  def on_modified(self, view):
    region = view.sel()[0]
    view.add_regions('edited', [region] + view.get_regions('edited'), 'variable.parameter', 'dot')
