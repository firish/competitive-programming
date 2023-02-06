if __name__ == "__main__":
    m = {'HELLO': "ENGLISH", "HOLA": "SPANISH", "HALLO":"GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}
    i = 1
    while True:
        s = input()
        if s == '#': break
        if s in m:
            print(f'Case {i}: {m[s]}')
        else:
            print(f'Case {i}: Unknown')
        i += 1