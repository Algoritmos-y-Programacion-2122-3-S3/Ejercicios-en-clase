"""1.- Diseñe las clases necesarias para modelar una Valida del 5 y 6, donde la
valida esta compuesta por cierto número de carreras y en cada carrera
participan 6 caballos. Deberá contemplar la creación de cada carrera con
sus correspondientes caballos, además de dar la salida de los caballos,
donde el caballo ganador se generara de forma aleatoria."""


from event import Event
from horses import Horse
from races import Race

def main():
    horse1 = Horse("Rayo","Antonio")
    horse2 = Horse("Centella","Jesus")
    horse3 = Horse("Bolido","Luis")
    horse4 = Horse("A","Isabella")
    horse5 = Horse("B","Camila")
    horse6 = Horse("C","Andres")
    horse_list = [horse1,horse2,horse3,horse4,horse5,horse6]
    print("WELCOME TO THE DERBY OF KENTUCKY")
    race_number = int(input("Please enter how many races you want to see: "))

    for i in range(race_number):
        race = Race(number=i,horses=horse_list)
        race.start()
        race.winner()

main()