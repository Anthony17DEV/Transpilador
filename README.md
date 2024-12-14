# Transpilador Python para JavaScript

## Descrição
Este é um transpilador que converte códigos escritos em Python para JavaScript. Ele foi desenvolvido para facilitar a migração de códigos entre as duas linguagens e garantir a compatibilidade com aplicações web.

## Recursos Suportados
O transpilador atualmente suporta as seguintes construções da linguagem Python:

### Variáveis
- Declaração e atribuição de variáveis com conversão para `let` no JavaScript.
  ```python
  x = 10
  y = "Olá, mundo"
  z = True
  ```
  Resultado:
  ```javascript
  let x = 10;
  let y = "Olá, mundo";
  let z = true;
  ```

### Funções
- Declaração e chamada de funções com argumentos opcionais.
  ```python
  def saudacao(nome, mensagem="Olá"):
      print(f"{mensagem}, {nome}!")
  ```
  Resultado:
  ```javascript
  function saudacao(nome, mensagem = "Olá") {
      console.log(`${mensagem}, ${nome}!`);
  }
  ```

### Condicionais
- Estruturas `if`, `elif`, e `else` traduzidas para a sintaxe equivalente em JavaScript.
  ```python
  if x > 10:
      print("Maior que 10")
  elif x == 10:
      print("Igual a 10")
  else:
      print("Menor que 10")
  ```
  Resultado:
  ```javascript
  if (x > 10) {
      console.log("Maior que 10");
  } else if (x == 10) {
      console.log("Igual a 10");
  } else {
      console.log("Menor que 10");
  }
  ```

### Loops
- Suporte para `for` com `range` e iteráveis, além de `while`.
  ```python
  for i in range(5):
      print(i)

  nomes = ["Ana", "João", "Maria"]
  for nome in nomes:
      print(f"Olá, {nome}!")
  ```
  Resultado:
  ```javascript
  for (let i = 0; i < 5; i++) {
      console.log(i);
  }

  let nomes = ["Ana", "João", "Maria"];
  for (let nome of nomes) {
      console.log(`Olá, ${nome}!`);
  }
  ```

### Listas e Métodos
- Reconhecimento de métodos de listas como `append`.
  ```python
  resultados = []
  resultados.append("Alto")
  ```
  Resultado:
  ```javascript
  let resultados = [];
  resultados.push("Alto");
  ```

### Operadores Lógicos
- Conversão de operadores como `and`, `or` e `not` para `&&`, `||` e `!`.
  ```python
  if x and not y:
      print("Condição atendida")
  ```
  Resultado:
  ```javascript
  if (x && !y) {
      console.log("Condição atendida");
  }
  ```

## Limitações
O transpilador possui algumas limitações, que incluem:
- **Classes e Herança:** Ainda não há suporte para classes Python.
- **Decoradores:** Não traduz decoradores Python para JavaScript.
- **List Comprehensions:** Ainda não é suportado.

## Requisitos
- Python 3.9 ou superior.

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/Anthony17DEV/Transpilador.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd transpilador-python-js
   ```
3. Execute o transpilador:
   ```bash
   python main.py
   ```

## Como Usar
1. Insira seu código Python no arquivo `teste.py`.
2. Execute o transpilador:
   ```bash
   python main.py
   ```
3. O resultado será gerado no arquivo `output.js`.

## Contribuições
Contribuições são bem-vindas! Por favor, envie um pull request com suas sugestões ou melhorias.

## Contato
Se você tiver dúvidas ou sugestões, entre em contato:
- **Email:** airanthony17@gmail.com
- **GitHub:** [Anthony17DEV](https://github.com/Anthony17DEV)

