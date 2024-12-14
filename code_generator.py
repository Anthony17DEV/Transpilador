import re

class CodeGenerator:
    def generate(self, code):
        """Converte código Python para JavaScript"""
        replacements = [
            # Variáveis (com 'let')
            (r'^(\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)', r'\1let \2 = \3;'),
            # Definição de funções
            (r'^(\s*)def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\):', r'\1function \2(\3) {'),
            # Retorno
            (r'(\s*)return\s+(.*)', r'\1return \2;'),
            # Comando print
            (r'(\s*)print\((.*?)\)', r'\1console.log(\2);'),
            # Condicional if
            (r'\bif\s*(.+):', r'if (\1) {'),
            # Condicional elif
            (r'\belif\s*(.+):', r'} else if (\1) {'),
            # Condicional else
            (r'\belse:', r'} else {'),
            # Loop for com range
            (r'\bfor\s+(\w+)\s+in\s+range\((.+)\):', r'for (let \1 = 0; \1 < \2; \1++) {'),
            # Loop for com iteráveis
            (r'\bfor\s+(\w+)\s+in\s+(\w+):', r'for (let \1 of \2) {'),
            # Loop while
            (r'\bwhile\s*(.+):', r'while (\1) {'),
            # Substituição de operadores lógicos
            (r'\band\b', '&&'),
            (r'\bor\b', '||'),
            (r'\bnot\b', '!'),
            # Substituição de f-strings
            (r'f\"(.*?)\"', lambda match: self.convert_f_string(match.group(1))),
            # Booleanos
            (r'\bTrue\b', 'true'),
            (r'\bFalse\b', 'false'),
        ]

        # Substituir o código de entrada
        js_code = code
        for pattern, replacement in replacements:
            js_code = re.sub(pattern, replacement, js_code, flags=re.MULTILINE)

        # Adicionar fechamento correto para blocos
        js_code = self.fix_closing_braces(js_code)

        return js_code

    def convert_f_string(self, f_string):
        """Converte f-strings do Python para template literals do JavaScript"""
        # Substitui {variável} por ${variável}
        return '`' + re.sub(r'{(.*?)}', r'${\1}', f_string) + '`'

    def fix_closing_braces(self, code):
        """Fecha corretamente os blocos de código"""
        lines = code.split('\n')
        result = []
        indent_stack = []

        for line in lines:
            stripped = line.strip()
            current_indent = len(line) - len(line.lstrip())

            # Fechar blocos quando a indentação diminui
            while indent_stack and current_indent < indent_stack[-1]:
                result.append(' ' * indent_stack.pop() + '}')

            result.append(line)

            # Abrir novos blocos
            if stripped.endswith('{') and not stripped.startswith('}'):
                indent_stack.append(current_indent)

        # Fechar blocos restantes
        while indent_stack:
            result.append(' ' * indent_stack.pop() + '}')

        return '\n'.join(result)
