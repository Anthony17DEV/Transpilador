import re

class Scanner:
    def tokenize(self, code):
        """Identifica os tokens no código Python"""
        tokens = []
        patterns = [
            (r'\bdef\b', 'DEF'),  # Definição de função
            (r'\breturn\b', 'RETURN'),  # Retorno de função
            (r'\bif\b', 'IF'),  # Condicional if
            (r'\belif\b', 'ELIF'),  # Condicional elif
            (r'\belse\b', 'ELSE'),  # Condicional else
            (r'\bfor\b', 'FOR'),  # Loop for
            (r'\bwhile\b', 'WHILE'),  # Loop while
            (r'\bprint\b', 'PRINT'),  # Comando print
            (r'\bTrue\b', 'BOOLEAN'),  # Boolean True
            (r'\bFalse\b', 'BOOLEAN'),  # Boolean False
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Identificadores
            (r'[0-9]+', 'NUMBER'),  # Números inteiros
            (r'\".*?\"|\'.*?\'', 'STRING'),  # Strings
            (r'\+|-|\*|/|%|==|!=|<|>|<=|>=|=', 'OPERATOR'),  # Operadores
            (r'\.|,', 'DELIMITER'),  # Operador de acesso e vírgulas
            (r'\(|\)|\{|\}|\[|\]|:', 'DELIMITER'),  # Delimitadores
            (r'\s+', None),  # Espaços em branco (ignorar)
        ]

        index = 0
        while index < len(code):
            match = None
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(code, index)
                if match:
                    if token_type:  # Ignorar espaços em branco
                        tokens.append((token_type, match.group(0)))
                    index = match.end()
                    break
            if not match:
                raise SyntaxError(f"Token inválido no código: {code[index:]}")
        return tokens
