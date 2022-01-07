# PageRank & HITS

### PageRank

PageRank è un algoritmo iterativo ideato da Larry Page and Sergey Brin nel 1996 e presentato due anni dopo, nel 1998.<br>
L'algoritmo è utilizzato per descrivere - attraverso un _rank_ - la popolarità della diverse _page_ nel web.<br>
È utilizzato da Google nel suo motore di ricerca.

Esso parte dall'ipotesi che una pagina web è tanto più autorevole quanti più link in ingresso - _inlink_ - essa ha.<br>
Si noti che tale algoritmo è del tutto agnostico rispetto al contenuto delle pagine web: un utente malevolo quindi potrebbe realizzare una _link farm_ verso il proprio sito web per aumentarne il ranking.

Si considera un **_random surfer_** che naviga senza sosta nel web.<br>
Ogni volta che esso visita una pagina può effettuare una delle seguenti azioni:
- scegliere un link a caso tra quelli presenti nella pagina e spostarsi alla pagina puntata
- spostarsi su una pagina random (scelta definita come _surprise me_) 

L'algoritmo considera anche un parametro di tuning: il valore _λ_ (definito _soglia di probabilità_) compreso tra 0 e 1.

A ogni iterazione:

1. Si sceglie un valore random _x_ tra 0 e 1
2. Se _x_<_λ_ allora si sceglie l'opzione _surprise me_, altrimenti si sceglie un link a caso di quelli presenti nella pagina
3. Si torna al punto 1

In genere il valore _λ_ è scelto molto basso per favorire la scelta di un link all'interno della pagina: in effetti questo è il comportamento tipico umano quando si naviga su internet. Ciò porta a visitare le pagine _più popolari_.<br>
Allo stesso modo è utile che esso non sia troppo basso: se così non fosse rischiereri di incappare in cicli o in pagine che non contengono link uscenti.

Considerando una pagina _u_ e un insieme di pagine _B_ (pagine che contengono link verso _u_) il PageRank di _u_ è dato da 

<div align="center">  
<img src="https://latex.codecogs.com/svg.image?PR(u)=\frac{\lambda}{N}&plus;(1-\lambda)\cdot\sum_{v&space;\in&space;&space;B}{\frac{PR(v)}{L_{v}}}" title="PR(u)=\frac{\lambda}{N}+(1-\lambda)\cdot\sum_{v \in B}{\frac{PR(v)}{L_{v}}}" />
</div>

_N_ è il numero totale di pagine web e _L_ è il numero totale di link uscenti dalla pagina.


---

#### Applicazione dell'algoritmo PageRank al sito web [_mariocuomo.github.io_](https://mariocuomo.github.io/)
Ho applicato l'algoritmo PageRank al mio sito web per cercare di capire quale fossero le pagine web più popolari.<br>
Ho utilizzato il software [_Gephi_](https://gephi.org/).

Per prima cosa ho realizzato un grafo che rispecchia la topologia del sito.<br>
Il grafo associato è costituito da
- nodi: sono le pagine web (un nodo per ogni pagina distinta)
- archi: si ha un arco orientato dal nodo _x_ al nodo _y_ se è presente un link nella pagina rappresentata dal nodo _x_ verso la pagina rappresentata dal nodo _y_.<br>Gli archi sono distinti: se si hanno due link da _x_ a _y_, si hanno due archi da  _x_ a _y_.


<div align="center">  
  <img src="https://github.com/mariocuomo/pageRankOfMySite/blob/main/website.png" width=800>
</div>


Questa è la topologia a grafo del sito web realizzato con Gephi.<br>
NOTA: ho considerato solamente link che puntano a pagine del mio sito; riferimenti a pagine esterne sono stati esclusi.

<div align="center">  
  <img src="https://github.com/mariocuomo/pageRankOfMySite/blob/main/topology.png" width=600>
</div>

Ho infine applicato PageRank con il software Gephi.<br>
I parametri di tuning sono _λ=0.15_ e _ε=0.001_.<br>
Il parametro _ε_ serve per terminare la computazione dell'algoritmo: a ogni iterazione sono aggiornati i valori di PageRank. Ci si ferma nel momento in cui l'aggiornamento - tra una iterazione e la successiva - è minore di _ε_.

<div align="center">  
  <img src="https://github.com/mariocuomo/pageRankOfMySite/blob/main/stats.png" width=600>
</div>

<div align="center">  
  <img src="https://github.com/mariocuomo/pageRankOfMySite/blob/main/pageranks.png">
</div>


Si nota come la pagina [_whoIAm_](https://mariocuomo.github.io/view/whoiam.html) risulta essere quella più autorevole - anche se non di troppo - rispetto le altre.

---


### Hyperlink-Induced Topic Search

L'algoritmo HITS è stato sviluppato in contemporanea all'algoritmo PageRank.<br>
Così come PageRank anche HITS è agnostico rispetto al contenuto delle entità coinvolte - in questo caso pagine web - considerando solamente la topologia della rete.<br>
Una delle differenze è l'applicazione: PageRank è utilizzato per identificare le pagine più autorevoli assegnandogli uno score. Lo score è un tag che può essere utile al motore di ricerca durante l'indicizzazione o il recupero delle informazioni a seguito di una query. HITS è utilizzato per estendere la search o migliorare il browsing trovando entità esperte candidate: è un algoritmo utilizzato per trovare _community_ all'interno del web.

Una comunità è un gruppo di entità che interagiscono in un ambiente sociale condividendo obiettivi, caratteristiche e interessi: quando si parla di _web community_ si considerano entità che sono pagine web e che trattano argomenti comuni.
Le caratteristiche fondamentali di una community sono che essa è composta da entità simili - secondo una misura di similarità - e che l'interazione tra i membri di essa è molta rispetto a quella verso l'esterno.

Se si rappresentano le entità come nodi si ha che 
- nodi: sono le entità (le pagine web)
- archi: sono le interazioni e possono essere _diretti_, nel caso in cui si ha una relazione non simmetrica - o _indiretti_


Per ogni entità sono calcolati i valori di _**authority score**_ e di _**hub score**_. Il primo stima il valore del contenuto di una pagina, il secondo stima il valore complessivo delle pagine da essa puntata.

Anche in questo caso si parte da una supposizione molto semplice: buoni hub puntano a buone authority così come buone authority puntano a buoni hub.

A ogni iterazione si aggiornano i valori di Authority e di Hub come segue
<div align="center">  
  <img src="https://latex.codecogs.com/svg.image?A(p)=\sum_{q&space;\rightarrow&space;p}{H(q)}&space;" title="A(p)=\sum_{q \rightarrow p}{H(q)} " />
</div>
<div align="center">  
  <img src="https://latex.codecogs.com/svg.image?H(p)=\sum_{p&space;\rightarrow&space;q}{A(q)}&space;" title="H(p)=\sum_{p \rightarrow q}{A(q)} " />
</div>

L'authority di una pagina è la somma di tutti gli _hub score_ delle pagine che puntano a essa.<br>
L'hub score di una pagina è la somma di tutti gli _authority score_ delle pagine che essa punta.

Si inizia l'algoritmo con _A(p)_=_H(p)_=1.<br>
Al termine di ogni iterazione si normalizzano gli score nell'intervallo [0,1].

Le entità che presentano i valori più alti sono considerati i _**leader**_ della comunità.

#### Applicazione di HITS al sito web [_mariocuomo.github.io_](https://mariocuomo.github.io/)
Ho applicato l'algoritmo HITS al mio sito web per cercare di capire quale fossero le pagine _core_.<br>
Ho utilizzato il software [_Gephi_](https://gephi.org/).

Il grafo realizzato è lo stesso utilizzato nell'applicazione di PageRank.<br>
Anche per HITS si può decidere di impostare un valore di convergenza _ε_.
Questi sono i risultati proposti da HITS.

<div align="center">  
  <img src="https://github.com/mariocuomo/pageRankOfMySite/blob/main/hits.png">
</div>

La pagina che ha il minor valore di _hub_ è la pagina iniziale; allo stesso tempo ha il valore di Authority più alto.<br>
In effetti _index.html_ ha un solo link in uscita verso _whoIAm.html_.<br>
L'alta _authority_ deriva dal fatto che ogni pagina del sito web contiene un riferimento ad essa.
