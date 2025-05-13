# === Início de GeradorAtaques.py ===
import importlib
import random
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade

def Regular(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    if Alvos is None:
        Alvos = [AlvoS]
    for Alvo in Alvos:
        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        if I is not None and I != False:
            Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta = I(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

DicionarioAtaques = {

    "Jato de Água": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_de_Agua,
    "Jato Duplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Duplo,
    "Bolhas": lambda: importlib.import_module("Dados.Ataques.Agua").Bolhas,
    "Controle do Oceano": lambda: importlib.import_module("Dados.Ataques.Agua").Controle_do_Oceano,
    "Splash": lambda: importlib.import_module("Dados.Ataques.Agua").Splash,
    "Vasculhar no Rio": lambda: importlib.import_module("Dados.Ataques.Agua").Vasculhar_no_Rio,
    "Golpe de Concha": lambda: importlib.import_module("Dados.Ataques.Agua").Golpe_de_Concha,
    "Gota Pesada": lambda: importlib.import_module("Dados.Ataques.Agua").Gota_Pesada,
    "Bola de Água": lambda: importlib.import_module("Dados.Ataques.Agua").Bola_de_Agua,
    "Cachoeira": lambda: importlib.import_module("Dados.Ataques.Agua").Cachoeira,
    "Jato Triplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Triplo,

    "Tapa": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa,
    "Tapa Especial": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa_Especial,
    "Cabeçada": lambda: importlib.import_module("Dados.Ataques.Normal").Cabeçada,
    "Investida": lambda: importlib.import_module("Dados.Ataques.Normal").Investida,
    "Vasculhar": lambda: importlib.import_module("Dados.Ataques.Normal").Vasculhar,
    "Ataque Rápido": lambda: importlib.import_module("Dados.Ataques.Normal").Ataque_Rapido,
    "Provocar": lambda: importlib.import_module("Dados.Ataques.Normal").Provocar,
    "Energia": lambda: importlib.import_module("Dados.Ataques.Normal").Energia,
    "Arranhar": lambda: importlib.import_module("Dados.Ataques.Normal").Arranhar,
    "Crescer": lambda: importlib.import_module("Dados.Ataques.Normal").Crescer,
    "Esbravejar": lambda: importlib.import_module("Dados.Ataques.Normal").Esbravejar,
    "Esmagar": lambda: importlib.import_module("Dados.Ataques.Normal").Esmagar,
    "Descansar": lambda: importlib.import_module("Dados.Ataques.Normal").Descansar,
    "Canto Alegre": lambda: importlib.import_module("Dados.Ataques.Normal").Canto_Alegre,

    "Sopro do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Sopro_do_Dragao,
    "Garra do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Garra_do_Dragao,
    "Ultraje": lambda: importlib.import_module("Dados.Ataques.Dragao").Ultraje,
    "Cauda Violenta": lambda: importlib.import_module("Dados.Ataques.Dragao").Cauda_Violenta,
    "Investida do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Investida_do_Dragao,

    "Faisca": lambda: importlib.import_module("Dados.Ataques.Eletrico").Faisca,
    "Energizar": lambda: importlib.import_module("Dados.Ataques.Eletrico").Energizar,
    "Eletrólise Hidrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Eletrolise_Hidrica,
    "Choque do Trovão": lambda: importlib.import_module("Dados.Ataques.Eletrico").Choque_do_Trovao,
    "Onda Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Onda_Eletrica,
    "Bola Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Bola_Eletrica,
    "Tempestade de Raios": lambda: importlib.import_module("Dados.Ataques.Eletrico").Tempestade_de_Raios,

    "Queimar": lambda: importlib.import_module("Dados.Ataques.Fogo").Queimar,
    "Bola de Fogo": lambda: importlib.import_module("Dados.Ataques.Fogo").Bola_de_Fogo,
    "Superaquecer": lambda: importlib.import_module("Dados.Ataques.Fogo").Superaquecer,
    "Brasa": lambda: importlib.import_module("Dados.Ataques.Fogo").Brasa,
    "Ondas de Calor": lambda: importlib.import_module("Dados.Ataques.Fogo").Ondas_de_Calor,
    "Raio de Fogo": lambda: importlib.import_module("Dados.Ataques.Fogo").Raio_de_Fogo,
    "Ataque de Chamas": lambda: importlib.import_module("Dados.Ataques.Fogo").Ataque_de_Chamas,
    "Laser Incandescente": lambda: importlib.import_module("Dados.Ataques.Fogo").Laser_Incandescente,

    "Cristalizar": lambda: importlib.import_module("Dados.Ataques.Gelo").Cristalizar,
    "Reinado de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Reinado_de_Gelo,
    "Magia de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Magia_de_Gelo,
    "Raio de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Raio_de_Gelo,
    "Gelo Verdadeiro": lambda: importlib.import_module("Dados.Ataques.Gelo").Gelo_Verdadeiro,

    "Brilho": lambda: importlib.import_module("Dados.Ataques.Fada").Brilho,
    "Vento Fada": lambda: importlib.import_module("Dados.Ataques.Fada").Vento_Fada,
    "Benção": lambda: importlib.import_module("Dados.Ataques.Fada").Bençao,
    "Busca Alegre": lambda: importlib.import_module("Dados.Ataques.Fada").Busca_Alegre,
    "Tapa das Fadas": lambda: importlib.import_module("Dados.Ataques.Fada").Tapa_das_Fadas,
    "Constelação Mágica": lambda: importlib.import_module("Dados.Ataques.Fada").Constelaçao_Magica,
    "Explosão Lunar": lambda: importlib.import_module("Dados.Ataques.Fada").Explosao_Lunar,

    "Mordida": lambda: importlib.import_module("Dados.Ataques.Inseto").Mordida,
    "Seda": lambda: importlib.import_module("Dados.Ataques.Inseto").Seda,
    "Picada": lambda: importlib.import_module("Dados.Ataques.Inseto").Picada,
    "Minhocagem": lambda: importlib.import_module("Dados.Ataques.Inseto").Minhocagem,
    "Coleta": lambda: importlib.import_module("Dados.Ataques.Inseto").Coleta,
    "Tesoura X": lambda: importlib.import_module("Dados.Ataques.Inseto").Tesoura_X,
    "Dor Falsa": lambda: importlib.import_module("Dados.Ataques.Inseto").Dor_Falsa,

    "Assombrar": lambda: importlib.import_module("Dados.Ataques.Fantasma").Assombrar,
    "Lambida": lambda: importlib.import_module("Dados.Ataques.Fantasma").Lambida,
    "Atravessar": lambda: importlib.import_module("Dados.Ataques.Fantasma").Atravessar,
    "Coleta Gananciosa": lambda: importlib.import_module("Dados.Ataques.Fantasma").Coleta_Gananciosa,
    "Mão Espectral": lambda: importlib.import_module("Dados.Ataques.Fantasma").Mao_Espectral,
    "Maldade": lambda: importlib.import_module("Dados.Ataques.Fantasma").Maldade,
    "Massacre Fantasmagórico": lambda: importlib.import_module("Dados.Ataques.Fantasma").Massacre_Fantasmagorico,
    "Vasculhada Trapaceira": lambda: importlib.import_module("Dados.Ataques.Fantasma").Vasculhada_Trapaceira,

    "Soco": lambda: importlib.import_module("Dados.Ataques.Lutador").Soco,
    "Chamar para Briga": lambda: importlib.import_module("Dados.Ataques.Lutador").Chamar_para_Briga,
    "Punho Míssil": lambda: importlib.import_module("Dados.Ataques.Lutador").Punho_Missil,
    "Combate Próximo": lambda: importlib.import_module("Dados.Ataques.Lutador").Combate_Proximo,
    "Submissão": lambda: importlib.import_module("Dados.Ataques.Lutador").Submissão,
    "Treinar": lambda: importlib.import_module("Dados.Ataques.Lutador").Treinar,

    "Reforçar": lambda: importlib.import_module("Dados.Ataques.Metal").Reforçar,
    "Cauda de Ferro": lambda: importlib.import_module("Dados.Ataques.Metal").Cauda_de_Ferro,
    "Projétil Metálico": lambda: importlib.import_module("Dados.Ataques.Metal").Projetil_Metalico,
    "Barragem": lambda: importlib.import_module("Dados.Ataques.Metal").Barragem,
    "Broca Perfuradora": lambda: importlib.import_module("Dados.Ataques.Metal").Broca_Perfuradora,
    
    "Pedregulho": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedregulho,
    "Pedra Especial": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedra_Especial,
    "Barragem Rochosa": lambda: importlib.import_module("Dados.Ataques.Pedra").Barragem_Rochosa,
    "Impacto Rochoso": lambda: importlib.import_module("Dados.Ataques.Pedra").Impacto_Rochoso,
    "Pedra Colossal": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedra_Colossal,
    "Fúria Pétrea": lambda: importlib.import_module("Dados.Ataques.Pedra").Furia_Petrea,

    "Arremesso de Terra": lambda: importlib.import_module("Dados.Ataques.Terrestre").Arremesso_de_Terra,
    "Tremor": lambda: importlib.import_module("Dados.Ataques.Terrestre").Tremor,
    "Quebra Chão": lambda: importlib.import_module("Dados.Ataques.Terrestre").Quebra_Chao,
    "Afinidade Territorial": lambda: importlib.import_module("Dados.Ataques.Terrestre").Afinidade_Territorial,
    "Osso Veloz": lambda: importlib.import_module("Dados.Ataques.Terrestre").Osso_Veloz,
    "Golpe Territorial": lambda: importlib.import_module("Dados.Ataques.Terrestre").Golpe_Territorial,
    "Terremoto": lambda: importlib.import_module("Dados.Ataques.Terrestre").Terremoto,

    "Confusão": lambda: importlib.import_module("Dados.Ataques.Psiquico").Confusão,
    "Bola Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Bola_Psiquica,
    "Teleporte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Teleporte,
    "Ampliação Mental": lambda: importlib.import_module("Dados.Ataques.Psiquico").Ampliação_Mental,
    "Psíquico Desgastante": lambda: importlib.import_module("Dados.Ataques.Psiquico").Psiquico_Desgastante,
    "Mente Forte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Mente_Forte,
    "Psicorte Duplo": lambda: importlib.import_module("Dados.Ataques.Psiquico").Psicorte_Duplo,
    "Corrosão Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Corrosao_Psiquica,
    "Tranferência Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Transferencia_Psiquica,
    "Teletransporte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Teletransporte,
    "Raio Psíquico": lambda: importlib.import_module("Dados.Ataques.Psiquico").Raio_Psiquico,
    "Agonia Mental": lambda: importlib.import_module("Dados.Ataques.Psiquico").Agonia_Mental,

    "Nas Sombras": lambda: importlib.import_module("Dados.Ataques.Sombrio").Nas_Sombras,
    "Bola Sombria": lambda: importlib.import_module("Dados.Ataques.Sombrio").Bola_Sombria,
    "Corte Noturno": lambda: importlib.import_module("Dados.Ataques.Sombrio").Corte_Noturno,
    "Confronto Trevoso": lambda: importlib.import_module("Dados.Ataques.Sombrio").Confronto_Trevoso,

    "Voar": lambda: importlib.import_module("Dados.Ataques.Voador").Voar,
    "Ataque de Asa": lambda: importlib.import_module("Dados.Ataques.Voador").Ataque_de_Asa,
    "Investida Aérea": lambda: importlib.import_module("Dados.Ataques.Voador").Investida_Aerea,
    "Rasante": lambda: importlib.import_module("Dados.Ataques.Voador").Rasante,
    "Bico Broca": lambda: importlib.import_module("Dados.Ataques.Voador").Bico_Broca,
    "Vento Forte": lambda: importlib.import_module("Dados.Ataques.Voador").Vento_Forte,

    "Envenenar": lambda: importlib.import_module("Dados.Ataques.Veneno").Envenenar,
    "Ácido": lambda: importlib.import_module("Dados.Ataques.Veneno").Acido,
    "Bomba de Lodo": lambda: importlib.import_module("Dados.Ataques.Veneno").Bomba_de_Lodo,
    "Extração": lambda: importlib.import_module("Dados.Ataques.Veneno").Extraçao,

    "Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Dreno,
    "Disparo de Semente": lambda: importlib.import_module("Dados.Ataques.Planta").Disparo_de_Semente,
    "Chicote de Vinha": lambda: importlib.import_module("Dados.Ataques.Planta").Chicote_de_Vinha,
    "Cura Natural": lambda: importlib.import_module("Dados.Ataques.Planta").Cura_Natural,
    "Raio Solar": lambda: importlib.import_module("Dados.Ataques.Planta").Raio_Solar,
    "Dança das Pétalas": lambda: importlib.import_module("Dados.Ataques.Planta").Dança_das_Petalas,
    "Mega Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Mega_Dreno,
    "Folha Navalha": lambda: importlib.import_module("Dados.Ataques.Planta").Folha_Navalha,
    "Morteiro de Pólem": lambda: importlib.import_module("Dados.Ataques.Planta").Morteiro_de_Polem,

}

def SelecionaAtaques(ataque):
    return DicionarioAtaques[ataque]()


# === Fim de GeradorAtaques.py ===

# === Início de GeradorOutros.py ===
import random
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
from Geradores.GeradorPokemon import Pokemons_Todos
from Dados.itens import Pokebolas_Todas,Estadios_Todos,Amplificadores_Todos,Frutas_Todas,Outros_Todos, Poçoes_Todas
from Dados.Estadios import Estadios


Pokebolas_disponiveis  = Pokebolas_Todas
Estadios_disponiveis = Estadios_Todos
Amplificadores_disponiveis = Amplificadores_Todos
Frutas_disponiveis = Frutas_Todas
Poçoes_disponiveis = Poçoes_Todas
Outros_disponiveis = Outros_Todos

Pokedex = Pokemons_Todos

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "preta"]

class Baralho:
    def __init__(self):
        self.pokemons = []
        self.pokebolas = []
        self.frutas = []
        self.amplificadores = []
        self.estadios = []
        self.poçoes = []
        self.outros = []

        for pokebola in Pokebolas_disponiveis:
            for _ in range(pokebola["quantidade"]):
                self.pokebolas.append(pokebola)

        for fruta in Frutas_disponiveis:
            for _ in range(fruta["quantidade"]):
                self.frutas.append(fruta)

        for amplificador in Amplificadores_disponiveis:
            for _ in range(amplificador["quantidade"]):
                self.amplificadores.append(amplificador)

        for estadio in Estadios_disponiveis:
            for _ in range(estadio["quantidade"]):
                self.estadios.append(estadio)

        for poçao in Poçoes_disponiveis:
            for _ in range(poçao["quantidade"]):
                self.poçoes.append(poçao)

        for outro in Outros_disponiveis:
            for _ in range(outro["quantidade"]):
                self.outros.append(outro)
        
        self.baralho = self.pokebolas + self.amplificadores + self.frutas + self.poçoes + self.estadios + self.outros
        self.Comuns = []
        self.Incomuns = []
        self.Raros = []
        self.Lendarios = []

        self.PokeComuns = []
        self.PokeIncomuns = []
        self.PokeRaros = []
        self.PokeEpicos = []
        self.PokeMiticos = []
        self.PokeLendarios = []

        for item in self.baralho:
            if item["raridade"] == "Comum":
                self.Comuns.append(item)
            elif item["raridade"] == "Incomum":
                self.Incomuns.append(item)
            elif item["raridade"] == "Raro":
                self.Raros.append(item)
            elif item["raridade"] == "Lendario":
                self.Lendarios.append(item)
        
        for pokemon in Pokedex:
            if pokemon != 0:
                if pokemon["raridade"] == "Comum":
                    self.PokeComuns.append(pokemon)
                elif pokemon["raridade"] == "Incomum":
                    self.PokeIncomuns.append(pokemon)
                elif pokemon["raridade"] == "Raro":
                    self.PokeRaros.append(pokemon)
                elif pokemon["raridade"] == "Epico":
                    self.PokeEpicos.append(pokemon)
                elif pokemon["raridade"] == "Mitico":
                    self.PokeMiticos.append(pokemon)
                elif pokemon["raridade"] == "Lendario":
                    self.PokeLendarios.append(pokemon)

    def Tira_item(self,item):
        if item["raridade"] == "Comum":
            self.Comuns.remove(item)
        elif item["raridade"] == "Incomum":
            self.Incomuns.remove(item)
        elif item["raridade"] == "Raro":
            self.Raros.remove(item)
        elif item["raridade"] == "Lendario":
            self.Lendarios.remove(item)

    def devolve_item(self,item):
            if item["raridade"] == "Comum":
                self.Comuns.append(item)
            elif item["raridade"] == "Incomum":
                self.Incomuns.append(item)
            elif item["raridade"] == "Raro":
                self.Raros.append(item)
            elif item["raridade"] == "Lendario":
                self.Lendarios.append(item)
    
    def devolve_pokemon(self,pokemon):
        if pokemon["raridade"] == "Comum":
            self.PokeComuns.append(pokemon)
        elif pokemon["raridade"] == "Incomum":
            self.PokeIncomuns.append(pokemon)
        elif pokemon["raridade"] == "Raro":
            self.PokeRaros.append(pokemon)
        elif pokemon["raridade"] == "Epico":
            self.PokeEpicos.append(pokemon)
        elif pokemon["raridade"] == "Mitico":
            self.PokeMiticos.append(pokemon)
        elif pokemon["raridade"] == "Lendario":
            self.PokeLendarios.append(pokemon)

def spawn_do_centro(centro,Baralho,turnos):

    if turnos < 4:
        raridades = { "Comum": 45, "Incomum": 40, "Raro": 13, "Epico": 2, "Mitico": 0, "Lendario": 0 }

    elif turnos < 8:
        raridades = { "Comum": 35, "Incomum": 35, "Raro": 20, "Epico": 7, "Mitico": 3, "Lendario": 0 }

    elif turnos < 15:
        raridades = { "Comum": 28, "Incomum": 28, "Raro": 25, "Epico": 12, "Mitico": 5, "Lendario": 2}
    
    else:
        raridades = { "Comum": 18, "Incomum": 20, "Raro": 22, "Epico": 20, "Mitico": 13, "Lendario": 7}


    baralhos_por_raridade = {
        "Comum": Baralho.PokeComuns,
        "Incomum": Baralho.PokeIncomuns,
        "Raro": Baralho.PokeRaros,
        "Epico": Baralho.PokeEpicos,
        "Mitico": Baralho.PokeMiticos,
        "Lendario": Baralho.PokeLendarios
    }
    
    def spawn(centro,i):
        raridade_escolhida = random.choices(
                population=["Comum", "Incomum", "Raro", "Epico", "Mitico", "Lendario"],
                weights=[raridades["Comum"], raridades["Incomum"], raridades["Raro"], raridades["Epico"], raridades["Mitico"], raridades["Lendario"]],
                k=1
            )[0]
        
        BaralhoEscolhido = baralhos_por_raridade[raridade_escolhida]
        if BaralhoEscolhido == []:
            return
        centro[i] = random.choice(BaralhoEscolhido)
        GV.adicionar_mensagem(f"Um {centro[i]["nome"]} selvagem apareceu")
        BaralhoEscolhido.remove(centro[i])
    
    def despawn(centro,i):
        GV.adicionar_mensagem(f"Um {centro[i]["nome"]} selvagem desapareceu")
        Baralho.devolve_pokemon(centro[i])
        centro[i] = None

    for i,slot in enumerate(centro):
        if slot is not None:
            if random.choice([1,2,3,4]) == 1:
                despawn(centro,i)
                break

    pokemonsSpawn = 0
    for i,slot in enumerate(centro):
        if pokemonsSpawn == 2:
            break
        if slot is None:
            if random.choice([1,2,3]) == 1:
                spawn(centro,i)
                pokemonsSpawn += 1

    return centro

def Compra_Energia(player,custo=0):
    if player.ouro >= custo:
        tocar("Energia")
        player.ouro -= custo
        energia_sorteada = random.choice(Energias)
        player.energias[energia_sorteada] += 1
        energia_sorteada = random.choice(Energias)
        player.energias[energia_sorteada] += 1
    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Sem ouro para comprar energias")
        

def Gera_item(Lista,Baralho):
        item = random.choice(Lista)
        Baralho.tira_item(item)
        return item

def coletor():
    energia_sorteada = random.choice(Energias)
    return energia_sorteada

def Gera_Mapa(i):
    return Mapa(Estadios[i])

def Gera_Baralho():
    return Baralho()

class Mapa:
    def __init__(self, Info):
        self.tempo = Info["Tempo"]
        self.area = Info["zona"]
        self.cores = Info["cores"]
        self.PlojaI = Info["LojaItens"]
        self.PlojaP = Info["LojaPokebolas"]
        self.PlojaE = Info["LojaEnergias"]
        self.PlojaA = Info["LojaAmplificadores"]
        self.pLojaT = Info["LojaTreEst"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]

    def MudarEstagio(self,i):
        
        Info = Estadios[i]

        self.tempo = Info["Tempo"]
        self.area = Info["zona"]
        self.cores = Info["cores"]
        self.PlojaI = Info["LojaItens"]
        self.PlojaP = Info["LojaPokebolas"]
        self.PlojaE = Info["LojaEnergias"]
        self.PlojaA = Info["LojaAmplificadores"]
        self.pLojaT = Info["LojaTreEst"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]


# === Fim de GeradorOutros.py ===

# === Início de GeradorPlayer.py ===
from Geradores.GeradorPokemon import Gerador_final
from Visual.Sonoridade import tocar
from Jogo.Abas import Trocar_Ataque_Pergunta
from Geradores.GeradorOutros import Pokebolas_disponiveis,coletor
import Visual.GeradoresVisuais as GV

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1],1,self)]
        self.inventario = []
        self.energias = {"vermelha": 10, "azul": 10, "amarela": 10, "verde": 10, "roxa": 10, "laranja": 10, "preta": 10}
        self.energiasDesc = []
        self.ouro = 10
    
    def usar_item(self,item,Pokemon,tela,Mapa,ataque,EstadoDaPergunta, Baralho):
            if item["classe"] in ["pokebola", "fruta"]:
                tocar("Bloq")
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            tocar("Usou")
                            Baralho.devolve_item(item)
                            self.inventario.remove(item)
                            Pokemon.curar(cura,self,tela)
                            return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser curados")
                elif item["classe"] in ["amplificador"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            tipo = item["aumento"]
                            if tipo == "Evolucional":
                                Pokemon.FormaFinal(item,self)
                            elif tipo == "XP":
                                Pokemon.Ganhar_XP(5,self)
                                GV.adicionar_mensagem(f"{Pokemon.nome} Ganhou 5 de XP")
                                Baralho.devolve_item(item)
                                self.inventario.remove(item)
                                return
                            elif Pokemon.amplificações > 5:
                                GV.adicionar_mensagem("Esse pokemon já atingiu 6 amplificações")
                                return
                            else:
                                tocar("Usou")
                                Baralho.devolve_item(item)
                                self.inventario.remove(item)
                                Pokemon.amplificar(tipo,tela,self)
                                return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser amplificados")
                elif item["classe"] == "estadio":
                    tocar("Usou")
                    Mapa.MudarEstagio(item["ST Code"])
                    Baralho.devolve_item(item)
                    self.inventario.remove(item)
                    return
                elif item["classe"] == "Outros":
                    if item["nome"] == "Trocador de Ataque" and ataque is not None:
                        tocar("Usou")
                        Trocar_Ataque_Pergunta(Pokemon,ataque,EstadoDaPergunta)
                        Baralho.devolve_item(item)
                        self.inventario.remove(item)
                        return
                    else:
                        tocar("Bloq")
                        GV.adicionar_mensagem("selecione um ataque para usar um item")
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("selecione um pokemon para usar um item")
    
    def vender_item(self,item,Baralho):
        self.ouro += item["preço"] // 2
        self.inventario.remove(item)
        Baralho.devolve_item(item)

    def ganhar_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def muda_descarte(self,energia):
        if energia in self.energiasDesc:
            self.energiasDesc.remove(energia)
        else:
            self.energiasDesc.append(energia)

    def ganhar_item(self,item,Baralho):
            if len(self.inventario) < 13:
                self.inventario.append(item)
                return True
            else:
                GV.adicionar_mensagem("Inventário cheio")
                self.ouro += item["preço"]
                Baralho.devolve_item(item)
                return False

def Gerador_player(informaçoes):
    return Jogador(informaçoes)


# === Fim de GeradorPlayer.py ===

# === Início de GeradorPokemon.py ===
import Visual.GeradoresVisuais as GV
import random
import Jogo.Funções2 as FU
from Dados.Gen1.Basicos import Pokemons_Todos
from Visual.Mensagens import adicionar_mensagem_passageira
from Visual.Imagens import Carrega_Icone_pokemon
from Visual.Sonoridade import tocar
from Visual.Efeitos import adicionar_efeito
from Jogo.Tabuleiro import GuardarPosicionar
from Jogo.Partida import VerificaGIF
from Geradores.GeradorAtaques import SelecionaAtaques
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30,Fonte35, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

EfeitosNegativos = {
    "Confuso": 0,
    "Bloqueado": 0,
    "Envenenado": 0,
    "Tóxico": 0,
    "Fragilizado": 0,
    "Quebrado": 0,
    "Congelado": 0,
    "Queimado": 0,
    "Paralisado": 0,
    "Encharcado": 0,
    "Vampirico": 0,
    "Descarregado": 0,
    "Enfraquecido": 0,
    "Incapacitado": 0 
    }

EfeitosPositivos = {
    "Regeneração": 0,
    "Abençoado": 0,
    "Imune": 0, 
    "Preparado": 0,
    "Provocando": 0,
    "Furtivo": 0,
    "Voando": 0,
    "Ofensivo": 0,
    "Reforçado": 0,
    "Imortal": 0,
    "Refletir": 0,
    "Focado": 0,
    "Velocista": 0,
    "Energizado": 0,
    }

EfeitosDescrição = {
    "Regeneração": "Cura 15 de vida por turno",
    "Abençoado": "Aumenta 30% da cura",
    "Imune": "Não pode receber efeitos negativos", 
    "Preparado": "bloqueia e contra ataca com valores baseados na velocidade",
    "Provocando": "Sempre é o alvo",
    "Furtivo": "Não pode ser um alvo",
    "Voando": "Ataques contra voce tem -50 assertividade",
    "Ofensivo": "Mais 30% de ataques",
    "Reforçado": "Mais 30% de defesas",
    "Imortal": "Não pode ser nocauteado",
    "Refletir": "Recebe apenas 20% do dano, o resto reflete",
    "Focado": "Sempre mais 50 assertividade",
    "Velocista": "Mais 50% de velocidade",
    "Energizado": "Precisa de só uma energia para atacar",
    "Confuso": "Menos 50 de assertividade sempre",
    "Bloqueado": "Não recebe efeitos positivos",
    "Envenenado": "10 de dano por turno",
    "Tóxico": "20 de dano por turno",
    "Fragilizado": "Menos 50% de Sp defesa ",
    "Quebrado": "Menos 50% de defesa",
    "Congelado": "Não pode ser selecionado",
    "Queimado": "Corta cura de 30% e toma 15 de dano por turno",
    "Paralisado": "Velocidade zerada",
    "Encharcado": "Mais 2 energias para se mover",
    "Vampirico": "Inimigos se curam em 30% do dano causado",
    "Descarregado": "Ataca com o dobro de energias",
    "Enfraquecido": "Menos 30% de ataques",
    "Incapacitado": "Não pode atacar"
}

class Pokemon:
    def __init__(self, pokemon, player):

        self.nome = pokemon["nome"]
        self.tipo = pokemon["tipo"]
        self.raridade = pokemon["raridade"]
        self.Estagio = pokemon["estagio"]
        self.Altura = pokemon["altura"]
        self.Peso = pokemon["peso"]

        self.barreira = 0
        self.amplificações = 0

        self.Vida = pokemon["vida"]
        self.Atk = 0
        self.Atk_sp = 0
        self.Def = 0
        self.Def_sp = 0
        self.vel = 0 

        self.VidaMaxB = pokemon["vida"]
        self.VidaMax = 1
        self.VarVida = 0

        self.AtkB = pokemon["atk"]
        self.Atk_spB = pokemon["atk SP"]
        self.DefB = pokemon["def"]
        self.Def_spB = pokemon["def SP"] 
        self.velB = pokemon["velocidade"]

        self.VarAtk_temp = 0
        self.VarAtk_sp_temp = 0
        self.VarDef_temp = 0
        self.VarDef_sp_temp = 0
        self.Varvel_temp = 0

        self.VarAtk_perm = 0
        self.VarAtk_sp_perm = 0
        self.VarDef_perm = 0
        self.VarDef_sp_perm = 0
        self.Varvel_perm = 0

        self.custo = pokemon["custo"]
        self.evolucao = pokemon["evolução"]
        self.FF = pokemon["FF"]
        self.xp_atu = pokemon["XP atu"]
        self.xp_total = pokemon["XP"]

        self.IV = pokemon["IV"]
        self.IV_vida = pokemon["IV vida"]
        self.IV_atk = pokemon["IV atk"]
        self.IV_atkSP = pokemon["IV atk SP"]
        self.IV_def = pokemon["IV def"]
        self.IV_defSP = pokemon["IV def SP"]
        self.IV_vel = pokemon["IV vel"]

        self.movimento1 = pokemon["Move1"]
        self.movimento1["num"] = 1
        self.movimento2 = pokemon["Move2"]
        self.movimento1["num"] = 2
        self.movimento3 = pokemon["Move3"]
        self.movimento1["num"] = 3
        self.movimento4 = pokemon["Move4"]
        self.movimento1["num"] = 4
        self.moveList = pokemon["MoveList"]
        self.movePossiveis = pokemon["possiveis"]

        self.PodeMovimento1 = 0
        self.PodeMovimento2 = 0
        self.PodeMovimento3 = 0
        self.PodeMovimento4 = 0

        self.code = pokemon["code"]
        self.ID = pokemon["ID"] #unico

        self.guardado = 0
        self.local = None
        self.icone = Carrega_Icone_pokemon(self.nome)
        self.efeitosPosi = EfeitosPositivos.copy()
        self.efeitosNega = EfeitosNegativos.copy()
        self.descrição = EfeitosDescrição
        
        try:
            player.pokemons.append(self)
            self.pos = player.pokemons.index(self)
        except AttributeError:
            self.pos = None
        
        self.atacou = False
        self.PodeEvoluir = True
        self.PodeAtacar = True
        self.PodeSerAtacado = True

    def FormaFinal(self,item,player):
        if self.xp_atu >= self.xp_total:
            pos = self.pos
            if self.FF is not None:
                for i in range(len(self.FF)):
                    if item["nome"] == "Energia Mega":
                        if self.FF[i]["FF"] == "Mega":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(i,player))

                    elif item["nome"] == "Energia Vstar":
                        if self.FF[i]["FF"] == "Vstar":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(1,player))

                    elif item["nome"] == "Energia GigantaMax":
                        if self.FF[i]["FF"] == "Vmax":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(0,player))
            else:
                GV.adicionar_mensagem("Esse pokemon não tem forma final")
                return
            
            GV.adicionar_mensagem("Energia não condiz com a forma final")
            return

        else:
            GV.adicionar_mensagem("Xp insuficiente")
            return
        
    def Evoluir_Final(self,i,player):
        nome_antigo = self.nome
        self.nome = self.FF[i]["nome"]
        self.VidaMaxB = round(self.VidaMaxB * self.FF[i]["vida"])
        self.Vida = round(self.Vida * self.FF[i]["vida"])
        self.DefB = round(self.DefB * self.FF[i]["def"])
        self.Def_spB = round(self.Def_spB * self.FF[i]["def SP"])
        self.AtkB = round(self.AtkB * self.FF[i]["atk"])
        self.Atk_spB = round(self.Atk_spB * self.FF[i]["atk SP"])
        self.velB = round(self.velB * self.FF[i]["velocidade"])
        self.custo = self.FF[i]["custo"]
        self.Estagio = self.FF[i]["estagio"]
        self.xp_total = self.FF[i]["XP"]
        self.evolucao = self.FF[i]["evolução"]
        VerificaGIF(player)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Insano!")

    def evoluir(self,player):
        if self.xp_atu >= self.xp_total:
            if self.PodeEvoluir is True:
                if isinstance(self.evolucao,list):
                    self.evolucao = random.choice(self.evolucao)
                if self.evolucao is not None:
                    i = self.pos
                    self.PodeEvoluir = False
                    adicionar_efeito("Evoluindo", (520 + i * 190, 980), ao_terminar=lambda: self.Evoluir_de_fato(player))
                    return
            else:
                tocar("Bloq")
                GV.adicionar_mensagem("Evoluindo...")
                return
        tocar("Bloq")
        GV.adicionar_mensagem("Seu pokemon não pode evoluir")

    def Evoluir_de_fato(self,player):
        nome_antigo = self.nome

        if self.evolucao["moves"] >= 3 and self.movimento3 is None:
            while True:
                sorteado = random.choice(self.evolucao["movelist"])
                ataque = SelecionaAtaques(sorteado)
                if sorteado not in self.moveList:
                    self.moveList.append(sorteado)
                    self.movimento3 = ataque
                    break
        if self.evolucao["moves"] == 4 and self.movimento4 is None:
            while True:
                sorteado = random.choice(self.evolucao["movelist"])
                ataque = SelecionaAtaques(sorteado)
                if sorteado not in self.moveList:
                    self.moveList.append(sorteado)
                    self.movimento4 = ataque
                    break
        
        self.movePossiveis = self.evolucao["movelist"]
        self.nome = self.evolucao["nome"]
        self.VidaMaxB = round(self.VidaMaxB * self.evolucao["vida"])
        self.Vida = round(self.Vida * self.evolucao["vida"])
        self.DefB = round(self.DefB * self.evolucao["def"])
        self.Def_spB = round(self.Def_spB * self.evolucao["def SP"])
        self.AtkB = round(self.AtkB * self.evolucao["atk"])
        self.Atk_spB = round(self.Atk_spB * self.evolucao["atk SP"])
        self.velB = round(self.velB * self.evolucao["velocidade"])
        self.custo = self.evolucao["custo"]
        self.Estagio = self.evolucao["estagio"]
        self.FF = self.evolucao["FF"]
        self.xp_total = self.evolucao["XP"]
        self.evolucao = self.evolucao["evolução"]
        self.icone = Carrega_Icone_pokemon(self.nome)
        VerificaGIF(player)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")


    def Ganhar_XP(self,quantidade,player):
        self.xp_atu = self.xp_atu + quantidade
    
    def amplificar(self,tipo,tela,player):
        if tipo == "atk":
            J = round(self.Atk)
            self.VarAtk_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ataque, foi de {J} para {J + 2}")
        elif tipo == "atk SP":
            J = round(self.Atk_sp)
            self.VarAtk_sp_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ataque especial, foi de {J} para {J + 2}")
        elif tipo == "def":
            J = round(self.Def)
            self.VarDef_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou sua defesa, foi de {J} para {J + 2}")
        elif tipo == "def SP":
            J = round(self.Def_sp)
            self.VarDef_sp_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou sua defesa especial, foi de {J} para {J + 2}")
        elif tipo == "vel":
            J = round(self.vel)
            self.Varvel_perm += 3
            GV.adicionar_mensagem(f"{self.nome} amplificou sua velocidade, foi de {J} para {J + 3}")
        elif tipo == "Vida":
            J = round(self.VidaMax)
            self.VarVida += 6
            self.Vida += 6
            GV.adicionar_mensagem(f"{self.nome} amplificou sua vida máxima, foi de {J} para {J + 6}")
        
        self.amplificações += 1
        
    
    def atacado(self,dano,player,inimigo,tela,Mapa):
        DanoOriginal = dano

        if self.barreira > 0:
            if self.barreira <= dano:
                dano = self.barreira
            self.barreira = self.barreira - dano
            self.barreira = round(self.barreira,1)

        else:
            if self.Vida <= dano:
                if self.efeitosPosi["Imortal"]:
                    dano = self.Vida - 0.1
                    self.efeitosPosi["Imortal"] = 0
                else:
                    dano = self.Vida
            
            self.Vida = self.Vida - dano
            self.Vida = round(self.Vida,1)
        
        i = self.pos
        if self in inimigo.pokemons:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((1410 - i * 190),180))
        else:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((425 + i * 190),975))

        if self.Vida == 0:
            GuardarPosicionar(self,player,0,Mapa.Zona)
            GV.adicionar_mensagem(f"{self.nome} foi nocauteado")

    def curar(self,cura,player,tela):
            if self.efeitosPosi["Abençoado"] != 0:
                cura = cura * 1.3
            if self.efeitosNega["Queimado"] != 0:
                cura = cura * 0.7

            dano_tomado = self.VidaMax - self.Vida
            self.Vida = round(self.Vida + cura,1)
            if self.Vida > self.VidaMax:
                self.Vida = self.VidaMax
                cura = dano_tomado 
            
            i = self.pos
            if self in player.pokemons:
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((510 + i * 190),1010))
            else:
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((1410 - i * 190),180))

IDpoke = 0

def Gerador(Pokemon,P):
    global IDpoke
    IDpoke += 1
    Pok = Pokemon

    vida_min = int(Pok["vida"] * 0.8)
    vida_max = int(Pok["vida"] * 1.2)
    vida_max_real = int(vida_max * P)
    vida = random.randint(vida_min, vida_max_real)
    vida = min(vida, int(Pok["vida"] * 1.2))

    atk_min = int(Pok["atk"] * 0.8)
    atk_max = int(Pok["atk"] * 1.2)
    atk_max_real = int(atk_max * P)
    Atk = random.randint(atk_min, atk_max_real)
    Atk = min(Atk, int(Pok["atk"] * 1.2))

    atkSP_min = int(Pok["atk SP"] * 0.8)
    atkSP_max = int(Pok["atk SP"] * 1.2)
    atkSP_max_real = int(atkSP_max * P)
    Atk_SP = random.randint(atkSP_min, atkSP_max_real)
    Atk_SP = min(Atk_SP, int(Pok["atk SP"] * 1.2))

    def_min = int(Pok["def"] * 0.8)
    def_max = int(Pok["def"] * 1.2)
    def_max_real = int(def_max * P)
    Def = random.randint(def_min, def_max_real)
    Def = min(Def, int(Pok["def"] * 1.2))

    defSP_min = int(Pok["def SP"] * 0.8)
    defSP_max = int(Pok["def SP"] * 1.2)
    defSP_max_real = int(defSP_max * P)
    Def_SP = random.randint(defSP_min, defSP_max_real)
    Def_SP = min(Def_SP, int(Pok["def SP"] * 1.2))

    vel_min = int(Pok["velocidade"] * 0.8)
    vel_max = int(Pok["velocidade"] * 1.2)
    vel_max_real = int(vel_max * P)
    vel = random.randint(vel_min, vel_max_real)
    vel = min(vel, int(Pok["velocidade"] * 1.2))

    IVV = ((vida - vida_min) / (vida_max - vida_min)) * 100
    IVA = ((Atk - atk_min) / (atk_max - atk_min)) * 100
    IVAS = ((Atk_SP - atkSP_min) / (atkSP_max - atkSP_min)) * 100
    IVD = ((Def - def_min) / (def_max - def_min)) * 100
    IVDS = ((Def_SP - defSP_min) / (defSP_max - defSP_min)) * 100
    IVVE = ((vel - vel_min) / (vel_max - vel_min)) * 100

    IV = round((IVV + IVA + IVAS + IVD + IVDS + IVVE) / 6, 2)

    Coef_Genetico = random.uniform(0.75,1.15)

    Altura = Pok["H"] * (Coef_Genetico + (IVV/200) + (IVA/300) + (IVAS/300))
    Peso = Pok["W"] * (Coef_Genetico + (IVV/200) + (IVD/200) + (IVDS/200) - (IVVE/250))

    if Altura > 9.9:
        Altura = round(Altura,1)
    else:
        Altura = round(Altura,2)

    if Peso > 99.5:
        Peso = round(Peso,0)
    else:
        Peso = round(Peso,1)

    Stats = {
        "nome": Pok["nome"],
        "tipo": Pok["tipo"],
        "raridade": Pok["raridade"],
        "vida": vida,
        "estagio": 1,
        "altura": Altura,
        "peso": Peso,
        "atk": Atk,
        "atk SP": Atk_SP,
        "def": Def,
        "def SP": Def_SP,
        "velocidade": vel,
        "XP": Pok["XP"],
        "custo": Pok["custo"],
        "evolução": Pok["evolução"],
        "FF": Pok["FF"],
        "XP atu": 0,
        "IV": round(IV,1),
        "IV vida": round(IVV),
        "IV atk": round(IVA),
        "IV atk SP": round(IVAS),
        "IV def": round(IVD),
        "IV def SP": round(IVDS),
        "IV vel": round(IVVE),
        "code": Pok["code"],
        "ID": IDpoke,
        "MoveList": [],
        "possiveis": Pok["MoveList"],
        "Move1": None,
        "Move2": None,
        "Move3": None,
        "Move4": None
    }

    for i in range(Pok["Moves"]):
        while True:
            sorteado = random.choice(Pok["MoveList"])
            ataque = SelecionaAtaques(sorteado)
            if sorteado not in Stats["MoveList"]:
                Stats["MoveList"].append(sorteado)
                Stats[f"Move{i+1}"] = ataque
                break

    return Stats

def Gerador_final(code,P,player):
    return Pokemon(Gerador(Pokemons_Todos[code],P),player)

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "preta"]

def VerificaSituaçãoPokemon(player, inimigo):
    for pokemon in player.pokemons:
        if pokemon.atacou == True or pokemon.efeitosNega["Incapacitado"] > 0 or pokemon.efeitosNega["Congelado"] > 0 or pokemon.local is None:
            pokemon.PodeAtacar = False
        else:
            pokemon.PodeAtacar = True
        if pokemon.PodeEvoluir is True:
            if pokemon.local is None:
                pokemon.PodeEvoluir = False

    for pokemon in player.pokemons + inimigo.pokemons:
        # --- Resetar apenas os modificadores TEMPORÁRIOS ---
        pokemon.VarAtk_temp = 0
        pokemon.VarAtk_sp_temp = 0
        pokemon.VarDef_temp = 0
        pokemon.VarDef_sp_temp = 0
        pokemon.Varvel_temp = 0

        # --- Aplicar efeitos negativos/positivos TEMPORÁRIOS ---
        if pokemon.efeitosNega["Quebrado"] > 0:
            pokemon.VarDef_temp += -pokemon.DefB * 0.5
        if pokemon.efeitosNega["Fragilizado"] > 0:
            pokemon.VarDef_sp_temp += -pokemon.Def_spB * 0.5
        if pokemon.efeitosPosi["Reforçado"] > 0:
            pokemon.VarDef_temp += pokemon.DefB * 0.3
            pokemon.VarDef_sp_temp += pokemon.Def_spB * 0.3
        if pokemon.efeitosNega["Enfraquecido"] > 0:
            pokemon.VarAtk_temp += -pokemon.AtkB * 0.3
            pokemon.VarAtk_sp_temp += -pokemon.Atk_spB * 0.3
        if pokemon.efeitosPosi["Ofensivo"] > 0:
            pokemon.VarAtk_temp += pokemon.AtkB * 0.3
            pokemon.VarAtk_sp_temp += pokemon.Atk_spB * 0.3
        if pokemon.efeitosPosi["Velocista"] > 0:
            pokemon.Varvel_temp += pokemon.velB * 1.5
        if pokemon.efeitosNega["Paralisado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB
        if pokemon.efeitosNega["Congelado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB

        # --- Atualizar status finais (Base + Permanente + Temporário) ---
        pokemon.VidaMax = pokemon.VidaMaxB + pokemon.VarVida
        pokemon.Atk = round(pokemon.AtkB + pokemon.VarAtk_perm + pokemon.VarAtk_temp)
        pokemon.Atk_sp = round(pokemon.Atk_spB + pokemon.VarAtk_sp_perm + pokemon.VarAtk_sp_temp)
        pokemon.Def = round(pokemon.DefB + pokemon.VarDef_perm + pokemon.VarDef_temp)
        pokemon.Def_sp = round(pokemon.Def_spB + pokemon.VarDef_sp_perm + pokemon.VarDef_sp_temp)
        pokemon.vel = round(pokemon.velB + pokemon.Varvel_perm + pokemon.Varvel_temp)


        if sum(player.energias[energia] for energia in Energias) > 0:
            if player.energiasDesc == []:
                while True:
                    energiaSort = random.choice(Energias)
                    if energiaSort not in player.energiasDesc and player.energias[energiaSort] != 0:
                        player.energiasDesc.append(energiaSort)
                        break

            while True:
                SomaDesc = sum(player.energias[energia] for energia in player.energiasDesc)

                if SomaDesc >= 1:
                    break

                energiaSort = random.choice(Energias)
                if energiaSort not in player.energiasDesc and player.energias[energiaSort] != 0:
                    player.energiasDesc.append(energiaSort)



# === Fim de GeradorPokemon.py ===

