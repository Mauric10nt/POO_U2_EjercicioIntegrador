class Medicamento:
    __idCama = None
    __idMedic = None
    __nombComer = None
    __mDroga = None
    __present = None
    __cantApli = None
    __PrecioTotal = None

    def __init__(self, idCama, __idMed, nComer, mdroga, present, cantapli, preciototal):
        self.__idCama = idCama
        self.__idMedic = __idMed
        self.__nombComer = nComer
        self.__mDroga = mdroga
        self.__present = present
        self.__cantApli = cantapli
        self.__PrecioTotal = preciototal
    
    
    def getIdCama(self):
        return self.__idCama
    
    def get__idMed(self):
        return self.__idMedic
    
    def getNombreComercial(self):
        return self.__nombComer
    
    def getMonodroga(self):
        return self.__mDroga
    
    def getPresentacion(self):
        return self.__present
    
    def getCantidadAplicada(self):
        return self.__cantApli
    
    def getPrecioTotal(self):
        return self.__PrecioTotal