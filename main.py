""" Rotation-Chiffre: Der Text wird in Blöcke geschrieben, um 90° nach rechts gedreht und neu gelesen """

FILLER = 'X'


def prepare_text(text):
    """
    Bereitet einen Text für die Verschlüsselung vor: Leerzeichen entfernen, in Grossbuchstaben umwandeln
    :param text: der Text
    :return: der bereinigte Text, zum Beispiel 'KURZERTEXT' für 'kurzer Text'
    :raises TypeError: wenn der Text kein String ist
    :raises ValueError: wenn der Text leer ist oder andere Zeichen als Buchstaben enthält
    """
    if not isinstance(text, str):
        raise TypeError('Der Text muss ein String sein')
    cleaned = ''.join(text.split()).upper()
    if cleaned == '':
        raise ValueError('Der Text darf nicht leer sein')
    if not cleaned.isalpha():
        raise ValueError('Der Text darf nur Buchstaben enthalten')
    return cleaned


def split_blocks(text, block_length):
    """
    Teilt den Text in Blöcke der angegebenen Länge. Der letzte Block wird mit FILLER aufgefüllt.
    :param text: der bereinigte Text
    :param block_length: die Blocklänge
    :return: eine Liste von Blöcken, zum Beispiel ['KURZE', 'RTEXT']
    :raises TypeError: wenn die Blocklänge keine ganze Zahl ist
    :raises ValueError: wenn die Blocklänge kleiner als 2 oder grösser als die Textlänge ist
    """
    if isinstance(block_length, bool) or not isinstance(block_length, int):
        raise TypeError('Die Blocklänge muss eine ganze Zahl sein')
    if block_length < 2 or block_length > len(text):
        raise ValueError('Die Blocklänge muss zwischen 2 und der Textlänge liegen')
    blocks = []
    for start in range(0, len(text), block_length):
        block = text[start:start + block_length]
        blocks.append(block.ljust(block_length, FILLER))
    return blocks


def rotate_right(blocks):
    """
    Dreht die Blöcke um 90° nach rechts: Aus jeder Spalte wird eine Zeile, von unten nach oben gelesen
    :param blocks: eine Liste von gleich langen Blöcken, zum Beispiel ['KURZE', 'RTEXT']
    :return: die gedrehten Zeilen, zum Beispiel ['RK', 'TU', 'ER', 'XZ', 'TE']
    :raises ValueError: wenn die Liste leer ist oder die Blöcke unterschiedlich lang sind
    """
    if len(blocks) == 0:
        raise ValueError('Es braucht mindestens einen Block')
    block_length = len(blocks[0])
    for block in blocks:
        if len(block) != block_length:
            raise ValueError('Alle Blöcke müssen gleich lang sein')
    rows = []
    for column in range(block_length):
        row = ''
        for block in reversed(blocks):
            row += block[column]
        rows.append(row)
    return rows


def encrypt(plaintext, block_length):
    """
    Verschlüsselt einen Klartext mit der Rotation-Chiffre
    :param plaintext: der Klartext
    :param block_length: die Blocklänge
    :return: der Chiffretext, zum Beispiel 'RKTUERXZTE' für 'kurzer Text' mit Blocklänge 5
    """
    text = prepare_text(plaintext)
    blocks = split_blocks(text, block_length)
    return ''.join(rotate_right(blocks))


def decrypt(ciphertext, block_length):
    """
    Entschlüsselt einen Chiffretext. Aufgefüllte Zeichen (FILLER) bleiben am Ende stehen.
    :param ciphertext: der Chiffretext
    :param block_length: die Blocklänge
    :return: der Klartext in Grossbuchstaben, zum Beispiel 'KURZERTEXT' für 'RKTUERXZTE' mit Blocklänge 5
    :raises TypeError: wenn die Blocklänge keine ganze Zahl ist
    :raises ValueError: wenn die Länge des Chiffretexts kein Vielfaches der Blocklänge ist
    """
    text = prepare_text(ciphertext)
    if isinstance(block_length, bool) or not isinstance(block_length, int):
        raise TypeError('Die Blocklänge muss eine ganze Zahl sein')
    if block_length < 2 or len(text) % block_length != 0:
        raise ValueError('Die Länge des Chiffretexts muss ein Vielfaches der Blocklänge sein')
    row_count = len(text) // block_length
    rotated = [text[start:start + row_count] for start in range(0, len(text), row_count)]
    plaintext = ''
    for row in range(row_count):
        for column in range(block_length):
            plaintext += rotated[column][row_count - 1 - row]
    return plaintext


def main():
    """ Liest einen Klartext und die Blocklänge ein und gibt Chiffretext und Klartext aus """
    plaintext = input('Klartext: ')
    block_length = int(input('Blocklänge: '))
    ciphertext = encrypt(plaintext, block_length)
    print(f'Chiffretext: {ciphertext}')
    print(f'Entschlüsselt: {decrypt(ciphertext, block_length)}')


if __name__ == '__main__':
    main()
