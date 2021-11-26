from django.db import models

class modelo(models.Model):

    pesoc1 = models.FloatField("Peso C1")
    pesoc2 = models.FloatField("Peso C2")
    pesoc3 = models.FloatField("Peso C3")
    pesoc4 = models.FloatField("Peso C4")
    pesoc5 = models.FloatField("Peso C5")

    codigo = models.CharField(primary_key= True, max_length= 5)

class encuesta(models.Model):

# inicio dimension "Uso de Tecnologías digitales"

    choices1 =  (("1", "1-. Las desconozco"), ("2", "2-. algo de conocimiento"), ("3", "3 -.intermedio"), ("4", "4-.conozco"), ("5", "5-.Las conozco muy bien"))
    p1_dim1=models.CharField(" 1-.¿Cuál es el grado de conocimiento de las tecnologías digitales aplicadas a su empresa?", max_length = 1, choices = choices1)

    choices2 = (("1", "1-. no es factible"), ("2", "2-.poco factible"), ("3","3-.factible"), ("4", "4-.en algún momento se considerará"), ("5", "5-.Muy factible"))
    p2_dim1=models.CharField(" 2-.Considerando las necesidades y objetivos en su empresa, ¿Qué tan factible sería invertir en tecnologías digitales?", max_length = 1, choices = choices2)

    choices3 = (("1", "1-.Muy poco o nada"), ("2", "2-. se implementará en algun momento"), ("3","3-.se evalua de vez en cuando "), ("4", "4-. usualmente las utilizamos "), ("5", "5-. siempre los utilizamos"))
    p3_dim1=models.CharField(" 3-.¿Evalúan el uso de tecnologías para la realización de procedimientos cotidianos?", max_length = 1, choices = choices3)

#   fin dimension "Uso de Tecnologías digitales"

############################################################################################################################

# inicio dimension "Planificacion estrategica"

    choices4 = (("1", "1-.Mala disposición"), ("2", "2-.Poca disposición"), ("3", "3 -.intermedio"), ("4", "4-.buena disposición"), ("5", "5-. muy dispuesta"))
    p1_dim2=models.CharField(" 1-.¿Qué tan dispuesta está la empresa a hacer cambio para la transformación digital?", max_length = 1, choices = choices4)

    choices5 = (("1", "1-.Muy poco o nada "), ("2", "2-.no sabemos"), ("3", "3 -.intermedio"), ("4", "4-.existe acceso"), ("5", "5-.hemos accedido a créditos"))
    p2_dim2 = models.CharField(" 2-.¿Qué nivel de acceso tiene la empresa a la banca formal?",max_length=1, choices=choices5)

    choices6 = (("1", "1-.Ninguno"), ("2", "2-.se piensa aplicar"), ("3", "3 -.se esta en proceso"), ("4", "4-.se ha conseguido apoyo"), ("5", "5-.Siempre"))
    p3_dim2 = models.CharField(" 3-.¿En que grado la empresa ha aplicado a proyectos de apoyo gubernamental?",max_length=1, choices=choices6)

    choices7 = (("1", "1-.Muy poco o nada"), ("2", "2-.no sabemos"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p4_dim2 = models.CharField(" 4-.¿En que grado modifica o adapta su modelo de negocios a las nuevas tecnologías?",max_length=1, choices=choices7)

    choices8 = (("1", "1-.Muy poco o nada"), ("2", "2-.no sabemos"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p5_dim2 = models.CharField(" 5-.¿En que grado ha incorporado programas o aplicaciones?",max_length=1, choices=choices8)

    choices9 = (("1", "1-.Muy poco o nada"), ("2", "2-.no sabemos"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p6_dim2 = models.CharField(" 6-.¿En que grado ha incorporado programas o aplicaciones?", max_length=1, choices=choices9)

# fin dimension ""Planificacion estrategica"

############################################################################################################################

# inicio dimension "Procesamiento de datos"

    choices10 = (("1", "1-.Muy poco o nada"), ("2", "2-.se piensa recolectar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p1_dim3 = models.CharField(" 1-.¿ En que grado hacen una recoleccion de datos sobre sus actividades? ", max_length=1, choices=choices10)

    choices11 = (("1", "1-.Muy poco o nada"), ("2", "2-.se piensa analizar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p2_dim3 = models.CharField(" 2-.¿ En que grado se analizan los datos para mejorar en el mercado?", max_length=1,choices=choices11)

    choices12 = (("1", "1-.Muy poco o nada"), ("2", "2-.se piensa consultar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p3_dim3 = models.CharField(" 3-.¿ Consultan datos externos para posicionarse en el mercado?", max_length=1,choices=choices12)

    choices13 = (("1", "1-.Muy poco o nada"), ("2", "2-.se piensa evaluar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p4_dim3 = models.CharField(" 4-.¿Evalúan la utilización de datos para mejorar sus procesos empresariales?", max_length=1,choices=choices13)

# Fin dimension "Procesamiento de datos"


############################################################################################################################


# inicio dimension "Digitalizacion de procesos"

    choices14 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea ejecutar "), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p1_dim4 = models.CharField(" 1-.En cuanto a los procesos de su empresa:  Las labores manuales ahora se ejecutan con dispositivos tecnológicos",max_length=1, choices=choices14)

    choices15 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea usar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p2_dim4 = models.CharField(" 2-.En cuanto a los procesos de su empresa:  Usan programas de gestión de recursos (ERP, CRM, SAP, otros) ?",max_length=1, choices=choices15)

    choices16 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea evaluar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p3_dim4 = models.CharField(" 3-.En cuanto a los procesos de su empresa: Evalúan el uso de tecnologías para uso de agroquímicos, riego, monitoreo, empaquetado, producción, otros procesos ?",max_length=1, choices=choices16)

    choices17 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea monitorear"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p4_dim4 = models.CharField(" 4-.En cuanto a los procesos de su empresa: Hay monitoreo en tiempo real del estado de los procesos ?",max_length=1, choices=choices17)

# Fin dimension "Digitalizacion de procesos"

############################################################################################################################

# inicio dimension "Equipo de trabajo o empleados"

    choices18 = (("1", "1-.Muy poco o nada"), ("2", "2-.no se considera relevante"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p1_dim5 = models.CharField("1-.En cuanto a su empresa y la relación con sus empleados, en que grado considera las habilidades tecnológicas?",max_length=1, choices=choices18)

    choices19 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea contratar"), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p2_dim5 = models.CharField("2-.En cuanto a su empresa y la relación con sus empleados, cuenta con personal calificado en tecnología que cambian la manera de funcionar?",max_length=1, choices=choices19)

    choices20 = (("1", "1-.Muy poco o nada"), ("2", "2-.se planea contratar "), ("3", "3 -.medianamente"), ("4", "4-.casi siempre"), ("5", "5-. siempre"))
    p3_dim5 = models.CharField("5-.En cuanto a su empresa y la relación con sus empleados, Cuenta con personal calificado para resolver problemas digitales?",max_length=1, choices=choices20)

    choices21 = (("1", "1-.Muy bajo"), ("2", "2-.pensamos capacitar "), ("3", "3 -.intermedio"), ("4", "4-.alto"), ("5", "5-. excelente"))
    p4_dim5 = models.CharField("6-.En cuanto a su empresa y la relación con sus empleados, Cuál es el grado de manejo en el uso de tecnologías?",max_length=1, choices=choices21)

# Fin dimension "Equipo de trabajo o empleados"

class resultadodimensiones(encuesta):

    criterio1_1 =models.FloatField("Criterio 1.1")
    criterio2_1 =models.FloatField("Criterio 2.1")
    criterio3_1 =models.FloatField("Criterio 3.1")
    resul_dim1= models.FloatField("Resultado Dimensión 1")

    def get_dimension1(self):
        self.criterio1_1 = int(self.p1_dim1) * 0.315
        self.criterio2_1 = int(self.p2_dim1) * 0.315
        self.criterio3_1 = int(self.p3_dim1) * 0.315

        totaldimension1 = self.criterio1_1+self.criterio2_1+self.criterio3_1
        return totaldimension1

    resul_dim1=property(get_dimension1)

    ###################################################################################################################

    criterio1_2 =models.FloatField("Criterio 1.2")
    criterio2_2 =models.FloatField("Criterio 2.2")
    criterio3_2 =models.FloatField("Criterio 3.2")
    criterio4_2 =models.FloatField("Criterio 4.2")
    criterio5_2 =models.FloatField("Criterio 5.2")
    criterio6_2 =models.FloatField("Criterio 6.2")

    resul_dim2 = models.FloatField("Resultado Dimensión 2")

    def get_dimension2(self):
        self.criterio1_2 = int(self.p1_dim2) * 0.021
        self.criterio2_2 = int(self.p2_dim2) * 0.021
        self.criterio3_2 = int(self.p3_dim2) * 0.021
        self.criterio4_2 = int(self.p4_dim2) * 0.021
        self.criterio5_2 = int(self.p5_dim2) * 0.021
        self.criterio6_2 = int(self.p6_dim2) * 0.021

        totaldimension2 = self.criterio1_2 + self.criterio2_2 + self.criterio3_2 + self.criterio4_2 + self.criterio5_2 +self.criterio6_2
        return totaldimension2

    resul_dim2=property(get_dimension2)

    ###################################################################################################################

    criterio1_3 =models.FloatField("Criterio 1.3")
    criterio2_3 =models.FloatField("Criterio 2.3")
    criterio3_3 =models.FloatField("Criterio 3.3")
    criterio4_3 =models.FloatField("Criterio 4.3")
    criterio5_3 =models.FloatField("Criterio 5.3")
    resul_dim3 = models.FloatField("Resultado Dimensión 3")

    def get_dimension3(self):
        self.criterio1_3 = int(self.p1_dim3) * 0.007
        self.criterio2_3 = int(self.p2_dim3) * 0.007
        self.criterio3_3 = int(self.p3_dim3) * 0.007
        self.criterio4_3 = int(self.p4_dim3) * 0.007

        totaldimension3 = self.criterio1_3 + self.criterio2_3 + self.criterio3_3 + self.criterio4_3
        return totaldimension3

    resul_dim3=property(get_dimension3)

    ###################################################################################################################

    criterio1_4 =models.FloatField("Criterio 1.4")
    criterio2_4 =models.FloatField("Criterio 2.4")
    criterio3_4 =models.FloatField("Criterio 3.4")
    criterio4_4 =models.FloatField("Criterio 4.4")
    resul_dim4 = models.FloatField("Resultado Dimensión 4")

    def get_dimension4(self):
        self.criterio1_4 = int(self.p1_dim4) * 0.009
        self.criterio2_4 = int(self.p2_dim4) * 0.009
        self.criterio3_4 = int(self.p3_dim4) * 0.009
        self.criterio4_4 = int(self.p4_dim4) * 0.009

        totaldimension4 = self.criterio1_4 + self.criterio2_4 + self.criterio3_4 + self.criterio4_4
        return totaldimension4

    resul_dim4=property(get_dimension4)
    ###################################################################################################################

    criterio1_5 =models.FloatField("Criterio 1.5")
    criterio2_5 =models.FloatField("Criterio 2.5")
    criterio3_5 =models.FloatField("Criterio 3.5")
    criterio4_5 =models.FloatField("Criterio 4.5")

    resul_dim5 = models.FloatField("Resultado Dimensión 5")

    def get_dimension5(self):
        self.criterio1_5 = int(self.p1_dim5) * 0.315
        self.criterio2_5 = int(self.p2_dim5) * 0.315
        self.criterio3_5 = int(self.p3_dim5) * 0.315
        self.criterio4_5 = int(self.p4_dim5) * 0.315

        totaldimension5 = self.criterio1_5 + self.criterio2_5 + self.criterio3_5 + self.criterio4_5
        return totaldimension5

    resul_dim5=property(get_dimension5)



