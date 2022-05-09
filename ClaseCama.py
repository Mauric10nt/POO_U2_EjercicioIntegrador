class Cama:
    __idCama = None
    __habitacion = None
    __estado = None
    __nombPaciente = None
    __diagnostico = None
    __fechaInter = None
    __fechaAlta = None

    def __init__(self, idCama, habi, estado, nPaciente, diagnostico, fInter, fAlta = None):
        self.__idCama = idCama
        self.__habitacion = habi
        self.__estado = estado
        self.__nombPaciente = nPaciente
        self.__diagnostico = diagnostico
        self.__fechaInter = fInter
        self.__fechaAlta = fAlta
    
    def getNombrePaciente(self):
        return self.__nombPaciente
    
    def getIdCama(self):
        return self.__idCama
    
    def getHabitacion(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getFechaInternacion(self):
        return self.__fechaInter
    
    def getFechaAlta(self):
        return self.__fechaAlta

    def darAltaPaciente(self, fAlta):
        self.__fechaAlta = fAlta
        self.__estado = False
    
    
    def __str__(self):
        cadena = "Paciente: {0:<32} Cama: {1:<5} Habitación: {2:<4}\n".format(self.getNombrePaciente(), self.getIdCama(), self.getHabitacion())
        cadena += "Diagnóstico: {0:<20} Fecha internación: {1:<10}\n".format(self.getDiagnostico(), self.getFechaInternacion())
        cadena += "Fecha de alta: {0:<10}\n".format(self.getFechaAlta())
        return cadena
    