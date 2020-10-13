class Monitor:
    def __init__(self, manufacturer, resolution, price, inch):
        self.manufacturer = manufacturer
        self.resolution = resolution
        self.price = price
        self.inch = inch
    def getCharacteristics(self):
        print("Производитель: ", self.manufacturer)
        print("Разрешение (точек): ", self.resolution)
        print("Цена ($): ", self.price)
        print("Диагональ (в дюймах): ", self.inch)
def switch(argument):
        if(argument == 1): lg = Monitor("LG", 1920*1080, 600, 23)
        if(argument == 2): lg.getCharacteristics()
        if(argument == 3): "March"
        if(argument == 4): "April"
        if(argument == 5): "May"

print("Номера операций:" + "\n" + "1 - запись априорной информации \n2 - режим обучения с учителем \n3 - режим "
                                      "распознавания \n4 - режим распознавания с самообучением \n5 - конец работы с "
                                      "программой")
lg = Monitor("LG", 1920*1080, 600, 23)
lg.getCharacteristics()
num_operation = int(input())
while(num_operation != 5):
    switch(num_operation)