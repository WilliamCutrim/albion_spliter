
# Albion Loot Splitter Bot

Este é um bot de Discord desenvolvido para calcular a divisão de valores entre vários membros, com base em uma lista fornecida. Ele também adiciona um valor externo à soma total e exibe os resultados no Discord.

## Pré-requisitos

Antes de começar, você vai precisar ter as seguintes ferramentas instaladas na sua máquina:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.com/)
- Um editor de texto, como o [Visual Studio Code](https://code.visualstudio.com/)

## Instalação

### 1. Clonar o repositório

Clone o projeto para sua máquina local utilizando o Git:

```bash
git clone <URL do seu repositório>
```

### 2. Criar e ativar um ambiente virtual

Dentro da pasta do projeto, crie um ambiente virtual e o ative:

- **Windows**:
  ```bash
  python -m venv venv
  .env\Scriptsctivate
  ```

- **Linux/macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as dependências

Instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo, substituindo `SEU_TOKEN_AQUI` pelo token do seu bot do Discord:

```
DISCORD_TOKEN=SEU_TOKEN_AQUI
```

> **Nota**: Certifique-se de que o token do bot foi criado no [Discord Developer Portal](https://discord.com/developers/applications).

## Como Executar

Após concluir a instalação, execute o seguinte comando para iniciar o bot:

```bash
python main.py
```

Se tudo estiver correto, o terminal mostrará a mensagem de que o bot está conectado:

```
Bot conectado como albion_loot_spliter#XXXX
```

## Como Usar

No Discord, use o seguinte comando para calcular a divisão de valores entre membros:

```
!dividir <valor_externo> <nome-valor> <nome-valor> ...
```

### Exemplo:

```bash
!dividir 100 Noble-510 cone-480 Curo-500 Pipoka-340 Rafa-470 Zikus-430
```

O bot responderá com algo como:

```
Resultados:
Noble: 471.67 - 510 = -38.33
cone: 471.67 - 480 = -8.33
Curo: 471.67 - 500 = -28.33
Pipoka: 471.67 - 340 = 131.67
Rafa: 471.67 - 470 = 1.67
Zikus: 471.67 - 430 = 41.67

Total com valor externo: 2730 + 100 = 2830.00
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias para o projeto. Para contribuir, siga as etapas abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`).
3. Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin featue/NovaFeature`).
5. Abra um Pull Request.

## Licençar

Este projeto não possui uma licença específica no momento.
