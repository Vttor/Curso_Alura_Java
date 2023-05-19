class Programa:
    def __init__(self, nome: str, ano: int) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return (f'Serie: {self.nome} - Ano: {self.ano}'
        f' - {self.likes} Likes')

    @property
    def likes(self):
        return self._likes


    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome: str, ano: int, duracao: int) -> None:
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return (f'Serie: {self.nome} - Ano: {self.ano}'
        f' - {self.duracao} min - {self.likes} Likes')

class Serie(Programa):
    def __init__(self, nome: str, ano: int, temporadas: int) -> None:
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f'Serie: {self.nome} - Ano: {self.ano}'
        f' - {self.temporadas} temporadas - {self.likes} Likes')

class Playlist():
    def __init__(self, nome: str, programas: list) -> None:
        self.nome = nome
        self._programas = programas
        
    @property
    def listagem(self):
        return self._programas
    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
atlanta = Serie("Atlanta",2010,6)
demolidor = Filme("Demolidor", 2008, 120)
office = Serie("The Office", 2004, 9)


vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

office.dar_like()
office.dar_like()
office.dar_like()
office.dar_like()
office.dar_like()
office.dar_like()




playlist_filmes_e_series = [vingadores, atlanta,demolidor,office]
playlist = Playlist("Fim de Semana", playlist_filmes_e_series)

print(f'Tamanho do playlist: {len(playlist.listagem)}')

for programa in playlist.listagem:
    print(programa)

print(f'Tá ou não tá? {demolidor in playlist.listagem}')
