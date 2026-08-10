class RegistryMeta(type):
    registry = {}
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name!= "Base":
            cls.registry[name] = new_cls
        return new_cls

class Base(metaclass=RegistryMeta):
    pass

class User(Base): pass
class Admin(Base): pass

print(RegistryMeta.registry) # {'User': <class '__main__.User'>, 'Admin': <class '__main__.Admin'>}