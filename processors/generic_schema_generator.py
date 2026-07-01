import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class schema_row:
    def __init__(self, label, pattern:None, talend_type):
        self.comment = ""
        self.default = ""
        self.key = ""
        self.label = label
        self.length = "-1"
        self.nullable = "true"
        self.originalDbColumnName = label
        self.pattern = pattern
        self.talendType = talend_type
        self.precision = "0"
        self.talendType = talend_type

    def write_xml(self) -> Element[str]:
        column = ET.Element(
            "column",
            {
                "comment": self.comment,
                "default": self.default,
                "key": self.key,
                "label": self.label,
                "length": self.length,
                "nullable": self.nullable,
                "originalDbColumnName": self.originalDbColumnName,
                "pattern": self.pattern,
                "precision": self.precision,
                "talendType": self.talendType
            }
        )

        return column


def create_xml_rows(types_list: list) -> list:
    count = 0
    rows = []

    root = ET.Element("schema")

    for t_type in types_list:
        label, talend_type, pattern = parse_talend_types(t_type)
        row = schema_row(label, talend_type, pattern)
        count += 1
        root.append(row.write_xml())
        rows.append(row)
    ET.indent(root, space="    ")

    ET.ElementTree(root).write(
        "schema.xml",
        encoding="utf-8",
        xml_declaration=True
    )

    return rows

def parse_talend_types(talend_type:str) -> tuple[str, str, str | None]:
    parts = talend_type.split("||", 1)

    if len(parts) == 2:
        left, element3 = parts
    else:
        left = parts[0]
        element3 = ""

    element1, element2 = left.split("&&", 1)

    return element1, element2, element3
