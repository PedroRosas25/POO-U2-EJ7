from claseviajerofrecuente import ViajeroFrecuente
import csv
class Controlador:
    __viajeros=[]
    def __init__(self):
        self.__viajeros = []
    def crearLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            nro=int(fila[0])
            dni=str(fila[1])
            nom=str(fila[2])
            ape=str(fila[3])
            tmil=int(fila[4])
            viajero=ViajeroFrecuente(nro,dni,nom,ape,tmil)
            self.__viajeros.append(viajero)
    
    def comparar (self): 
        band = True
        numero = 0
        i = 0
        indice = int(input ('Ingrese numero de viajero a comparar millas '))
        while  i < len(self.__viajeros):
            if self.__viajeros[i].getNum() == indice:
                numero = int(input ('Ingrese cantidad de millas para comparar '))
                if (self.__viajeros[i] == numero) == True:
                    print ('Coincide las millas ingresadas con las del viajero ingresado (usando __eq__) ')
                if (numero == self.__viajeros[i]) == True:
                    print ('Coincide las millas ingresadas con las del viajero ingresado (usando __req__) ')    
                
                else : print ('No coinciden las millas ingresadas con las millas del viajero ingresado ')
                break
                       
            i+=1
        if i == len(self.__viajeros) : 
                print ('No se encontro ningun viajero con el numero ingresado ')    
            

    def acumularMillas (self):
        numero = 0
        i = 0
        indice = int(input ('Ingrese numero de viajero a acumular millas '))
        while  i < len(self.__viajeros):
            if self.__viajeros[i].getNum() == indice:
                numero = int(input ('Ingrese cantidad de millas a acumular '))
                print ('Actual cantidad de millas: {} '.format(self.__viajeros[i].retornatotalmillas()))
                self.__viajeros[i] = numero + self.__viajeros[i]
                print ('Nueva cantidad de millas del viajero {}: {} '.format(self.__viajeros[i].getNum(), self.__viajeros[i].retornatotalmillas()))
                break
            i+=1
        else : 
            print ('No se encontro ningun viajero con el numero ingresado ')    
            
    def canjearMillas (self):
        numero = 0
        i = 0
        indice = int(input ('Ingrese numero de viajero a canjear millas '))
        while  i < len(self.__viajeros):
            if self.__viajeros[i].getNum() == indice:
                numero = int(input ('Ingrese cantidad de millas a canjear '))
                print ('Actual cantidad de millas: {} '.format(self.__viajeros[i].retornatotalmillas()))
                self.__viajeros[i] = numero - self.__viajeros[i]
                print ('Nueva cantidad de millas del viajero {}: {} '.format(self.__viajeros[i].getNum(), self.__viajeros[i].retornatotalmillas()))
                break
            i+=1
        else : 
            print ('No se encontro ningun viajero con el numero ingresado ')    
                    