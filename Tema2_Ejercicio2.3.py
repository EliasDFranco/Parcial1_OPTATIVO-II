class CalculadoraSuma:
        def suma(self, num1 , num2):
            self.num1 = num1 
            self.num2 = num2
            return self.num1 + self.num2
calcular = CalculadoraSuma()
print("La suma de ambos números es de: ", calcular.suma(20, 100))