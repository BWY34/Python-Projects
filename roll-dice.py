import os
import random


def clear():
    """Limpa o console do usuário"""

    # Se for windows, executa 'cls', caso contrário, executa 'clear'
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Representação das faces do dado
dices = [
  """
  ---------
  |       |
  |   #   |
  |       |
  ---------
  """,
  """
  ---------
  | #     |
  |       |
  |     # |
  ---------
  """,
  """
  ---------
  | #     |
  |   #   |
  |     # |
  ---------
  """,
  """
  ---------
  | #   # |
  |       |
  | #   # |
  ---------
  """,
  """
  ---------
  | #   # |
  |   #   |
  | #   # |
  ---------
  """,
  """
  ---------
  | # # # |
  |       |
  | # # # |
  ---------
  """
]


while True:
    print("1 - Jogar o dado")
    print("2 - Sair")

    opt = int(input("O que você quer fazer? "))

    if opt == 1:
        number = random.randint(1, 6)
        clear()
        print(f"O resultado é: {number}")
        print(dices[number - 1])
    else:
        break
