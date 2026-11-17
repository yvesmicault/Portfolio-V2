import json, re, os, sys
REPO = '/home/user/portfolio-v2'
AGJ = '/mnt/project-files/prototype/accueil-v4/data/globe/agence.json'

s = open(REPO + '/data.js').read()
parts = re.split(r'window\.(\w+)\s*=', s)
D = {parts[i]: json.loads(parts[i + 1].strip().rstrip(';')) for i in range(1, len(parts), 2)}
V2 = {p['id']: p for p in D['PROJ']}

def nat_of(n):
    if re.search(r'logement|coliving|résidence', n, re.I): return 'Logement'
    if re.search(r'bureau|siège|tertiaire', n, re.I): return 'Bureau'
    if re.search(r'projet urbain|urbanisme|quartier|zac|plan[- ]guide|îlot|metropole|métropole', n, re.I): return 'Urbanisme'
    if re.search(r'espace public|place|parc|paysag|jardin|promenade', n, re.I): return 'Espace public'
    return 'Équipement'

def stat_of(p):
    st, ph = p.get('st') or '', p.get('ph') or ''
    if re.search(r'livré', st, re.I): return 'Livré'
    if re.search(r'en cours|arrêt', st, re.I): return 'En études'
    if re.search(r'^(études|pro/dce|esquisse|faisabilité|avant-projet|permis)', ph, re.I): return 'En études'
    return 'Concours'

out = []
for p in json.load(open(AGJ))['p']:
    v = V2.get(p['id'], {})
    img = 'img/agt/%s.jpg' % p['id'] if os.path.exists(REPO + '/img/agt/%s.jpg' % p['id']) else None
    hero = v.get('hero') if v.get('hero') and os.path.exists(REPO + '/' + v['hero']) else None
    nat=nat_of(p.get('n', ''))
    nat={'le-cabanon-ideal-2023':'Logement','concours-vannes-2023':''}.get(p['id'],nat)
    out.append(dict(id=p['id'], t=p['t'], c=p['c'], y=int(p['y']) if str(p.get('y', '')).isdigit() else None,
                    k='a', nat=nat, stat=stat_of(p), prog=p.get('n', ''), s=p.get('s', ''),
                    ph=p.get('ph', ''), r=p.get('r', ''), st=p.get('st') or '', ll=p['ll'],
                    th=img, hero=hero or img, txt=v.get('txt', ''), src='Hamonic + Masson',
                    cr=v.get('cr', '')))

# Études (e) et concours personnels (c) : fiches complètes du dépôt V2
NAT_E = {'varese': 'Équipement', 'agri': 'Urbanisme', 'terminus': 'Équipement', 'elle': 'Équipement',
         'ventres': 'Urbanisme', 'crank': 'Logement', 'synergies': 'Urbanisme', 'siberian': 'Équipement',
         'equilibrium': 'Espace public'}
for p in D['PROJ']:
    if p['fam'] == 'a': continue
    f = dict(p['fiche'])
    out.append(dict(id=p['id'], t=p['t'], c=p['c'], y=p.get('y1') or p['y'], k=p['fam'], nat=NAT_E[p['id']],
                    stat='Étude' if p['fam'] == 'e' else 'Concours', prog=f.get('Programme', ''),
                    s=f.get('Surface', ''), ph=f.get('Nature', ''), r=p.get('role', ''), st='', ll=p['ll'],
                    th=p.get('th'), hero=p.get('hero'), txt=p.get('txt', ''), pl=p.get('pl', []),
                    src='Études' if p['fam'] == 'e' else 'Concours personnels', line=p.get('line', '')))

PROFIL = {
  'quote': 'L’architecture ne se résume pas à ce que l’on construit, mais à ce que l’on rend possible.',
  'contact': [['Courriel', 'ymicault@gmail.com'], ['Téléphone', '+33 7 60 86 66 62'], ['Ville', 'Marseille, France'],
              ['En agence', 'Hamonic + Masson'], ['Disponible', 'À partir de janvier 2027']],
  'pres': [
    'Mon parcours s’est construit entre Reims, Clermont-Ferrand et Moscou, au fil d’une formation qui m’a progressivement amené à considérer l’architecture au-delà du seul acte de bâtir. Le master EVAN, consacré aux relations entre ville, architecture et nature, a notamment nourri une réflexion sur les territoires, leurs transformations et les liens parfois fragiles qui unissent le paysage, le bâti et les usages.',
    'Depuis 2017, cette approche s’est enrichie d’une pratique professionnelle au sein de l’agence Hamonic + Masson, à Paris puis à Marseille. De la conception aux phases de développement technique, à travers des projets de logements, d’équipements et d’opérations urbaines, j’ai appris à confronter l’intention architecturale à la complexité du réel. Cette expérience, aujourd’hui portée par des responsabilités de chef de projet, m’a convaincu que la rigueur constructive et la sensibilité architecturale ne s’opposent pas, mais se nourrissent mutuellement.'],
  'philo': [
    'Je considère l’architecture moins comme la production d’un objet que comme une manière de révéler les qualités d’un lieu et d’en imaginer les possibles. Chaque territoire porte une histoire, des usages, des contraintes et des ressources qui méritent d’être observés avant d’être transformés. Le projet devient alors un travail de lecture et d’interprétation, une recherche d’équilibre entre ce qui préexiste et ce qui peut advenir.',
    'Cette conviction nourrit une attention particulière aux relations que l’architecture établit : entre le bâti et le paysage, entre l’intime et le collectif, entre la permanence des lieux et l’évolution des modes de vie. J’aspire à une architecture à la fois sensible et rationnelle, capable de répondre aux réalités de son époque sans renoncer à la simplicité de ses intentions.',
    'Car la justesse d’un projet ne tient pas seulement à ce qu’il apporte, mais aussi à la manière dont il trouve sa place, dialogue avec ce qui l’entoure et laisse ouvertes les possibilités de demain.'],
  'jalons': [[2009, 'BTCA, Reims'], [2013, 'Licence, Clermont-Ferrand'], [2014, 'Institut d’architecture de Moscou'],
             [2016, 'Diplôme, master EVAN'], [2017, 'Hamonic + Masson'], [2021, 'Europan 16, mentionné'],
             [2023, 'HMONP'], [2027, '…']],
  'exp': [['Depuis mars 2017', 'Hamonic + Masson Architectes, Paris · Marseille', 'Architecte / chef de projet, conception et études'],
          ['2016', 'ENSACF, Clermont-Ferrand', 'Monitorat en projet architectural et morphologie urbaine'],
          ['Nov. 2015', 'Epicentre Faktory, Clermont-Ferrand', 'Conférence sur l’agriculture urbaine'],
          ['Avr.–juil. 2015', 'Megabudka, Moscou', ''], ['Fév.–mars 2013', 'Neumann Architecte, Riom', ''],
          ['Mai–juin 2012', 'Asylum, Lyon', ''], ['Fév. 2011', 'B+A Planchon, Châlons-en-Champagne', ''],
          ['Fév. 2008', 'Eudes Architecture, Châlons-en-Champagne', '']],
  'form': [['2022 — 2023', 'HMONP', 'ENSA Clermont-Ferrand'],
           ['2015 — 2016', 'Diplôme d’architecte DE', 'ENSA Clermont-Ferrand, master 2 EVAN'],
           ['2014 — 2015', 'Institut d’architecture de Moscou', 'МАРХИ'],
           ['2009 — 2013', 'Licence en architecture', 'ENSA Clermont-Ferrand'],
           ['2007 — 2009', 'BTCA, brevet de technicien collaborateur d’architecte', 'Lycée Arago, Reims']],
  'cv': D['CV'], 'pdf': 'doc/CV_2026_Yves_Micault.pdf'}

js = 'window.RP=' + json.dumps(out, ensure_ascii=False) + ';\nwindow.RPROFIL=' + json.dumps(PROFIL, ensure_ascii=False) + ';\n'
open(REPO + '/recomposition/data.js', 'w').write(js)
import collections
print(len(out), collections.Counter(p['nat'] for p in out), collections.Counter(p['stat'] for p in out),
      sum(1 for p in out if p['th']), sum(1 for p in out if p['hero']))
missing = [p['hero'] for p in out if p['hero'] and not os.path.exists(REPO + '/' + p['hero'])] + [p['th'] for p in out if p['th'] and not os.path.exists(REPO + '/' + p['th'])]
print('missing', missing)
