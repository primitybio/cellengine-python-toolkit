import pytest


@pytest.fixture(scope="session")
def fcsfiles():
    fcsfiles = [
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e79",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "12"},
                {"name": "plate well", "value": "A12"},
            ],
            "eventCount": 898,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A12_A12.fcs",
            "hasFileInternalComp": True,
            "md5": "78df4458fa00a0a2621ce51331fb5fbc",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 94438,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7a",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "02"},
                {"name": "plate well", "value": "A02"},
            ],
            "eventCount": 1025,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A2_A02.fcs",
            "hasFileInternalComp": True,
            "md5": "4a0ddcc46265709d2bc0786ccc52e9a0",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 107131,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7b",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "05"},
                {"name": "plate well", "value": "A05"},
            ],
            "eventCount": 1490,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A5_A05.fcs",
            "hasFileInternalComp": True,
            "md5": "754cd2970e059ad7f391b007588feb90",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 153630,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7c",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "01"},
                {"name": "plate well", "value": "A01"},
            ],
            "eventCount": 415,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A1_A01.fcs",
            "hasFileInternalComp": True,
            "md5": "44b7add508fdfa816c57f8fc9d61f759",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 46131,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7d",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "03"},
                {"name": "plate well", "value": "A03"},
            ],
            "eventCount": 993,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A3_A03.fcs",
            "hasFileInternalComp": True,
            "md5": "7e139fa7cb350deb6f1f180a6290b87f",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 103931,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7e",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "04"},
                {"name": "plate well", "value": "A04"},
            ],
            "eventCount": 936,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A4_A04.fcs",
            "hasFileInternalComp": True,
            "md5": "4e02338052ec43d6ab4cf5ebb98064aa",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 98230,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e7f",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "06"},
                {"name": "plate well", "value": "A06"},
            ],
            "eventCount": 180,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A6_A06.fcs",
            "hasFileInternalComp": True,
            "md5": "da0791509dd29ebca1c5d6d649d11b73",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 22625,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e80",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "07"},
                {"name": "plate well", "value": "A07"},
            ],
            "eventCount": 3027,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A7_A07.fcs",
            "hasFileInternalComp": True,
            "md5": "b29b4a7ac056899cabf566b203493925",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 307329,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e81",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "08"},
                {"name": "plate well", "value": "A08"},
            ],
            "eventCount": 3684,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A8_A08.fcs",
            "hasFileInternalComp": True,
            "md5": "1c5955a05bd3e2b46aa58eec88d494b0",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 373037,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e82",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "09"},
                {"name": "plate well", "value": "A09"},
            ],
            "eventCount": 2196,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A9_A09.fcs",
            "hasFileInternalComp": True,
            "md5": "9156a780c62bd9bc8d4601d6dae03893",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 224229,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e83",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "10"},
                {"name": "plate well", "value": "A10"},
            ],
            "eventCount": 1120,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A10_A10.fcs",
            "hasFileInternalComp": True,
            "md5": "3613a1e91e28bb78da20105654dd779c",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 116631,
        },
        {
            "__v": 0,
            "_id": "5d64abe2ca9df61349ed8e84",
            "annotations": [
                {"name": "plate", "value": "96 Well - V bottom"},
                {"name": "plate row", "value": "A"},
                {"name": "plate column", "value": "11"},
                {"name": "plate well", "value": "A11"},
            ],
            "eventCount": 1135,
            "experimentId": "5d64abe2ca9df61349ed8e78",
            "filename": "Specimen_001_A11_A11.fcs",
            "hasFileInternalComp": True,
            "md5": "34283e8069da17a7315d4c456d3532c6",
            "panel": [
                {"channel": "FSC-A", "index": 1, "reagent": None},
                {"channel": "FSC-H", "index": 2, "reagent": None},
                {"channel": "FSC-W", "index": 3, "reagent": None},
                {"channel": "SSC-A", "index": 4, "reagent": None},
                {"channel": "SSC-H", "index": 5, "reagent": None},
                {"channel": "SSC-W", "index": 6, "reagent": None},
                {"channel": "Blue530-A", "index": 7, "reagent": None},
                {"channel": "Blue695-A", "index": 8, "reagent": None},
                {"channel": "Vio450-A", "index": 9, "reagent": None},
                {"channel": "Vio525-A", "index": 10, "reagent": None},
                {"channel": "Vio585-A", "index": 11, "reagent": None},
                {"channel": "Vio605-A", "index": 12, "reagent": None},
                {"channel": "Vio655-A", "index": 13, "reagent": None},
                {"channel": "Vio710-A", "index": 14, "reagent": None},
                {"channel": "UV450-A", "index": 15, "reagent": None},
                {"channel": "UV530-A", "index": 16, "reagent": None},
                {"channel": "Red670-A", "index": 17, "reagent": None},
                {"channel": "Red730-A", "index": 18, "reagent": None},
                {"channel": "Red780-A", "index": 19, "reagent": None},
                {"channel": "YG582-A", "index": 20, "reagent": None},
                {"channel": "YG610-A", "index": 21, "reagent": None},
                {"channel": "YG670-A", "index": 22, "reagent": None},
                {"channel": "YG710-A", "index": 23, "reagent": None},
                {"channel": "YG780-A", "index": 24, "reagent": None},
                {"channel": "Time", "index": 25, "reagent": None},
            ],
            "panelName": "Panel 1",
            "size": 118131,
        },
    ]
    return fcsfiles
