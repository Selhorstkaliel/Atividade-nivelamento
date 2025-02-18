def obter_altura_e_genero():
    pessoas = []
    for i in range(15):
        while True:
            try:
                altura = float(input(f"Digite a altura da pessoa {i+1} (use '.' ou ',' como separador decimal): ").replace(',', '.'))
                genero = input(f"Digite o gênero da pessoa {i+1} (M para Masculino, F para Feminino): ").strip().upper()
                if genero not in ['M', 'F']:
                    raise ValueError("Gênero inválido. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")
                pessoas.append((altura, genero))
                break
            except ValueError as e:
                print(e)
    return pessoas

def analisar_dados(pessoas):
    alturas = [pessoa[0] for pessoa in pessoas]
    alturas_masculinas = [pessoa[0] for pessoa in pessoas if pessoa[1] == 'M']
    contagem_feminina = sum(1 for pessoa in pessoas if pessoa[1] == 'F')

    altura_maxima = max(alturas)
    altura_minima = min(alturas)
    media_altura_masculina = sum(alturas_masculinas) / len(alturas_masculinas) if alturas_masculinas else 0

    print(f"A maior altura do grupo é: {altura_maxima}")
    print(f"A menor altura do grupo é: {altura_minima}")
    print(f"A altura média dos homens no grupo é: {media_altura_masculina}")
    print(f"O número de mulheres no grupo é: {contagem_feminina}")

def main():
    pessoas = obter_altura_e_genero()
    analisar_dados(pessoas)

if __name__ == "__main__":
    main()