from scanner import Scanner
from parser import Parser
from code_generator import CodeGenerator

class Transpiler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.scanner = Scanner()
        self.parser = Parser()
        self.generator = CodeGenerator()

    def transpile(self):
        with open(self.input_file, 'r') as file:
            code = file.read()

        # Etapa 1: Tokenizar
        tokens = self.scanner.tokenize(code)

        # Etapa 2: Validar
        self.parser.validate(tokens)

        # Etapa 3: Gerar código
        js_code = self.generator.generate(code)

        # Escrever código JavaScript no arquivo de saída
        with open(self.output_file, 'w') as file:
            file.write(js_code)

        print(f"Transpiração concluída! Código gerado em: {self.output_file}")


if __name__ == "__main__":
    input_file = 'teste.py'
    output_file = 'output.js'
    transpiler = Transpiler(input_file, output_file)
    transpiler.transpile()
