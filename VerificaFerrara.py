class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self):
    return f'Codice: {self.codice}\nFornitore: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantità: {self.quantita}\n'
    

  def modifica_scheda(self):
    scelta = int(input("Cosa vuoi modificare? 1-Fornitore 2-Marca 3-Prezzo 4-Quantità\n"))
    match scelta:
      case 1:
        self.fornitore = str(input("Inserire il nuovo fornitore."))
      case 2:
        self.marca = str(input("Inserire una nuova marca."))
      case 3:
        self.prezzo = int(input("Inserire il nuovo prezzo."))
      case 4:
        self.quantita = int(input("Inserire la nuova quantità."))
      case _:
        print("Il valore non è valido.")

class Televisore(Articolo):
  def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
    super().__init__(codice, fornitore, marca,prezzo, quantita)
    self.pollici = pollici
    self.tipo = tipo

  def scheda_articolo(self):
    return super().scheda_articolo() + f"Pollici: {self.pollici}\nTipo: {self.tipo}"
  
class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    super().__init__(codice, fornitore, marca, prezzo, quantita)
    self.dimensiioni = dimensioni
    self.modello = modello

  def scheda_articolo(self):
    return super().scheda_articolo() + f"Dimensioni: {self.dimensioni}\nModello {self.modello}"

t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
t1.modifica_scheda()
print(t1.scheda_articolo())
#09:51 Invernizzi

class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo
    self.articoli = []

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
    self.articoli.append(articolo)
    print(f"{tipo_articolo} aggiunto all'ordine {self.codice}")


  def rimuovi_articolo(self,articolo):
    if articolo in self.articoli:
      if isinstance(articolo,Televisore):
        tipo_articolo = "televisore"
      elif isinstance(articolo, Frigorifero):
        tipo_articolo = "frigorifero"
      print(f"{tipo_articolo} con codice {self.codice} rimosso")
      self.articoli.remove(articolo)
      print(f"{tipo_articolo} con codice {self.codice} non presente nell'ordine")

  def importo_ordine(self):
    importoTotale = 0
    for articolo in self.articoli:
      importoTotale += articolo.prezzo
    print(f"Importo ordine con codice {self.codice} contenente {len(self.articoli)} articolo/i = {importoTotale}")

  def dettaglio_ordine(self):
    sommaT = 0
    sommaF = 0
    for articolo in self.articoli:
      if isinstance(articolo,Televisore):
        sommaT += articolo.prezzo * articolo.quantita
      elif isinstance(articolo,Frigorifero):
        sommaF += articolo.prezzo * articolo.quantita
    
    return([sommaT,sommaF,sommaT+sommaF])

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)

ordine1.importo_ordine()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
#10:20 Invernizzi

class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.ordini = []

  def aggiungi_ordine(self,ordine):
    self.ordini.append(ordine)

  def rimuovi_ordine(self,ordine):
    if ordine in self.ordini:
      self.ordini.remove(ordine)
  
  def totale_ordini(self):
    totT = 0
    totF = 0
    tot = 0
    for ordine in self.ordini:
      dattaglioOrdine = ordine.dettaglio_ordine()
      totT += dattaglioOrdine[0]
      totF += dattaglioOrdine[1]
      tot += dattaglioOrdine[2]
    
    return ([totT,totF,tot])

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)
ordini_negozio.aggiungi_ordine(ordine2)
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")
#11:20 Spinarelli