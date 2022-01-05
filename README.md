# PageRank

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
2. Se _x_<_λ_ allora si sceglie l'opzione _surprise me_, altrimenti si sceglie un link a caso di quelli dpresenti nella pagina
3. Si torma al punto 1

In genere il valore _λ_ è scelto molto basso per favorire la scelta di un link all'interno della pagina: in effetti questo è il comportamento tipico umano quando si naviga su internet. Ciò porta a visitare le pagine _più popolari_.<br>
Allo stesso modo è utile che esso non sia troppo basso: se così non fosse rischiereri incappare in cicli o in pagine che non contengono più link uscenti.

Considerando una pagina _u_ e un insieme di pagine _B_ (pagine che contengono link verso _u_) il PageRank di _u_ è dato da 

<div align="center">  
<img src="https://latex.codecogs.com/svg.image?PR(u)=\frac{\lambda}{N}&plus;(1-\lambda)\cdot\sum_{\cdot&space;v&space;\in&space;&space;B}{\frac{PR(v)}{L_{v}}}" title="PR(u)=\frac{\lambda}{N}+(1-\lambda)\cdot\sum_{\cdot v \in B}{\frac{PR(v)}{L_{v}}}" />
</div>

_N_ è il numero totale di pagine web e _L_ è il numero totale di link uscenti dalla pagina.


---

#### Applicazione dell'algoritmo PageRank al sito web [_mariocuomo.github.io_](https://mariocuomo.github.io/)
Ho applicato l'algoritmo PageRank al mio sito web per cercare di capire quale fossero le pagine web più popolori.<br>
Ho utilizzato il software [_Gephi_](https://gephi.org/)

Per prima cosa ho realizzato un grafo che rispecchiasse la topologia del sito.<br>
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

---

Si nota come la pagina [_whoIAm_](https://mariocuomo.github.io/view/whoiam.html) risulta essere quella più autorevole - anche se non di troppo - rispetto le altre.
