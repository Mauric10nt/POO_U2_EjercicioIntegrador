from ClaseManejadorCamas import ManejadorCamas
from ClaseManejadorMedicamentos import ManejadorMedicamentos
from claseMenu import Menu


if __name__ == "__main__":

    unManejadorCamas = ManejadorCamas()
    unManejadorMedicamentos = ManejadorMedicamentos()
    unMenu = Menu()

    unManejadorCamas.cargar("camas.csv")
    unManejadorMedicamentos.cargar("medicamentos.csv")
    unMenu.ejecutarMenu(unManejadorCamas, unManejadorMedicamentos)