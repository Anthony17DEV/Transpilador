import re

class Parser:
    def validate(self, tokens):
        """Valida a sequência de tokens"""
        unsupported = {'TRY', 'EXCEPT', 'CLASS'}
        for token_type, token_value in tokens:
            if token_type in unsupported:
                raise SyntaxError(f"Token não suportado: {token_value}")
        return True

