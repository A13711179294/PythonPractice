class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls, *args, **kwargs)
        return cls._instance
        pass

class DBoptSingle(DataBaseClass):
    pass

db1=DataBaseClass()
print(id(db1))
db2=DataBaseClass()
print(id(db2))
db3=DataBaseClass()
print(id(db3))
db4=DBoptSingle()
print(id(db1))
db5=DBoptSingle()
print(id(db2))
db6=DBoptSingle()
print(id(db3))