from ClaseMedicamento import Medicamento
import csv

class ManejadorMedicamentos:
    __medicamentos = []

    def __init__(self):
        self.__medicamentos = []
    

    def agregarMedicamento(self, unMedicamento):
        if isinstance(unMedicamento, Medicamento):
            self.__medicamentos.append(unMedicamento)
    

    def cargar(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unMedicamento = Medicamento(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.agregarMedicamento(unMedicamento)
        archivo.close()
    
    def getMedicamentosPorNumeroDeCama(self, numeroCama):
        cadena = "{0:<15}{1:^15}{2:^10}{3:^10}{4:^7}\n".format("Medicamento", "Monodroga", "Presentacion", "Cantidad", "Precio")
        total = 0
        for unMedicamento in self.__medicamentos:
            if unMedicamento.getIdCama() == numeroCama:
                cadena +="{0:<15}{1:^15}{2:^10}{3:^10}{4:^7}\n".format(unMedicamento.getNombreComercial(), unMedicamento.getMonodroga(), unMedicamento.getPresentacion(), unMedicamento.getCantidadAplicada(), unMedicamento.getPrecioTotal())
                total += float(unMedicamento.getPrecioTotal())
        cadena += "Total adeudado:{0:>43.2f}".format(total)
        return cadena