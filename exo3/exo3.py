from abc import ABCMeta, abstractmethod

class unmanned_vehicule(metaclass=ABCMeta):
    @abstractmethod
    def mission(self):
        pass

class ground_vehicule(metaclass = ABCMeta):
    @abstractmethod
    def drive(self):
        pass

class underwater_vehicule(metaclass = ABCMeta):
    @abstractmethod
    def sail(self):
        pass

class aerial_vehicule(metaclass = ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class UGV(unmanned_vehicule, ground_vehicule):
    def mission(self):
        print("j'execute les ordres")
    
    def drive(self):
        print("vroom vroom !")
    
class UUV(unmanned_vehicule, underwater_vehicule):
    def mission(self):
        print("j'execute les ordres mais sous l'eau")
    
    def sail(self):
        print("Hello , I'm under the water please help me !")

class UAV(unmanned_vehicule, aerial_vehicule):
    def mission(self):
        print("j'execute les ordres depuis le ciel")
    
    def fly(self):
        print("Je suis high dans le sky !!")


if __name__ == '__main__':
    
    UGVehicule = UGV()
    UUVehicule = UUV()
    UAVehicule = UAV()

    UGVehicule.mission()
    UGVehicule.drive()

    UUVehicule.mission()
    UUVehicule.sail()

    UAVehicule.mission()
    UAVehicule.fly()