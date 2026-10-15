import csv
oggetti_stand=[]
oggetti_espositori=[]


class Espositori:
    "Classe esporitori"
    def __init__(self, codice,nome , cognome):

        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.codice_stand = None

    def preno_stand(self, codice_stand):
        self.codice_stand = codice_stand
    def __str__(self):
        return f"stand assgnato: {self.codice_stand} nome: {self.nome} cognome: {self.cognome}"




class Stand:
    """Classe stand"""
    def __init__(self, codice, Area, num_Padiglione, prezzo):
        self.codice = codice
        self.Area = Area
        self.num_Padiglione = num_Padiglione
        self.prezzo = prezzo
        self.codice_espo = None

    def preno_espo(self,codice_espo):
        self.codice_espo=codice_espo
    def __str__(self):
        return f" codice del stand :{self.codice} prenotado da {self.codice_espo} "



class Stand_prese_extra(Stand):
    "Classe stand_prese_extra"
    def __init__(self, codice, Area, num_Padiglione, prezzo, num_prese):
        super().__init__(codice, Area, num_Padiglione, prezzo)
        self.num_prese = num_prese

class Stand_premium(Stand):
    "Classe stand_premium"
    def __init__(self, codice, Area, num_Padiglione, prezzo, tipo):
        super().__init__(codice, Area , num_Padiglione, prezzo )
        self.tipo = tipo




class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        file = csv.reader(open(file_path, "r"))
        for line in file:
            if line[0].startswith("ES"):
                oggetti_espositori.append(Espositori(line[0], line[1], line[2]))

            if line[0].startswith("ST"):
                if len(line)==4:
                    oggetti_stand.append(Stand(line[0], line[1], line[2], line[3]))


                elif len(line)==5 and line[4].isalnum():
                    oggetti_stand.append(Stand_prese_extra(line[0], line[1], line[2], line[3] , line[4]))

                elif len(line)==5 and line[4].isalpha():
                    oggetti_stand.append(Stand_premium(line[0], line[1], line[2], line[3], line[4]))







    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        oggetto=0
        for e in oggetti_espositori:
            if codice_espositore==e.codice:
                espo=e

        for s in oggetti_stand:
            if codice_stand==s.codice:
                stand=s

        if espo.codice_stand==None and stand.codice_espo==None:

            stand.preno_espo(espo.codice)
            espo.preno_stand(stand.codice)

        elif espo.codice_stand!=None:
            raise Exception("L'espositore è già stato assegnato in un stand")

        elif stand.codice_stand!=None:
            raise  Exception("Lo stand è gia occupato da un espositore")

        print(espo)
        print(stand)

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
