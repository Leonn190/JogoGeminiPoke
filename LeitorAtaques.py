def Atacar(PokemonS,PokemonV,PokemonA,player,inimigo,Mapa,tela):
    if AtaqueS is not None:
            alvos = None
            AlvoLoc2 = None
            if AtaqueS["extra"] == "V":
                if PokemonV is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo visualizado")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc = ((510 + idx * 190),1010)

            elif AtaqueS["extra"] == "A":
                if PokemonA is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)

            elif AtaqueS["extra"] == "AV":
                if PokemonA is None or PokemonV is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo e um alvo visualizado")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)
                    
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc2 = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc2 = ((510 + idx * 190),1010)
            elif AtaqueS["extra"] == "MA":
                alvos = AtaqueS["alvos"](PokemonS,PokemonA,player,inimigo,Mapa)
            elif AtaqueS["extra"] == "MAA":
                alvos = AtaqueS["alvos"](PokemonS,PokemonA,player,inimigo,Mapa)
                if PokemonA is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)

            else:
                if PokemonV is not None and AtaqueS["extra"] == "TV":
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc2 = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc2 = ((510 + idx * 190),1010)
                idx = PokemonS.pos
                AlvoLoc = ((510 + idx * 190),1010)
            
            if VCusto(player,PokemonS,AtaqueS) == False:
                return
            
            PokemonS.atacou = True
            PokemonS.Ganhar_XP(4,player)

            if AtaqueS["extra"] == "A" or AtaqueS["extra"] == "AV":
                if VAcerta(PokemonS,PokemonA,AtaqueS,Mapa.Metros) == False:
                    return
            
            adicionar_efeito(AtaqueS["efeito"],AlvoLoc,lambda: AtaqueS["funçao"](PokemonS,PokemonV,PokemonA,alvos,player,inimigo,AtaqueS,Mapa,tela,AlvoLoc,EstadoDaPergunta,AtaqueS["irregularidade"]))
            if alvos is not None:
                for alvo in alvos:
                    idx = alvo.pos
                    if alvo in inimigo.pokemons:
                        AlvoLoc = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc = ((520 + idx * 190),1000)
                    adicionar_efeito(AtaqueS["efeito"],AlvoLoc)

            if AlvoLoc2 is not None:
                adicionar_efeito(AtaqueS["efeito2"],AlvoLoc2)

    else: 
        GV.adicionar_mensagem("Selecione um ataque")
        tocar("Bloq")
        return