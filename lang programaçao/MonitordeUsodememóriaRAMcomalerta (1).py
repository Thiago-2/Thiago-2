#Monitor de Uso de memória RAM com alerta

import psutil
import time
import os

limite = float(input("Defina o limite de uso de RAM (%): "))

while True:
  memoria = psutil.virtual_memory()

  total = memoria.total / (1024 ** 2)
  usado = memoria.used / (1024 ** 2)
  livre = memoria.available / (1024 ** 2)
  porcentagem_uso = memoria.percent

  os.system('cls' if os.name == 'nt' else 'clear')

  print("=== Monitor de RAM ===")
  print(f"Totaal: {total:.2f} MB")
  print(f"Usado: {usado:.2f} MB")
  print(f"Livre: {livre:.2f} MB")
  print(f"Uso: {porcentagem_uso:.2f}%")

  #Alerta
  if porcentagem_uso > limite:
    print("ALERTA: Uso de Ram acima do limite!")

  time.sleep(2)