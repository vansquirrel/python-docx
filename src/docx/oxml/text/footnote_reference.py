"""Custom element classes related to footnote references (CT_FtnEdnRef)."""

from docx.oxml.xmlchemy import (
    BaseOxmlElement, RequiredAttribute, OptionalAttribute
)
from docx.oxml.simpletypes import (
    ST_DecimalNumber, ST_OnOff
)

class CT_FtnEdnRef(BaseOxmlElement):
    """
    ``<w:footnoteReference>`` element, containing the properties for a footnote reference
    """
    id = RequiredAttribute('w:id', ST_DecimalNumber)
    customMarkFollows = OptionalAttribute('w:customMarkFollows', ST_OnOff)
