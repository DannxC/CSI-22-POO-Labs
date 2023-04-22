class Example:
    class_attribute = 0

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    # Método de instância
    def instance_method(self):
        print("Método de instância:")
        print(f"  Acessando atributo de instância: {self.instance_attribute}")
        print(f"  Acessando atributo de classe: {self.class_attribute}")

    # Método de classe
    @classmethod
    def class_method(cls):
        print("Método de classe:")
        print(f"  Acessando atributo de classe: {cls.class_attribute}")

    # Método estático
    @staticmethod
    def static_method():
        print("Método estático:")
        print("  Sem acesso direto a atributos de instância ou classe")

# Criando um objeto da classe Example
ex = Example(10)

# Chamando os diferentes tipos de métodos
ex.instance_method()
Example.class_method()
Example.static_method()
