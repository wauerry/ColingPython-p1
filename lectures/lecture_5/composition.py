import json
from space import Star


class SpaceObjectExport:
    def export(self, star):
        pass


class ExportJSON(SpaceObjectExport):
    def export(self, star):
        return json.dumps({
            "name": star.name,
            "brightness": star.brightness
        })


class ExportXML(SpaceObjectExport):
    def export(self, star):
        return f"""<?xml version="1.0" encoding="utf-8"?>
<star>
    <name>{star.name}</name>
    <brightness>{star.brightness}</brightness>
</star>
"""


class ExportCSV(SpaceObjectExport):
    def export(self, star):
        return f"{star.name}, {star.brightness}"


class ExStar(Star):
    def __init__(self, name, brightness, exporter):
        super().__init__(name, brightness)
        self._exporter = exporter
        if not isinstance(self._exporter, SpaceObjectExport):
            raise ValueError("Bad exporter", exporter)

    def export(self):
        return self._exporter.export(self)


star_with_export = ExStar("Sun", "1e24", ExportCSV())
print(star_with_export.export())
