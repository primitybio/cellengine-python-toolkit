import pytest


@pytest.fixture(scope="session")
def experiments():
    experiments = [
        {
            "_id": "5d38a6f79fae87499999a74b",
            "name": "pytest_experiment",
            "uploader": {
                "_id": "5d366077a1789f7d6653075c",
                "username": "gegnew",
                "email": "g.egnew@gmail.com",
                "firstName": "Gerrit",
                "lastName": "Egnew",
                "fullName": "Gerrit Egnew",
                "id": "5d366077a1789f7d6653075c",
            },
            "__v": 0,
            "activeCompensation": 0,
            "updated": "2019-08-29T14:40:58.566Z",
            "permissions": [],
            "sortingSpec": {},
            "annotationTableSortColumns": [],
            "annotationValidators": {},
            "annotationNameOrder": [],
            "tags": [],
            "perFileCompensationsEnabled": False,
            "revisions": [],
            "retentionPolicy": {"history": []},
            "locked": False,
            "primaryResearcher": {
                "_id": "5d366077a1789f7d6653075c",
                "username": "gegnew",
                "email": "g.egnew@gmail.com",
                "firstName": "Gerrit",
                "lastName": "Egnew",
                "fullName": "Gerrit Egnew",
                "id": "5d366077a1789f7d6653075c",
            },
            "public": False,
            "deleted": None,
            "deepUpdated": "2019-10-15T09:58:38.224Z",
            "created": "2019-07-24T18:44:07.520Z",
            "comments": [
                {
                    "insert": "\xa0\xa0\xa0First 12 of 96 files from barcoding technical experiment (Primity)\n\n"
                }
            ],
        },
        {
            "_id": "5d5faa686d24fd0bf35129b1",
            "name": "with-reagents",
            "uploader": {
                "_id": "5d366077a1789f7d6653075c",
                "username": "gegnew",
                "email": "g.egnew@gmail.com",
                "firstName": "Gerrit",
                "lastName": "Egnew",
            },
            "updated": "2019-08-23T08:57:25.195Z",
            "permissions": [],
            "sortingSpec": {},
            "annotationTableSortColumns": [],
            "annotationValidators": {},
            "annotationNameOrder": [],
            "tags": [],
            "perFileCompensationsEnabled": False,
            "revisions": [],
            "retentionPolicy": {"history": []},
            "locked": False,
            "primaryResearcher": {
                "_id": "5d366077a1789f7d6653075c",
                "username": "gegnew",
                "email": "g.egnew@gmail.com",
                "firstName": "Gerrit",
                "lastName": "Egnew",
            },
            "public": False,
            "deleted": None,
            "deepUpdated": "2019-09-18T14:26:02.492Z",
            "created": "2019-08-23T08:57:12.313Z",
            "comments": [{"insert": "\n"}],
            "__v": 0,
        },
    ]

    return experiments
