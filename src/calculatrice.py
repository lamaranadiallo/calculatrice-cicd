def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def calculatrice():
    print("Calculatrice simple")
    print("Opérations disponibles : +, -, *, /")
    
    while True:
        try:
            a = float(input("Entrez le premier nombre : "))
            op = input("Entrez l'opération : ")
            b = float(input("Entrez le deuxième nombre : "))
            
            if op == '+':
                resultat = addition(a, b)
            elif op == '-':
                resultat = soustraction(a, b)
            elif op == '*':
                resultat = multiplication(a, b)
            elif op == '/':
                resultat = division(a, b)
            else:
                print("Opération non valide")
                continue
            
            print(f"Résultat : {resultat}")
        except ValueError as e:
            print(f"Erreur : {e}")
        except KeyboardInterrupt:
            print("\nAu revoir !")
            break

if __name__ == "__main__":
    calculatrice()