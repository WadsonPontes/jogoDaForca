# Author: Wadson Pontes
# Date: 15/06/2019
# Version: 1.0
import random as rd

# 1000 palavras com menos de 6 letras
palavras_n1 = ["favor", "este", "agora", "todos", "todas", "sido", "mais", "usual", "obra", "mera", "nossa", "muito", "saber", "cuja", "fins", "pelos", "pela", "ainda", "clara", "sabem", "sendo", "cada", "andou", "menos", "maior", "parte", "febre", "nome", "desde", "senti", "falta", "pelo", "povo", "rural", "fauna", "flora", "nosso", "alli", "como", "artes", "rara", "davam", "desta", "outro", "assim", "erros", "visto", "autor", "esta", "these", "isso", "errem", "croca", "cerva", "nunca", "garna", "fomo", "gombo", "esse", "lado", "suas", "obras", "lugar", "letra", "phene", "seus", "herva", "azaro", "atum", "taes", "casos", "facto", "mesma", "quem", "nota", "culta", "neste", "campo", "vinte", "dois", "annos", "larga", "meus", "entre", "achei", "tendo", "seja", "hajam", "seis", "essas", "vezes", "tido", "para", "luxar", "sujar", "usado", "gocho", "agra", "seto", "gaiar", "donde", "ferro", "tudo", "ouvir", "puros", "hedra", "hera", "tempo", "essa", "casal", "chama", "custa", "seria", "tarde", "algum", "acaso", "pouco", "dizer", "cunho", "local", "sabor", "hoje", "antes", "novas", "tomar", "foice", "pude", "norma", "termo", "ouve", "toda", "della", "outra", "chamo", "quero", "numa", "duas", "isto", "conta", "achou", "autos", "vira", "nada", "dever", "vedar", "abuso", "julga", "onde", "dito", "fica", "notar", "geral", "sejam", "tenha", "citar", "cinco", "devia", "ondas", "visse", "marau", "grifa", "grelo", "gaio", "eram", "puras", "sabe", "grave", "tanto", "torna", "caso", "massa", "fuga", "dado", "foram", "usos", "velha", "tupi", "povos", "falam", "falei", "estas", "sete", "daqui", "vivem", "aqui", "usada", "usoua", "agir", "bons", "ponto", "vista", "creio", "coisa", "tive", "quaes", "deve", "livro", "possa", "vejo", "longe", "qual", "julgo", "andei", "devo", "nica", "seres", "reino", "ordem", "tribo", "prole", "graus", "menor", "sobe", "cujo", "latim", "coube", "amplo", "nesse", "pelas", "passo", "havia", "largo", "trato", "gente", "abriu", "haver", "altas", "direi", "luxo", "tinha", "feito", "nomes", "senso", "estou", "aves", "dando", "zirro", "dados", "sirva", "mesmo", "abibe", "bibes", "bibi", "chega", "rigor", "fala", "viii", "luzes", "arte", "jogos", "novos", "novo", "oito", "raro", "vida", "longa", "amigo", "jogar", "ella", "corre", "casa", "logo", "texto", "levam", "tomo", "teve", "todo", "nesta", "nova", "cito", "oral", "falar", "item", "grado", "notei", "vimos", "quere", "disso", "podem", "prova", "venha", "corpo", "cave", "canem", "aviso", "segui", "fecho", "regra", "meia", "tomam", "lhes", "serve", "douto", "usava", "fummo", "cego", "igual", "lemos", "ouro", "oiro", "fazer", "devem", "pena", "lira", "tenho", "plana", "atraz", "ledor", "poria", "falso", "valor", "diria", "liceu", "velho", "terra", "sigo", "sons", "pede", "sinal", "voto", "cujos", "valem", "estes", "audaz", "mundo", "animo", "homem", "entra", "tirar", "nulo", "pesar", "deixa", "geito", "jeito", "vemos", "paiz", "quiz", "dizem", "raras", "fonte", "pois", "parar", "temos", "alto", "deram", "leram", "dias", "final", "feliz", "apraz", "arroz", "manda", "phase", "veio", "saiu", "meio", "vier", "veer", "malo", "coelo", "ferir", "lidos", "daria", "salvo", "tocar", "fruto", "mama", "ellas", "minha", "gota", "cana", "atar", "matar", "corda", "aptar", "perde", "linha", "disto", "santo", "septe", "ideal", "dotar", "junto", "levar", "pret", "bonet", "traje", "farei", "izar", "ambas", "justa", "isar", "grego", "izein", "vendo", "xiii", "elle", "trata", "vulgo", "muita", "recta", "trema", "viram", "godo", "poia", "feto", "ouvi", "lagos", "falte", "ufano", "ouviu", "nasal", "baca", "guvo", "andam", "andar", "vogal", "acaba", "norte", "botar", "surdo", "fixar", "bases", "anno", "abade", "oraes", "pais", "salmo", "luta", "tema", "actor", "recto", "posso", "idade", "cama", "haja", "serem", "acha", "diga", "prata", "rica", "bello", "abril", "data", "agudo", "surda", "digo", "caldo", "baixo", "leite", "fecha", "iria", "deixo", "sobre", "tanta", "fosse", "subre", "claro", "velas", "vento", "funil", "batel", "basta", "reis", "leme", "dono", "verbo", "ermo", "mormo", "esmo", "colmo", "resma", "sesmo", "judeu", "moio", "joio", "soito", "toiro", "loiro", "usar", "ideia", "fazem", "ontem", "usam", "lume", "crime", "votos", "xvii", "cofre", "teem", "cont", "pondo", "dada", "ramos", "curam", "quase", "persa", "disse", "idoso", "rosa", "comer", "xviii", "terei", "errar", "drusa", "moita", "caiba", "feita", "falou", "exige", "nisto", "vinha", "raros", "leis", "deduz", "lutam", "idos", "cedo", "trama", "abre", "estar", "tomei", "base", "terem", "somma", "cria", "glosa", "dessa", "acima", "verde", "frade", "silva", "urubu", "missa", "moda", "thema", "xxii", "alat", "alter", "angl", "anglo", "apher", "berb", "borg", "bret", "carth", "cast", "celt", "chil", "chin", "chulo", "comp", "conc", "cong", "conj", "contr", "corr", "xxiii", "defin", "escoc", "flam", "flex", "freq", "germ", "guar", "hebr", "hind", "holl", "hung", "idem", "imper", "inch", "infl", "ingl", "iron", "barb", "lisb", "prep", "pron", "lund", "ilha", "malab", "neerl", "neol", "nord", "norm", "obsol", "onom", "xxiv", "part", "pers", "peruv", "pess", "pleb", "poet", "port", "pref", "prop", "prov", "alent", "beir", "extr", "minh", "trasm", "provn", "quimb", "refl", "sent", "sign", "sing", "subst", "turc", "turco", "unif", "vasc", "veloc", "verb", "vers", "vulg", "zend", "zenda", "illa", "abrev", "datas", "circa", "ante", "riso", "noite", "eito", "aflus", "fluxo", "fato", "salto", "talho", "hora", "axis", "pegou", "casca", "vinho", "aata", "bico", "pato", "acies", "lados", "serra", "abba", "pelle", "abaco", "tiro", "gados", "mesa", "vidro", "cheia", "rosas", "badaq", "almas", "abbas", "dava", "morte", "dura", "cargo", "elege", "abado", "abas", "imite", "abafa", "modo", "mosto", "calor", "cobre", "bule", "bafo", "grito", "carta", "custo", "abafo", "milho", "cima", "acto", "basto", "bago", "bahu", "curva", "ruas", "cadas", "aguas", "fisga", "pesca", "olhos", "plano", "firme", "dente", "abalo", "fugir", "tiros", "medem", "balsa", "abama", "abano", "abana", "pedra", "banco", "roda", "banca", "reles", "bando", "banda", "palha", "ficou", "certa", "bango", "move", "leque", "anzol", "pano", "isca", "folho", "abapo", "abar", "barba", "cacho", "sola", "bolo", "nassa", "tenor", "roubo", "sexo", "cheio", "ataca", "negro", "padre", "priv", "basis", "coxim", "puro", "nariz", "abate", "navio", "cara", "eixo", "tumor", "seita", "abol", "servo", "bacia", "tacto", "abduz", "modos", "beato", "beber", "golla", "pecus", "gado", "beira", "cera", "nutre", "vivaz", "preto", "bemol", "arabe", "fixas", "raios", "fenda", "nesga", "redes", "seio", "bolso", "abrir", "opera", "drama", "dita", "bespa", "abeta", "otis", "tarda", "abete", "alvar", "abies", "abeto", "dama", "abia", "abio", "acido", "cedro", "abiga", "vespa", "ornar", "zona", "viver", "bios", "grau", "vive", "abita", "malva", "jugo", "agua", "ablui", "lava", "porta", "fique", "arco", "alas", "passe", "gesso", "cunha", "chapa", "bobo", "arma", "fraco", "gorda", "bocas", "chuva", "boca", "cabo", "raiva", "peixe", "morto", "anda", "tona", "boiar", "bras", "bois", "aboio", "canto", "boiz", "bolor", "criou", "abono", "abona", "docu", "ladra", "traja", "bordo", "causa", "eleva", "lisas", "filho", "gomos", "casas", "peito", "mesas", "reaes", "tino", "alna", "abra", "curar", "cujas", "lida", "nella", "volta", "cado", "ossos", "areal", "abrem", "livre", "abreu", "breve", "toma", "veias", "flor", "abro", "vindo", "quis", "olho", "abros", "stole", "fundo", "eidos", "bruma", "azul", "osso", "bruto", "altar", "losna", "falsa", "poder", "culpa", "gases", "suor", "votar", "lavar", "limpo", "dieta", "bulla", "voli", "boule", "abuna", "rico", "abur", "burel", "burro", "gatas", "abuta", "caixa", "magro", "coar", "corno", "cura", "ficar", "armas", "vulto", "piar", "bravo", "frue", "acca", "certo", "nelle", "oval", "tampa", "acahi", "hume", "fruta", "acaia", "tubo", "acaio", "tris", "acaju", "caju", "calar", "tado", "calmo", "asas", "solo", "seara", "doce", "soma", "carne", "porco", "canal", "puas", "unhas", "canco", "pisar", "canho", "ballo", "erva", "dedos", "poma", "rhin", "cauda", "oura", "mecha", "deita", "fumo", "acapu", "cons", "cardo", "umas", "alvo", "vacum", "caro", "affim", "acari", "leve", "acaro", "sarna", "passa", "horas", "lapas", "sesta", "tuas", "carro", "aonde", "leva", "forno", "acas", "macho", "acata", "verso", "tasso", "digno", "reter", "acato", "haste", "curta", "acava", "feixe", "junco", "egua", "moral", "actos", "poema", "actio", "ateia", "arder", "vela", "fogo", "lenha", "brios", "sueco", "alta", "vigor", "pague", "meios", "lhano", "cessa", "notas", "juizo", "grupo", "rios"];
# 518 palavras com mais de 05 letras e menos de 09
palavras_n2 = ["imprima", "morrer", "harmonia", "modernos", "graphias", "aquella", "ampliada", "alguns", "offerece", "trabalho", "prestado", "letras", "lutando", "adoptiva", "obscuros", "autores", "primeiro", "volume", "daquelle", "tempos", "sisuda", "menciono", "porque", "adduzo", "exemplos", "vazado", "moldes", "succedeu", "pararam", "tivessem", "esphera", "effeito", "internas", "moderna", "muitas", "coisas", "factos", "nossos", "mofino", "sestro", "cultor", "sempre", "estudo", "mestres", "milhares", "nossas", "ultramar", "melhor", "nomeada", "exemplo", "corrente", "paulada", "bruxedo", "palheiro", "plagiar", "granjear", "desvirar", "deparava", "sequer", "antiga", "popular", "daquella", "literato", "desceram", "erudita", "quinta", "eruditos", "quanto", "pobreza", "doutrina", "communs", "melhores", "podiam", "obstante", "ocioso", "embora", "outros", "definir", "pesebre", "pieira", "lacrau", "baceira", "torneja", "registem", "palavras", "igarvana", "mandem", "mucuna", "tornando", "similar", "escasso", "mercado", "nacional", "artigos", "qualquer", "memorar", "muiiii", "usaram", "decurso", "artigo", "souberam", "termos", "noutro", "diversos", "conhecia", "serviria", "grande", "refiro", "debalde", "picaveco", "plumbear", "panarei", "contudo", "aquelles", "marmanjo", "albatroz", "benzina", "azerar", "gorilla", "avessar", "delles", "abelha", "ambeta", "anserina", "aparinas", "aranha", "avessado", "azeredo", "muitos", "lacunas", "desabono", "dirige", "todavia", "dignos", "accusam", "capitaes", "durante", "despendi", "cuidados", "criado", "parecer", "quando", "escritor", "chamava", "depois", "residido", "arraigou", "mestre", "longos", "colheita", "andavam", "guardado", "incerta", "origem", "dessas", "outras", "deparam", "poucos", "antigos", "relegado", "desusada", "claror", "grossor", "calleja", "almofia", "doairo", "traguer", "trazer", "nembro", "confita", "ancinho", "ceivar", "orreta", "bramante", "barbante", "tenreiro", "guaiar", "cofinho", "inorar", "penetrar", "caminho", "avoengas", "antigas", "descudar", "bellos", "verguio", "mormente", "cheguei", "incluir", "verbas", "estariam", "intuitos", "procura", "apesar", "salvou", "livros", "devotado", "trinta", "aprendi", "aldeias", "perfeito", "dellas", "cidade", "esfumou", "cerros", "valles", "secular", "cedendo", "terreno", "plantas", "houver", "colher", "archivar", "consegui", "nelles", "valiosos", "belleza", "numeroso", "talvez", "seguir", "rigorosa", "chamei", "designo", "falado", "conhecem", "satisfaz", "processo", "simples", "verdade", "assombro", "tantos", "numerosa", "colhendo", "duvidosa", "obscura", "julgando", "cumprir", "natureza", "respeito", "impende", "tolerar", "capital", "entende", "formado", "consigna", "regista", "expungir", "defeitos", "vulgares", "condemno", "sabemos", "palavra", "thesoiro", "antigo", "moderno", "passando", "abrevar", "pequeno", "mancar", "faltar", "purista", "vivesse", "quatro", "sentir", "arranjar", "freire", "genebra", "bilhete", "besonha", "petigris", "poteia", "poterna", "abreuvar", "alegre", "abranjam", "phobia", "registo", "othodoxa", "ponderar", "inflija", "abeira", "bofetada", "esticar", "dinheiro", "penante", "pireza", "refilar", "reagir", "valente", "alavanca", "arrombar", "opporei", "reparos", "limitam", "estudos", "escrita", "falada", "detendo", "vulgar", "realizei", "locaes", "costumes", "enjeitou", "idioma", "europeia", "europeu", "recebeu", "entrou", "elemento", "portanto", "resultou", "haviam", "entrado", "apponho", "criados", "velhos", "partiram", "terras", "mortos", "partiu", "recebido", "geriza", "faneco", "alfafa", "alfaifa", "vergonha", "prezar", "equivale", "alguma", "ingrata", "valeram", "queixas", "contra", "largueza", "homens", "estudar", "fontes", "mingua", "prestar", "hesitar", "maiores", "passagem", "tinham", "escritos", "segundo", "escreve", "apenas", "imprensa", "gopiara", "gupiara", "gariroba", "gurejuba", "gurijuba", "guaiamum", "goiamum", "goiaba", "decidir", "exacta", "avisado", "leitor", "exegese", "resolver", "acatarei", "deveria", "chegar", "vegetaes", "vegetal", "aquelle", "classe", "cohorte", "planta", "figurar", "clareza", "cumpria", "observar", "offensa", "familias", "tribos", "referido", "preferir", "designar", "labiadas", "oppunha", "perderam", "estreito", "realizar", "registei", "detive", "colonial", "minhas", "noutros", "africana", "jardins", "primeira", "serviram", "largos", "ensejo", "jornaes", "directo", "frutos", "registar", "videiras", "entraram", "entram", "extenso", "menores", "surgiam", "colhido", "suspendi", "conheci", "composto", "derivada", "formavam", "quadrar", "secretas", "estreita", "sustar", "humano", "inventar", "vistosos", "intuito", "naquella", "alcance", "insectos", "limites", "especial", "procurei", "unidade", "refugir", "enfermam", "nenhum", "copioso", "refundir", "podiamos", "adquirir", "vermos", "animaes", "pedreiro", "guincho", "ferreiro", "afinal", "succede", "podendo", "inteiro", "gallispo", "galleno", "bisbis", "guizinho", "megengra", "variando", "reunir", "chapim", "patachim", "fradisco", "mezengro", "parachim", "cachapim", "fradinho", "revela", "devidos", "vaidade", "alarde", "auxiliar", "direito", "julgar", "aprouver", "julgue", "requeiro", "nestas", "autoriza", "affirmar", "lograram", "presente", "fabris", "militar", "gregas", "romanas", "omittir", "recentes", "humana", "melinite", "obedeci", "basear", "tivesse", "dezenas", "fadigas", "caminhos", "poderia", "abranger", "grossos", "volumes", "limitado", "mister", "editor", "arrojado", "incerto", "segunda", "saudoso", "hesitou", "dezena", "contos", "colhidos", "tornasse", "recursos", "maioria", "perigo", "exceder", "finado", "editora", "estranha", "voltar", "recordar", "triste", "successo", "retardou", "cessou", "remediar", "deixam"];
# 399 palavras com mais de 08 letras e menos de 12
palavras_n3 = ["documento", "linguagem", "registados", "portugueses", "satisfazer", "prescrita", "refundida", "corrigida", "portuguesa", "documentos", "leviandade", "mercantil", "monumentos", "laboriosas", "certamente", "nacionaes", "trabalhos", "similares", "inaugurou", "esmagados", "enormidade", "reconhece", "observado", "geralmente", "precederam", "conglobado", "thesoiros", "ampliando", "numerosas", "technologia", "industrial", "neologismo", "necessidade", "dirigisse", "conservados", "continente", "imperfeitos", "deparavam", "deferimento", "caudelaria", "plangente", "prefaciar", "agrupamento", "propositado", "reproductor", "empanturrar", "centenares", "raramente", "privativa", "folclorista", "restringida", "autoridade", "justificar", "distintos", "maniqueira", "gallacrista", "existiram", "fangapena", "marapinina", "perpetrem", "manifesto", "facilmente", "tantissimos", "enxameiam", "assombrosa", "conheceram", "registaram", "competente", "redigindo", "distribuida", "relativos", "pelagiano", "ampliadores", "empregaram", "batrachio", "inutilmente", "assexuado", "arachnidas", "camomilla", "parrochiano", "fundamento", "alquequenje", "astacites", "sobretudo", "determina", "principaes", "estimados", "serranias", "exaggerado", "celebrado", "provincias", "realmente", "consultado", "especiaes", "reverteram", "preciosos", "apropriadas", "numerosos", "ingenuidade", "capitular", "escritores", "manuscritos", "busaranhos", "quartapisa", "percorrer", "desviados", "expungiram", "pronunciar", "commummente", "gerecerse", "latinismos", "sonegadas", "exceptuando", "recolhido", "acentuado", "locomotiva", "locomotora", "entanguidas", "porventura", "resistindo", "continuar", "excepcional", "trasmontano", "signifique", "localidade", "respectivo", "alentejanos", "conhecidos", "distritos", "assentando", "excellentes", "primeiros", "desperdicei", "neologismos", "violentas", "alphabetei", "reproduzi", "experientes", "nimiamente", "tolerante", "reproduzir", "corrompido", "disparatado", "mulhermente", "gallicismos", "alongarei", "francesia", "barbarismo", "gallicismo", "incerteza", "confirmada", "perpetrado", "betarraba", "assembleia", "petimetre", "francesias", "portuguesas", "alludidos", "estranhos", "relacionado", "cangalhas", "catrafilar", "recebidas", "primeiras", "inoffensivo", "madeirense", "indigenas", "emancipou", "soberania", "organismo", "brasileira", "destinado", "prescindir", "praticada", "brasileiros", "romancistas", "entretanto", "provieram", "prosperam", "esquecidos", "alimentar", "comdemnada", "escreveram", "professores", "estudiosos", "respectivas", "soccorrer", "depararam", "advertirei", "procederam", "apparecem", "variantes", "guariroba", "gurandirana", "preferida", "registando", "remetendo", "vocabular", "afigurava", "collectiva", "subclasse", "variedade", "reduzindo", "taxinomia", "respeitei", "respeitando", "consagradas", "leguminosas", "provinham", "amplitude", "actualmente", "conhecidas", "cincoenta", "conheciam", "adaptariam", "coincidem", "parentesco", "conciliando", "enriquecer", "conseguiram", "inusitada", "recommendam", "qualidades", "medicinaes", "ornamentaes", "continental", "aconselhava", "registasse", "deparassem", "valorizam", "enriquessem", "consagraram", "reconhecer", "agricultura", "pertenciam", "variedades", "offerecia", "consultando", "confrades", "proseguir", "normalmente", "organizada", "elementos", "aventurei", "radioscopia", "exagerada", "adoptadas", "apparatoso", "productos", "largamente", "attendesse", "ampliaria", "lexicologia", "estabelecem", "apresentou", "prefaciando", "definidos", "catavento", "verificar", "avetoninha", "matoninha", "verdizella", "choradeira", "localidades", "seguintes", "chinchinim", "caldeirinha", "rabilongo", "melhorias", "semelhantes", "historiando", "processos", "facultaram", "importantes", "autorizados", "carinhoso", "populares", "actividade", "materiaes", "antolhavam", "organizar", "primitiva", "reconheci", "contribuiu", "colheitas", "succintas", "inventada", "inclinados", "substantivo", "adjectivo", "digressoar", "flavibico", "mostrasse", "brincando", "interpretem", "respectiva", "facilitar", "contraprova", "escrupuloso", "gratuitas", "praguentos", "improbidade", "consultar", "vocabulares", "representa", "dispersos", "pertencem", "devidamente", "sublinhados", "griphados", "lidimamente", "subscrevo", "escrevemos", "desusados", "exclusiva", "nobilitar", "pertencido", "significa", "violentos", "conhecida", "consignando", "extensiva", "intricado", "ensinaram", "habituaram", "convencidos", "ortographa", "resultado", "differentes", "autorizadas", "ministros", "professor", "cinquenta", "entrehabrir", "condemnando", "divergentes", "procuramos", "viceversa", "preconizar", "aconselham", "chancella", "lastimosas", "distincto", "significado", "preceitos", "civilisar", "portuguez", "expungisse", "prejudicial", "consoantes", "geminadas", "difficultar", "reformador", "possuindo", "facilitando", "filosofia", "corografia", "assumptos", "oligarchia", "ponderava", "conhecedor", "altamente", "represente", "consoante", "reconhecia", "complicada", "sentenciava", "introduzir", "humanistas", "estribados", "permittidas", "aventurasse", "escritora", "attenuada", "desideratos", "instantes", "salameleque", "calefrios", "enraizando", "aprazimento", "interessam", "officiaes", "organizados", "dilatando", "musulmano", "ampliarei", "fundamentos", "daquellas", "rigorosas", "costumeiras", "consideram", "amplamente", "aconselhada", "argumento", "prevalecer", "escasseiem", "hesitante", "quaesquer", "folhearam"];
# 362 palavras com mais de 11 letras e menos de 15
palavras_n4 = ["especialmente", "oficialmente", "copiosamente", "brilhantemente", "lexicographia", "relativamente", "disseminados", "cancioneiros", "quinhentistas", "principalmente", "internacional", "desconheceram", "lusitanismos", "amoravelmente", "desconhecidos", "diccionaristas", "conhecimento", "reconsiderar", "guerrilheiro", "enriqueceram", "surprehender", "justificaria", "collaboradores", "procuraremos", "patigabiraba", "spermatozoides", "escomberoides", "preoccupados", "religiosamente", "justificativos", "estrancinhar", "concomitante", "flexibilidade", "defrontarmos", "absolutamente", "provincianismo", "probabilidade", "esclarecimento", "inexplorados", "quatrocentos", "diccionarista", "lucreciamente", "convictamente", "consciencioso", "estrangeirismo", "ultramarinas", "concernentes", "precisamente", "constituinte", "pessoalmente", "brasileirismos", "considerados", "vocabularistas", "portuguesismos", "descobridores", "colonizadores", "perendengues", "injustamente", "comprehendesse", "obsequiosidade", "dificuldades", "difficuldades", "guarandirana", "naturalmente", "simplicidade", "simplesmente", "desenvolvido", "exclusivamente", "difficilmente", "perfeitamente", "difficuldade", "nomenclatura", "desnecessidade", "recentemente", "nomencladores", "pharmacologia", "desmedidamente", "especialidade", "effectivamente", "nomeadamente", "percorrermos", "abesconhinha", "donzellaverde", "especialistas", "antiguidades", "descobrimentos", "visivelmente", "lapantanamente", "manticostumes", "minotaurizado", "originalidades", "intencionados", "possibilidade", "difficultando", "minudencioso", "succintamente", "acompanhadas", "melhoramentos", "opportunidade", "directamente", "vernaculidade", "disparatados", "inteiramente", "sucessivamente", "orthographia", "generalidade", "mediocremente", "orthographam", "orthographias", "implicitamente", "intolerantes", "exclusivismos", "phoneticamente", "reproduziria", "diametralmente", "analphabetismo", "estimulassem", "simplificaram", "uniformizando", "estrangeiros", "infinitamente", "preambulando", "improficuidade", "envelhecidos", "convenientes", "precipitadas", "sensatamente", "inconsciente", "correspondente", "simplificada", "determinadas", "desconhecemos", "ingenuamente", "generalizada", "preoccuparam", "convencional", "correspondia", "legitimamente", "desconhecida", "completamente", "pronunciamos", "primitivamente", "portugalense", "conimbricense", "desapparecido", "preponderante", "intransigentes", "eruditamente", "concordantes", "estabelecidos", "uniformidade", "ensinamentos", "genuinamente", "substituindo", "levianamente", "generalizado", "apresentanos", "incontestada", "despoticamente", "graphicamente", "rigorosamente", "interessantes", "representada", "exploradores", "africanistas", "inarticulado", "photographia", "intermittente", "pronunciandose", "acontecimento", "graficamente", "representado", "immediatamente", "propangandista", "subordinasse", "intencionadas", "radicalismos", "essencialmente", "subordinarse", "simplificadas", "orthographica", "substituidas", "judiciosamente", "hellespontico", "distinguirse", "desfiguraria", "pronunciaram", "seguidamente", "insignificante", "phoneticistas", "representando", "indifferente", "independente", "proximamente", "interpretarem", "legitimidade", "dispensarmos", "acertadamente", "vantajosamente", "interessante", "descobrimento", "simplifiquei", "reproduzindo", "estranjeiros", "progredimento", "documentando", "pertencentes", "reuchliniana", "significarem", "conhecedores", "apparecimento", "grammaticaes", "circunscrita", "nacionalizando", "aprofundando", "comprehenderam", "communicados", "honestamente", "desenfrechar", "pulpitamente", "aumentativos", "correspondam", "diversamente", "mansuetissimo", "superlativos", "disseminadas", "integralmente", "caboverdeano", "chancellaria", "demonstrativo", "depreciativo", "ecclesiastico", "frequentativo", "conjunccional", "onomatopaico", "qualificativo", "intransitivo", "significando", "tentosamente", "extremidades", "abacamartado", "abacamartada", "abacelamento", "abacellamento", "rhinoceronte", "abalroamento", "abafadamente", "instrumentos", "espectadores", "abahuladamente", "abahulamento", "abairramento", "perpendicular", "inferiormente", "abajoujamento", "impressionado", "abalizadamente", "abalizamento", "abaluartamento", "solitariamente", "abandonamento", "abarracamento", "abarregamento", "abarrotamento", "abastadamente", "fornecimento", "abastardamento", "abastecimento", "abastosamente", "abatidamente", "abauladamente", "superiormente", "abdominoscopia", "abelhudamente", "abencerragens", "abencerrajens", "aberingelado", "propriamente", "desarrazoadas", "abibliotecar", "abibliothecar", "terebentinas", "profundidades", "profundidade", "abjectamente", "judicialmente", "caracterizadas", "ablamellares", "desapparecer", "abobadilheiro", "aborrecimento", "aboletamento", "abolicionismo", "abolicionista", "abominabilis", "abominosamente", "abonadamente", "apresentando", "arredondadas", "aborridamente", "abrandamento", "abrasadamente", "abrasileirado", "abrasileirar", "numericamente", "anesthesiado", "abreviadamente", "abreviamento", "abricoqueiro", "albricoqueiro", "abrolhamento", "intertropical", "abruptamente", "abrutadamente", "occultamente", "absinthiatus", "absolvimento", "coefficientes", "absorvedoiro", "absorvedouro", "absorvimento", "abstencionista", "insuladamente", "abstractamente", "abstrahimento", "separadamente", "abstraimento", "abstrusamente", "abstrusidade", "absurdamente", "caracterizada", "afroixamento", "abundantemente", "abundosamente", "maliciosamente", "abusivamente", "acabadamente", "acachafundar", "pseudoacacia", "brasiliensis", "academialmente", "academicamente", "garridamente", "acafelamento", "substanciosa", "indehiscente", "acairelamento", "acalcanhamento", "acalcanharem", "acalefologia", "celenterados", "aconchegando", "acalephologia", "tranquillizar", "comprehendem", "acamptosomos", "longitudinal", "acanaveadura", "acanhadamente", "acanonicamente", "transgressor", "introduzidos"];
# 297 palavras com mais de 14 letras e menos de 18
palavras_n5 = ["successivamente", "irregularidades", "inconscientemente", "provincianismos", "impossibilidade", "despreoccupasse", "excepcionalmente", "responsabilidade", "necessariamente", "consubstanciarse", "convencionalmente", "desconhecimento", "suficientemente", "estrangeirismos", "desacompanhados", "circunflexamente", "independentemente", "esclarecimentos", "aproximadamente", "estabelecimentos", "propositadamente", "subrepticiamente", "convenientemente", "abalaustramento", "abandonadamente", "desenvolvimento", "abespinhadamente", "inesperadamente", "abominavelmente", "pretensiosamente", "aborrecidamente", "abrachiocefalia", "abraquiocefalia", "absorpciometria", "acabrunhadamente", "longitudinalmente", "atabalhoadamente", "acantopterigiano", "acariciadamente", "acaudilhadamente", "acauteladamente", "acceitabilidade", "acceleradamente", "accessibilidade", "accessoriamente", "accidentalmente", "accidentariamente", "accommodadamente", "accrescentamento", "accumuladamente", "accumulativamente", "accusatoriamente", "achincalhamento", "acidentariamente", "acobardadamente", "acompleicionado", "acondicionamento", "aconselhadamente", "administrativos", "acostumadamente", "acrescentamento", "acumulativamente", "acusatoriamente", "antecipadamente", "estabelecimento", "adjectivadamente", "administradeira", "administrativas", "administrativus", "admirativamente", "admissibilidade", "adulatoriamente", "adulteradamente", "adventiciamente", "adversativamente", "aerogastrectasia", "aeroterapeutica", "aferrenhadamente", "afervoradamente", "afirmativamente", "afidalgadamente", "aformoseadamente", "aforquilhamento", "afortunadamente", "afrancesadamente", "afrodisiografia", "agasalhadamente", "momentaneamente", "agglutinabilidade", "aggressivamente", "agigantadamente", "aglutinabilidade", "agradabilissimo", "agradecidamente", "simultaneamente", "aguardentadamente", "aguilhoadamente", "ajuramentadamente", "complicadamente", "alambazadamente", "alambicadamente", "alapardadamente", "insignificantes", "alcandoradamente", "alcantiladamente", "artificialmente", "particularidade", "atrapalhadamente", "alfabetadamente", "alfabeticamente", "correspondentes", "trinitrocelulose", "escrofularineas", "perpendiculares", "indistintamente", "apaixonadamente", "alternativamente", "alvorotadamente", "amarguradamente", "amedrontadamente", "amesquinhamento", "metamorfosearem", "indecorosamente", "desordenadamente", "scientificamente", "amfiguricamente", "amplificadamente", "anacoreticamente", "anagliptografia", "anagramaticamente", "enfraquecimento", "anatripsiologia", "insensibilidade", "micropusunicolor", "desaparecimento", "anfibologicamente", "anfiguricamente", "anfractuosidade", "angustiadamente", "animalculovismo", "animalculovista", "aniversariamente", "anniversariamente", "anniversariante", "anomocardiostenia", "antecedentemente", "anteconhecimento", "precedentemente", "antropocentrismo", "antropocentrista", "antropomorfismo", "antropomorfista", "antiaristocrata", "antibonapartismo", "antibonapartistas", "antibonapartista", "antichristandade", "antichristianismo", "anticivilizador", "anticontagionista", "anticristandade", "anticristianismo", "antidesnutritivo", "antiescrofuloso", "antiespiritismo", "antiespiritista", "antigalicanismo", "antigovernamental", "antiministerial", "antigrammatical", "antihemorroidal", "antiliberalismo", "anteroposterior", "antimonarchista", "antimonarquista", "antiparalelismo", "antiparlamentar", "antipatriotismo", "antipestilencial", "antiprogressista", "antiprotestante", "antiracionalismo", "antiregulamentar", "antirepublicano", "antireumatismal", "antirracionalismo", "antirreformista", "antirregulamentar", "antirrepublicano", "antirreumatismal", "antisociabilidade", "antispiritualismo", "antissocialismo", "antissocialista", "antivaticanista", "antrecambadamente", "constrangidamente", "aparelhadamente", "apaziguadamente", "aperceptibilidade", "depreciativamente", "aportuguesamento", "determinadamente", "apostolicamente", "apreensivamente", "aprobativamente", "apropriadamente", "apreensibilidade", "apressuradamente", "aprimoradamente", "apropositadamente", "aprostatotrofia", "aproveitadamente", "aprovisionamento", "aquadrilhamento", "arbitrariamente", "archiepiscopado", "archimandritado", "archimoquenqueiro", "architectonicus", "architecturista", "aristodemocracia", "aristodemocrata", "aritmeticamente", "representativos", "arquiepiscopado", "arquimandritado", "arquimoquenqueiro", "arquitecturista", "arrebatadamente", "arrebatapunhadas", "arrebatosamente", "distanciadamente", "arremessadamente", "precipitadamente", "continuadamente", "arrevesadamente", "arterioesclerose", "articuladamente", "artificialidade", "artificiosamente", "assambarcamento", "asseguradamente", "asseveradamente", "assimilabilidade", "indefinidamente", "assinaladamente", "assoldadadamente", "assombrosamente", "assumpcionistas", "mastoidooccipital", "astragalectomia", "astragalomancia", "astrologicamente", "astronomicamente", "atabernadamente", "atemorizadamente", "atormentadamente", "impertinentemente", "atravancadamente", "atravessadamente", "atregulhadamente", "atribuladamente", "atropeladamente", "attenciosamente", "auspiciosamente", "autochtoneidade", "automaticamente", "automobilistico", "autonomicamente", "autorizadamente", "auxiliariamente", "avantajadamente", "imprevistamente", "semitransparente", "aventurosamente", "averiguadamente", "avinagradamente", "bacchalaureatus", "bacteriologista", "bacterioterapia", "indiscretamente", "massarandubeira", "balbuciantemente", "imperfeitamente", "incorrectamente", "negligentemente", "barbarissonante", "transversalmente", "barometricamente", "barometrografia", "horizontalmente", "entrecruzamento", "electropositivo", "batologicamente", "battologicamente", "immoderadamente"];
# 226 palavras com mais de 17 letras
palavras_n6 = ["lexicograficamente", "simplificacionistas", "administracionalizar", "administrationaliser", "administrativamente", "anticonstitucional", "anticonstitucionalmente", "antidesassimilador", "antiespiritualismo", "antirepublicanismo", "antirrepublicanismo", "antissociabibilidade", "antiviviseccionista", "antivivisseccionista", "aportuguesadamente", "architectonografia", "arenicalcinzamento", "consubstancialidade", "aristocraticamente", "arquitectonografia", "perpendicularmente", "bastantissimamente", "bolboprotuberancial", "caracteristicamente", "ceremoniaticamente", "circumstanciadamente", "circunstanciadamente", "incondicionalmente", "colecistenterostomia", "colpoperineoplastia", "colpoperineorrafia", "compreensibilidade", "compreensivelmente", "congregacionalista", "conscienciosamente", "constantinopolitano", "constantinopolitanus", "constitucionalidade", "constitucionalismo", "constitucionalista", "constitucionalizar", "constitucionalmente", "consubstancialitas", "consubstancialmente", "extraordinariamente", "contemplativamente", "contemporaneamente", "contraditoriamente", "correspondentemente", "imperceptivelmente", "demonstrativamente", "desacauteladamente", "desacompanhadamente", "desaconselhadamente", "despropositadamente", "desacostumadamente", "desafortunadamente", "desagradecidamente", "desapaixonadamente", "desaparelhadamente", "desapercebidamente", "desaproveitadamente", "desassombradamente", "desassossegadamente", "desavergonhadamente", "desceremoniosamente", "descompassadamente", "desconcertadamente", "desconfortadamente", "descontinuadamente", "desconversavelmente", "desembrulhadamente", "desencabrestadamente", "desencadernadamente", "desapropositadamente", "desencaminhadamente", "desencapotadamente", "desenfastiadamente", "desincompatibilizar", "desinteressadamente", "desnecessariamente", "despreocupadamente", "despretensiosamente", "desproporcionadamente", "desqualificadamente", "desresponsabilizar", "discretissimamente", "dissemelhantemente", "enantiopaticamente", "estenograficamente", "estereotipicamente", "estratificadamente", "experimentavelmente", "exterritorialidade", "extrajudicialmente", "extraoficialmente", "superabundantemente", "fantasmagoricamente", "albiziaodoratissima", "fenilidroquinazolina", "fermentescibilidade", "responsabilizandose", "supersticiosamente", "entrincheiramentos", "fotocromaticamente", "gastroconjuntivite", "gastroenterocolite", "gastroenterostomia", "hiperintelectualidade", "imisericordiosamente", "imperceptibilidade", "imperfectibilidade", "imperturbabilidade", "imperturbavelmente", "impremeditadamente", "imprescriptibilidade", "impressionabilidade", "improporcionalidade", "improporcionalmente", "inconvenientemente", "improrrogabilidade", "imputrescibilidade", "inacreditavelmente", "incombustibilidade", "incomensurabilidade", "incomensuravelmente", "incomunicabilidade", "incomunicavelmente", "incomportavelmente", "incompreensibilidade", "incompreensivelmente", "incompressibilidade", "inconciliabilidade", "inconciliavelmente", "incontestavelmente", "incondicionalidade", "inconquistabilidade", "inconscienciosamente", "inconsequentemente", "inconsideradamente", "inconstitucionalidade", "inconstitucionalmente", "incontestabilidade", "incontrastavelmente", "incorruptibilidade", "incorruptivelmente", "indescriptibilidade", "indescriptivelmente", "indescritibilidade", "indescritivelmente", "indestructibilidade", "indestructivelmente", "indestrutibilidade", "indestrutivelmente", "indeterminabilidade", "indeterminadamente", "indisciplinabilidade", "indisciplinadamente", "indiscriminadamente", "indispensabilidade", "indispensavelmente", "inextinguibilidade", "infermentescibilidade", "inhospitaleiramente", "ininteligivelmente", "ininterrompidamente", "inospitaleiramente", "inquestionavelmente", "institucionalmente", "insubordinadamente", "insubstancialidade", "insuficientemente", "insurreccionalmente", "intercorrentemente", "interlocutoriamente", "intermediariamente", "internacionalidade", "internacionalmente", "interparlamentares", "interpretativamente", "intransmissibilidade", "intuspectivamnente", "irreconciliavelmente", "irrecuperavelmente", "irrepreensibilidade", "irrepreensivelmente", "irresponsabilidade", "irresponsavelmente", "irretractavelmente", "irreverenciosamente", "irrivalizavelmente", "incompatibilidades", "lepidopterologista", "mefistofelicamente", "megalantropogenesia", "misericordiosamente", "notabilissimamente", "malvasiapenaguiota", "perpendicularidade", "proporcionadamente", "quadruplicadamente", "qualificativamente", "quintuplicadamente", "reproductibilidade", "resplandecentemente", "revolucionariamente", "sanguinolentamente", "satisfactoriamente", "significativamente", "simplicissimamente", "simplificacionista", "fibrocartilaginosa", "sobrecelestialmente", "sorpreendentemente", "substantivadamente", "superexcitabilidade", "surpreendentemente", "transcendentalismo", "transcendentalista", "transcendentalmente", "transfiguradamente", "transmissibilidade", "transmissivelmente", "transordinariamente", "trigonometricamente", "cordealissimamente"];

def main():
	vidas = 6
	letras = []
	nivel = 0;

	while (nivel != 1 and nivel != 2 and nivel != 3 and nivel != 4 and nivel != 5 and nivel != 6 and nivel != 7):
		print("Tamanho da palavra: ")
		print("(1) MUITO PEQUENA")
		print("(2) PEQUENA")
		print("(3) POUCO PEQUENA")
		print("(4) POUCO GRANDE")
		print("(5) GRANDE")
		print("(6) MUITO GRANDE")
		print("(7) ALEATÓRIO")
		nivel = int(input(">"))
		pass

	if (nivel == 7):
		nivel = rd.randrange(1, 7)

	if (nivel == 1):
		palavras = palavras_n1
	elif (nivel == 2):
		palavras = palavras_n2
	elif (nivel == 3):
		palavras = palavras_n3
	elif (nivel == 4):
		palavras = palavras_n4
	elif (nivel == 5):
		palavras = palavras_n5
	else:
		palavras = palavras_n6

	resposta = palavras[rd.randrange(0, len(palavras))].upper()
	palavra = ["_" for i in range(len(resposta))]

	mostrarPalavra(palavra)

	while (vidas > 0 and naoGanhou(palavra)):
		letras.append(input("Digite uma letra: ").upper())
		print("")

		if (caractereInvalido(letras[-1])):
			print("Caractere inválido")
			letras.pop()

		elif (letraRepetida(letras)):
			print("Letra repetida")
			letras.pop()

		elif (naoAcertou(letras[-1], resposta, palavra)):
			vidas -= 1
			if (vidas > 0):
				print("Você errou pela " + str(6 - vidas) + "ª vez. Tente de novo!")

		print("Vidas: " + str(vidas))
		mostrarLetras(letras)
		mostrarPalavra(palavra)
		pass

	if (naoGanhou(palavra)):
		print("Enforcado!")
		print("A palavra era: " + resposta)
	else:
		print("Você ganhou. Parabéns!")

def caractereInvalido(c):
	if (len(c) > 1):
		return True
	elif (ord(c) > 64 and ord(c) < 91):
		return False
	else:
		return True

def letraRepetida(letras):
	repetida = False

	for i in range(len(letras) - 1):
		if (letras[i] == letras[-1]):
			repetida = True
		pass

	return repetida

def mostrarLetras(letras):
	print("Letras já testadas: " + ' '.join(letras))

def mostrarPalavra(palavra):
	print("A palavra é:     " + ' '.join(palavra))

def naoAcertou(letra, resposta, palavra):
	nao_acertou = True

	for i in range(len(resposta)):
		if (resposta[i] == letra):
			nao_acertou = False
			palavra[i] = letra
		pass

	return nao_acertou


def naoGanhou(resposta):
	nao_ganhou = False

	for i in resposta:
		if (i == "_"):
			nao_ganhou = True
		pass

	return nao_ganhou

main()