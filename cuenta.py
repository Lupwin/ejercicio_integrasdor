class Cuenta:
    def __init__(self, titular, monto =0 ):
        self.__nombre = titular
        self.__saldo = monto
       
    @property
    def nombre(self):
        return self.__nombre  
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor  
    
    @property
    def monto(self):
        return self.__saldo
    @monto.setter
    def saldo(self,valor):
        self.__saldo = valor  
    
    @property
    def mostrar(self):
        if Cuenta == Cuenta_joven:
            print(f"Titular:{self.__nombre}") 
            print(f"Saldo:${self.__saldo}")
            print(f"Su bonificación es {(Cuenta_joven.bono)/100}%")
        else:
            print(f"Titular:{self.__nombre}") 
            print(f"Saldo:${self.__saldo}")
          
   
    def depositar(self,deposito):
        if deposito >0:
            self.saldo +=  deposito
            print(f"Cuenta {self.nombre}")
            print(f"Depositado:$ {deposito}")
        else: 
            print("Monto incorrecto, por favor revisar")
    
    def retirar(self,retiro):
        if retiro <self.saldo:
            self.saldo -= retiro
            print(f"Cuenta {self.nombre}")
            print(f"Retirado:$ {retiro}")
        elif retiro > self.saldo and retiro <2.10 *self.saldo:
            self.saldo -= retiro
            print(f"Cuenta {self.nombre}")
            print(f"Retiro realizado:$ {retiro}, debe ${abs(self.saldo)}")
        else:
            print("Monto insuficiente para retirar, intente con un monto menor")

class Cuenta_joven(Cuenta):
    def __init__(self, titular, monto=0,bonificacion=0):
        super().__init__(titular, monto)
        self.__bonificacion = bonificacion
    @property
    def bono(self):
        return self.__bonificacion/100
    
    @bono.setter
    def bono(self,valor):
        self.__bonificacion = (valor/100)
    
    @property
    def mostrar(self):
            print(f"Titular:{self.nombre}") 
            print(f"Saldo:${self.saldo}")
            print(f"Su bonificación es {(self.__bonificacion/100)}%")
    
    
   
        
c1 = Cuenta_joven("Lupwin",100,100)
c2 = Cuenta("Mayerlin")
c1.mostrar
print("este es el bono", c1.bono,"%")
c2.mostrar


#No he podido que el bono se sume al saldo en cta joven