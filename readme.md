# Projeto calculadora

Minha 1° API 100% individual, uma calculadora que espera um json com a opeção, x e y

## Como utilizar?
Prieiramente precisamos subir o contêiner do Docker, no terminal e dentro da pasta **CALCULADORA** exececute os seguintes comandos

### Docker

1. montar o contêiner 
```python
 sudo docker-compose build
```
2. rodar o contêiner
```python
sudo docker-compose up
```

### Postman

Configurar o Postman é muito simples, precisamos de um método **POST** e utilizamos esta rota aqui
```python
localhost:5000/calc
```

#### Body

No Body nós precisamos utilizar **raw** e **json** para enviar as seguintes informções e do seguinte modo
```python
{
    "function": "add",
    "x":5,
    "y":5
}
```

### Operações

Funciona da seguinte maneira, em ```"function"``` Nós temos quatro operações
- add x + y
- sub x - y
- mult x * y
- div x / y
  