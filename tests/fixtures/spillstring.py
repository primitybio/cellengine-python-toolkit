import pytest


@pytest.fixture(scope="session")
def spillstring():
    spillstring = """
    '14,Ax488-A,PE-A,PE-TR-A,PerCP-Cy55-A,PE-Cy7-A,Ax647-A,Ax700-A,Ax750-A,PacBlu-A,Qdot525-
    A,PacOrange-A,Qdot605-A,Qdot655-A,Qdot705-A,1,0.13275251154306414,0.022299626990118084,0
    .004878042437009129,0,0.023414331795661554,0,0.0001045193688180274,0,0.00232054090471367
    06,0,0.0015794832917931567,0,0,0.014120514856008378,1,0.20396581209146827,0.068600613252
    66388,0.005574843072910521,0.006309243886188101,0.0006609691554180386,0.0003004405167904
    172,0.00008003496282569645,0.0017626160950411506,0.10476698396462747,0.05058088553554031
    ,0.014527973484650415,0.0037922424631924175,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0.00179663486166
    19662,0.007212804344713549,0,1,0.16321009952978738,0.21992770547111068,0.399278611141278
    7,0.2678088269888597,0.004329151406987344,0.010822922018408362,0.004328296174818103,0.00
    28867642317136444,0.02669072659509929,0.5006316964230421,0.0035277830203874565,0.0423411
    3386077418,0.009547515616566844,0.00664175690713028,1,0.021108333327899742,0.00728518086
    0798545,0.3453922687555398,0.0009963316107540721,0.0011625273878571583,0.003985057917970
    354,0.004317271735840328,0.0008302206021389921,0.0021586181363940048,0,0.000063403793860
    01867,0.0000836951385606204,0.0009786546586352228,0.0002700164311001327,1,0.130528569869
    7553,0.07888821940265825,0,0,0.00027040048369592155,0,0.000877588608529122,0.00048823727
    034341354,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0.0061797770573503415,
    0.0007270153315273468,0.0010907250874644793,0.00036357794934124843,0.0003635835242425773
    6,0.03697642209421769,0.003272251371442924,0.0013089003597669736,1,0.3301341962836818,0.
    08900525339199582,0.027341699433188493,0.009307740439747515,0.0026178829729397984,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1'
    """

    return spillstring.replace("\n", "").replace("'", "").replace(" ", "")
