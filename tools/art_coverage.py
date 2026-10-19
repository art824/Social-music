"""Check which album-art sources find cover art for a list of albums. Python 3 standard library only.
Run:  python3 tools/art_coverage.py
"""
import json, time, urllib.parse, urllib.request, urllib.error

# (artist, album, group). Underground picks are best-effort from memory: swap in your own.
ALBUMS = [
    ("Bad Bunny", "Un Verano Sin Ti", "mainstream"),
    ("Taylor Swift", "1989", "mainstream"),
    ("Kendrick Lamar", "GNX", "mainstream"),
    ("Matuê", "Máquina do Tempo", "brazil trap"),
    ("Matuê", "30PRAUM", "brazil trap"),
    ("Racionais MC's", "Sobrevivendo no Inferno", "brazil rap"),
    ("Peso Pluma", "Génesis", "mexican"),
    ("Natalia Lafourcade", "Hasta la Raíz", "mexican"),
    ("Baco Exu do Blues", "Esú", "brazil underground"),
    ("Don L", "Roteiro pra Aïnouz Vol. 2", "brazil underground"),
    ("Jovem Dionisio", "Acorda Pedrinho", "brazil indie"),
    ("Boogarins", "Manual", "brazil indie"),
    ("Black Country, New Road", "For the first time", "uk indie"),
    ("Squid", "Bright Green Field", "uk indie"),
    ("Dry Cleaning", "New Long Leg", "uk indie"),
    ("Porridge Radio", "Every Bad", "uk indie"),
    ("Sorry", "925", "uk indie"),
    ("black midi", "Schlagenheim", "uk indie"),
]
UA = {"User-Agent": "social-music-art-test/0.1 (personal prototype)"}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15) as r:
        return r.status, r.read()

def itunes(artist, album):
    q = urllib.parse.urlencode({"term": f"{artist} {album}", "entity": "album", "limit": 1})
    d = json.loads(get("https://itunes.apple.com/search?" + q)[1])
    return bool(d["results"])

def deezer(artist, album):
    q = urllib.parse.urlencode({"q": f'artist:"{artist}" album:"{album}"', "limit": 1})
    d = json.loads(get("https://api.deezer.com/search/album?" + q)[1])
    return bool(d.get("data"))

def caa(artist, album):
    q = urllib.parse.urlencode({"query": f'releasegroup:"{album}" AND artist:"{artist}"', "fmt": "json", "limit": 1})
    d = json.loads(get("https://musicbrainz.org/ws/2/release-group?" + q)[1])
    time.sleep(1.1)
    if not d.get("release-groups"):
        return False
    try:
        return get(f"https://coverartarchive.org/release-group/{d['release-groups'][0]['id']}/front")[0] == 200
    except urllib.error.HTTPError:
        return False

sources = {"iTunes": itunes, "Deezer": deezer, "CoverArtArchive": caa}
hits = {n: 0 for n in sources}
print(f"{'album':52}{'group':20}" + "".join(f"{n:17}" for n in sources))
for artist, album, group in ALBUMS:
    row = f"{(artist + ' - ' + album)[:50]:52}{group:20}"
    for n, fn in sources.items():
        ok = None
        for attempt in range(3):
            try:
                ok = fn(artist, album)
                break
            except Exception as e:
                err = str(e)
                time.sleep(3 * (attempt + 1))
        time.sleep(1.5)
        hits[n] += bool(ok)
        row += f"{'ERR' if ok is None else ('yes' if ok else 'NO'):17}"
    print(row)
print("\nfound:", {n: f"{c}/{len(ALBUMS)}" for n, c in hits.items()})
