menu = input("Elige que conversor quieres usar (CF: Celsius-Fahrenheit | FC: Fahrenheit-Celsius) | DE: Dolar-Euro | ED: Euro-Dolar: ").capitalize()

match menu:
  case CF:
    gradosCF = input("Pon los grados celsius para pasarlos a fahrenheit: ")
    