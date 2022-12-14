
class Programa:

    def __init__ (self, nome, ano):
        self._nome = nome.title ()
        self.ano = ano
        self._likes = 0

    @property
    def likes (self):
        return self._likes

    def dar_likes (self):
        self._likes += 1

    @property
    def nome (self):
        return self._nome
    
    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title ()
    
class Filme (Programa):

    def __init__ (self, nome, ano, duracao):
        super ().__init__ (nome, ano)
        self.duracao = duracao

    def __str__ (self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes"

class Serie (Programa):

    def __init__ (self, nome, ano, temporadas):
        super ().__init__ (nome, ano)
        self.temporadas = temporadas

    def __str__ (self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes"

class Playlist:

    def __init__ (self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__ (self, item):
        return self._programas [item]
    @property
    def listagem (self):
        return self._programas

    @property
    def tamanho (self):
        return len (self._programas)

vingadores = Filme ("vingadores", 2018, 160)
atlanta = Serie ("atlanta", 2018, 2)
avatar = Filme ("Avatar", 2012, 120)
himym = Serie ("How I Met Your Mother", 2010, 9)

vingadores.dar_likes ()
avatar.dar_likes ()
avatar.dar_likes ()
vingadores.dar_likes ()
himym.dar_likes ()
atlanta.dar_likes ()

filmes_e_series = [vingadores, atlanta, avatar, himym]
playlist_fim_de_semana = Playlist ("Fim de semana", filmes_e_series)

for programa in playlist_fim_de_semana.listagem:
    print (programa)
