class people(object):
    country = "china"
    #静态方法
    @staticmethod
    def getCountry():
        return people.country

p = people()
print(p.getCountry())