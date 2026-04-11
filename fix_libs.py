import os
import hashlib
import urllib.request
import urllib.error

lib_dir = os.path.join(os.environ['APPDATA'], '.shangrimc', 'common', 'libraries')

# From forge-1.20.1-47.4.20-version.json - exact SHA1 and sizes
libs = [
    {
        "path": "cpw/mods/securejarhandler/2.1.10/securejarhandler-2.1.10.jar",
        "url": "https://maven.minecraftforge.net/cpw/mods/securejarhandler/2.1.10/securejarhandler-2.1.10.jar",
        "sha1": "51e6a22c6c716beb11e244bf5b8be480f51dd6b5",
        "size": 88749
    },
    {
        "path": "org/ow2/asm/asm/9.9.1/asm-9.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar",
        "sha1": "2ceea6ab43bcae1979b2a6d85fc0ca429877e5ab",
        "size": 126252
    },
    {
        "path": "org/ow2/asm/asm-commons/9.9.1/asm-commons-9.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/ow2/asm/asm-commons/9.9.1/asm-commons-9.9.1.jar",
        "sha1": "ab35de4c537184a09339069f1a3b3aacf2289149",
        "size": 75010
    },
    {
        "path": "org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/ow2/asm/asm-tree/9.9.1/asm-tree-9.9.1.jar",
        "sha1": "b6b1b3366296163b4b1f540731aad0a2baa484d8",
        "size": 51963
    },
    {
        "path": "org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/ow2/asm/asm-util/9.9.1/asm-util-9.9.1.jar",
        "sha1": "e51f5b0ae0b0c1960687ae970a2a3434d39d8abb",
        "size": 94643
    },
    {
        "path": "org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/ow2/asm/asm-analysis/9.9.1/asm-analysis-9.9.1.jar",
        "sha1": "1ab8d9316ef7a67240087919a708246c37ed1660",
        "size": 35170
    },
    {
        "path": "net/minecraftforge/accesstransformers/8.0.4/accesstransformers-8.0.4.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/accesstransformers/8.0.4/accesstransformers-8.0.4.jar",
        "sha1": "272d240aa73f42195b2a68e2ebd8b701ecf41f63",
        "size": 77756
    },
    {
        "path": "org/antlr/antlr4-runtime/4.9.1/antlr4-runtime-4.9.1.jar",
        "url": "https://maven.minecraftforge.net/org/antlr/antlr4-runtime/4.9.1/antlr4-runtime-4.9.1.jar",
        "sha1": "428664f05d2b7f7b7610204b5aa7c1763f62011a",
        "size": 337868
    },
    {
        "path": "net/minecraftforge/eventbus/6.2.33/eventbus-6.2.33.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/eventbus/6.2.33/eventbus-6.2.33.jar",
        "sha1": "3fae69cfa9c5095bcc25c0a8a3ed9b26c156f922",
        "size": 64014
    },
    {
        "path": "net/minecraftforge/forgespi/7.0.1/forgespi-7.0.1.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/forgespi/7.0.1/forgespi-7.0.1.jar",
        "sha1": "3b4972a0cdb135853dba219be61a79b22cff1309",
        "size": 29831
    },
    {
        "path": "net/minecraftforge/coremods/5.2.4/coremods-5.2.4.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/coremods/5.2.4/coremods-5.2.4.jar",
        "sha1": "e30bab269d896613e38396274711410b3a0e4b87",
        "size": 31872
    },
    {
        "path": "cpw/mods/modlauncher/10.0.9/modlauncher-10.0.9.jar",
        "url": "https://maven.minecraftforge.net/cpw/mods/modlauncher/10.0.9/modlauncher-10.0.9.jar",
        "sha1": "06d9443f56f50bb85cea383686ff9c867391458b",
        "size": 130343
    },
    {
        "path": "net/minecraftforge/unsafe/0.2.0/unsafe-0.2.0.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/unsafe/0.2.0/unsafe-0.2.0.jar",
        "sha1": "54d7a0a5e8fdb71b973025caa46f341ae5904f39",
        "size": 2834
    },
    {
        "path": "net/minecraftforge/mergetool/1.1.5/mergetool-1.1.5-api.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/mergetool/1.1.5/mergetool-1.1.5-api.jar",
        "sha1": "f3da18e12c696d35a47c82cbb2cc8b5aa15e1154",
        "size": 2572
    },
    {
        "path": "com/electronwill/night-config/core/3.6.4/core-3.6.4.jar",
        "url": "https://maven.minecraftforge.net/com/electronwill/night-config/core/3.6.4/core-3.6.4.jar",
        "sha1": "510f174abbf1c947494db50ef2445683bd52c230",
        "size": 199834
    },
    {
        "path": "com/electronwill/night-config/toml/3.6.4/toml-3.6.4.jar",
        "url": "https://maven.minecraftforge.net/com/electronwill/night-config/toml/3.6.4/toml-3.6.4.jar",
        "sha1": "51d6cefb2b55ee55ee26b16391212fb2c7dfb4f4",
        "size": 31816
    },
    {
        "path": "org/apache/maven/maven-artifact/3.8.5/maven-artifact-3.8.5.jar",
        "url": "https://maven.minecraftforge.net/org/apache/maven/maven-artifact/3.8.5/maven-artifact-3.8.5.jar",
        "sha1": "4433f50c07debefaed0553bd0068f4f48d449313",
        "size": 58077
    },
    {
        "path": "net/jodah/typetools/0.6.3/typetools-0.6.3.jar",
        "url": "https://maven.minecraftforge.net/net/jodah/typetools/0.6.3/typetools-0.6.3.jar",
        "sha1": "a01aaa6ddaea9ec07ec4f209487b7a46a526283a",
        "size": 18281
    },
    {
        "path": "net/minecrell/terminalconsoleappender/1.2.0/terminalconsoleappender-1.2.0.jar",
        "url": "https://maven.minecraftforge.net/net/minecrell/terminalconsoleappender/1.2.0/terminalconsoleappender-1.2.0.jar",
        "sha1": "96d02cd3b384ff015a8fef4223bcb4ccf1717c95",
        "size": 15977
    },
    {
        "path": "org/jline/jline-reader/3.12.1/jline-reader-3.12.1.jar",
        "url": "https://maven.minecraftforge.net/org/jline/jline-reader/3.12.1/jline-reader-3.12.1.jar",
        "sha1": "4382ab1382c7b6f379377ed5f665dc2f6e1218bc",
        "size": 150765
    },
    {
        "path": "org/jline/jline-terminal/3.12.1/jline-terminal-3.12.1.jar",
        "url": "https://maven.minecraftforge.net/org/jline/jline-terminal/3.12.1/jline-terminal-3.12.1.jar",
        "sha1": "c777448314e050d980a6b697c140f3bfe9eb7416",
        "size": 211712
    },
    {
        "path": "org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar",
        "url": "https://maven.minecraftforge.net/org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar",
        "sha1": "9d1c0c3a304ae6697ecd477218fa61b850bf57fc",
        "size": 1089277
    },
    {
        "path": "org/openjdk/nashorn/nashorn-core/15.4/nashorn-core-15.4.jar",
        "url": "https://maven.minecraftforge.net/org/openjdk/nashorn/nashorn-core/15.4/nashorn-core-15.4.jar",
        "sha1": "f67f5ffaa5f5130cf6fb9b133da00c7df3b532a5",
        "size": 2167292
    },
    {
        "path": "net/minecraftforge/JarJarSelector/0.3.19/JarJarSelector-0.3.19.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/JarJarSelector/0.3.19/JarJarSelector-0.3.19.jar",
        "sha1": "376cc9c8ea60720cf027c01fc033de915699801c",
        "size": 17374
    },
    {
        "path": "net/minecraftforge/JarJarMetadata/0.3.19/JarJarMetadata-0.3.19.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/JarJarMetadata/0.3.19/JarJarMetadata-0.3.19.jar",
        "sha1": "0083feaa9b770e6ac0e96ee4fc23fa89325c5fe2",
        "size": 15895
    },
    {
        "path": "cpw/mods/bootstraplauncher/1.1.2/bootstraplauncher-1.1.2.jar",
        "url": "https://maven.minecraftforge.net/cpw/mods/bootstraplauncher/1.1.2/bootstraplauncher-1.1.2.jar",
        "sha1": "0c546e00443d8432cda6baa1c860346980742628",
        "size": 8284
    },
    {
        "path": "net/minecraftforge/JarJarFileSystems/0.3.19/JarJarFileSystems-0.3.19.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/JarJarFileSystems/0.3.19/JarJarFileSystems-0.3.19.jar",
        "sha1": "2464eb7d6b9ddb9db36a82cf8a95193e5c6fe020",
        "size": 32195
    },
    {
        "path": "net/minecraftforge/fmlloader/1.20.1-47.4.20/fmlloader-1.20.1-47.4.20.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/fmlloader/1.20.1-47.4.20/fmlloader-1.20.1-47.4.20.jar",
        "sha1": "8798bdd148d476c7ec54d8156f88de5e243c2dfb",
        "size": 270672
    },
    {
        "path": "net/minecraftforge/fmlearlydisplay/1.20.1-47.4.20/fmlearlydisplay-1.20.1-47.4.20.jar",
        "url": "https://maven.minecraftforge.net/net/minecraftforge/fmlearlydisplay/1.20.1-47.4.20/fmlearlydisplay-1.20.1-47.4.20.jar",
        "sha1": "4dcdfb740aff35b40a3471708ca8a5f1e22a9504",
        "size": 170513
    },
]

def sha1_file(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def download(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    with open(dest, 'wb') as f:
        f.write(data)

print("=== Verification et installation des librairies Forge ===")
print(f"Dossier: {lib_dir}\n")

ok = 0
fixed = 0
failed = 0

for lib in libs:
    dest = os.path.join(lib_dir, lib['path'].replace('/', os.sep))
    name = os.path.basename(dest)

    need_download = False

    if not os.path.exists(dest):
        print(f"[MANQUANT] {name}", end='', flush=True)
        need_download = True
    else:
        actual_sha1 = sha1_file(dest)
        if actual_sha1 != lib['sha1']:
            actual_size = os.path.getsize(dest)
            print(f"[CORROMPU] {name} (taille={actual_size}, SHA1={actual_sha1[:8]}...)", end='', flush=True)
            need_download = True
        else:
            print(f"[OK] {name}")
            ok += 1

    if need_download:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            download(lib['url'], dest)
            actual_sha1 = sha1_file(dest)
            if actual_sha1 == lib['sha1']:
                print(f" -> Telecharge OK!")
                fixed += 1
            else:
                print(f" -> ERREUR SHA1! Attendu={lib['sha1'][:8]}, Recu={actual_sha1[:8]}")
                failed += 1
        except Exception as e:
            print(f" -> ERREUR: {e}")
            failed += 1

print(f"\n=== Termine ===")
print(f"Corrects: {ok} | Corriges: {fixed} | Echecs: {failed}")

if failed == 0:
    print("\nToutes les librairies sont OK! Lance le launcher.")
else:
    print(f"\nATTENTION: {failed} fichier(s) en echec. Envoie ce resultat pour aide.")
