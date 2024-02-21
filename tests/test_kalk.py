from main import saskaitisana, atnemsana, reizinasana, dalisana

"""
 def test_saskaitisana():
    if saskaitisana(3, 4) == 7:
        print("Malacis, māki skaitīt :)")
    else:
        print("Vispār nemāki skaitīt")

def test_atnemsana():
    if atnemsana(4, 2.5) == 1.5:
        print("Jau māki atņemt")
    else:
        print("TU PAT ATŅEMT NEMĀKI")
    
test_saskaitisana()
test_atnemsana() """

def test_saskaitisana():
    assert saskaitisana(4, 5) == 9
    assert saskaitisana(-3, 5) == 2
    assert saskaitisana(41.5, 2) == 43.5
    assert saskaitisana(-5, -5) == -10
    assert saskaitisana(6, -5) == 1

def test_atnemsana():
    assert atnemsana(5, 5) == 0
    assert atnemsana(5, -5) == 10
    assert atnemsana(4.5, 6) == -1.5
    assert atnemsana(0, -3) == 3
    assert atnemsana(1, 3) == -2

def test_reizinasana():
    assert reizinasana(-2, -2) == 4
    assert reizinasana(1.5, 5) == 7.5
    assert reizinasana(10, 0.12) == 1.2
    assert reizinasana(0.25, 4) == 1
    assert reizinasana(-3122341414, 0) == 0

def test_dalisana():
    assert dalisana(100, 10) == 10
    assert dalisana(10, 0.1) == 100
    assert dalisana(-10, -10) == 1
    assert dalisana(1100, 0) == "NEVAR DALĪT AR 0 TU AMBĀLI!!!!!!"
    assert dalisana(121, -11) == -11
