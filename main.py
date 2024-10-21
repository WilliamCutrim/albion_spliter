import discord
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")

# Substitua pelo seu token
TOKEN = config.get('DISCORD_TOKEN')

# Definindo os intents
intents = discord.Intents.default()
intents.message_content = True  # Habilitar acesso ao conteúdo das mensagens

# Definir o prefixo para os comandos do bot, aqui estamos usando "!"
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento para quando o bot estiver online
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Função para dividir valores iguais e incluir o total
def dividir_valores_iguais(dados, valor_externo):
    # Somar os valores da lista original
    total = sum(valor for nome, valor in dados)

    # Somar o valor externo ao total
    total_com_valor_externo = total + valor_externo

    # Calcular a média
    media = total_com_valor_externo / len(dados)

    # Gerar os resultados
    resultados = []
    for nome, valor in dados:
        resultado = media - valor
        resultados.append(f'{nome}: {media:.2f} - {valor} = {resultado:.2f}')
    
    # Adicionar a linha do total
    resultados.append(f'\nTotal com valor externo: {total} + {valor_externo} = {total_com_valor_externo:.2f}')

    return "\n".join(resultados)

# Comando do bot para dividir valores
@bot.command()
async def loot_spliter(ctx, valor_externo: float, *dados_str):
    try:
        # Converter os dados de entrada (formato: nome,valor) para uma lista de tuplas
        dados = []
        for item in dados_str:
            nome, valor = item.split('-')
            dados.append((nome, float(valor)))

        # Chamar a função para calcular os resultados
        resultado = dividir_valores_iguais(dados, valor_externo)

        # Enviar o resultado no canal
        await ctx.send(f"Resultados:\n{resultado}")
    
    except ValueError:
        await ctx.send("Erro: Certifique-se de que os valores estão no formato correto: nome,valor")

# Rodar o bot
bot.run(TOKEN)
