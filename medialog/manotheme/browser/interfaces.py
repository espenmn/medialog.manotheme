from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.portlets.interfaces import IColumn

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Manotheme Theme" theme, this interface must be its layer
       (in manotheme/viewlets/configure.zcml).
    """
    
class IManothemeTopContent(IColumn):
    """we need our own portlet manager in the top area.
    """

class IManothemeFooterContent(IColumn):
    """we need our own portlet manager in the footer area.
        """