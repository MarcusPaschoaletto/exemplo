#para abrir no git hurb , comece com clonar com https: copia e cola no vscode na parte inicial como clone githurb.
#ja tem o commit da main ( master) "original", depois abrir um branch
# no icone abaixo da lupa, nos 3 pontos, branch, create branch, so nomear nova branch.

def soma(*args):
    try:
        total = 0
        for n in args:
            total += float(n)
        return total
    except Exception as e:
        print(str(e))
        print(*30)
        




