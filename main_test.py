""" Unit Tests für die Rotation-Chiffre """


# ---------------------------------------------------------------------------
# prepare_text
# ---------------------------------------------------------------------------

def test_prepare_text_valid():
    # TODO: Rufe prepare_text mit 'kurzer Text' auf
    # TODO: Prüfe, dass 'KURZERTEXT' zurückgegeben wird
    assert False


def test_prepare_text_no_string():
    # TODO: Formal falsch: Prüfe mit pytest.raises, dass eine Zahl statt eines Texts
    #       einen TypeError auslöst
    assert False


def test_prepare_text_empty():
    # TODO: Logisch ungültig: Prüfe, dass ein Text nur aus Leerzeichen einen ValueError auslöst
    assert False


def test_prepare_text_invalid_chars():
    # TODO: Logisch ungültig: Prüfe, dass ein Text mit Ziffern oder Sonderzeichen
    #       einen ValueError auslöst
    assert False


# ---------------------------------------------------------------------------
# split_blocks
# ---------------------------------------------------------------------------

def test_split_blocks_valid():
    # TODO: Teile 'KURZERTEXT' in Blöcke der Länge 5
    # TODO: Prüfe, dass ['KURZE', 'RTEXT'] zurückgegeben wird
    assert False


def test_split_blocks_padding():
    # TODO: Teile 'KURZERTEXT' in Blöcke der Länge 4
    # TODO: Prüfe, dass der letzte Block mit 'X' aufgefüllt wird
    assert False


def test_split_blocks_length_no_int():
    # TODO: Formal falsch: Prüfe, dass die Blocklänge '5' (Text) einen TypeError auslöst
    assert False


def test_split_blocks_length_too_small():
    # TODO: Logisch ungültig: Prüfe, dass die Blocklänge 1 einen ValueError auslöst
    assert False


def test_split_blocks_length_too_big():
    # TODO: Logisch ungültig: Prüfe, dass eine Blocklänge grösser als der Text
    #       einen ValueError auslöst
    assert False


# ---------------------------------------------------------------------------
# rotate_right
# ---------------------------------------------------------------------------

def test_rotate_right_valid():
    # TODO: Drehe die Blöcke ['KURZE', 'RTEXT']
    # TODO: Prüfe, dass ['RK', 'TU', 'ER', 'XZ', 'TE'] zurückgegeben wird
    assert False


def test_rotate_right_different_lengths():
    # TODO: Logisch ungültig: Prüfe, dass unterschiedlich lange Blöcke einen ValueError auslösen
    assert False


# ---------------------------------------------------------------------------
# encrypt und decrypt
# ---------------------------------------------------------------------------

def test_encrypt_valid():
    # TODO: Verschlüssle 'kurzer Text' mit Blocklänge 5
    # TODO: Prüfe, dass 'RKTUERXZTE' zurückgegeben wird
    assert False


def test_decrypt_valid():
    # TODO: Entschlüssle 'RKTUERXZTE' mit Blocklänge 5
    # TODO: Prüfe, dass 'KURZERTEXT' zurückgegeben wird
    assert False


def test_decrypt_wrong_length():
    # TODO: Logisch ungültig: Prüfe, dass ein Chiffretext, dessen Länge kein Vielfaches
    #       der Blocklänge ist, einen ValueError auslöst
    assert False


def test_encrypt_decrypt():
    # TODO: Verschlüssle einen eigenen Text und entschlüssle ihn wieder
    # TODO: Prüfe, dass wieder der bereinigte Klartext herauskommt
    #       (Achtung: Ist der letzte Block aufgefüllt, stehen am Ende zusätzliche 'X')
    assert False
