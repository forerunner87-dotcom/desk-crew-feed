"""Push every new status.json entry to James's phone via ntfy."""
import json, os, subprocess, urllib.request

TOPIC = os.environ["NTFY_TOPIC"]
NAMES = {"chauncey": "Chauncey", "gary": "Gary", "bernard": "Bernard"}
TAGS = {"chauncey": "clipboard", "gary": "mag", "bernard": "iphone"}

def load(ref):
    try:
        raw = subprocess.run(["git", "show", f"{ref}:status.json"], capture_output=True, text=True, check=True).stdout
        return json.loads(raw).get("updates", [])
    except Exception:
        return []

before = os.environ.get("BEFORE", "")
old = load(before) if before and set(before) != {"0"} else []
new = load("HEAD")
last = max((u.get("at", "") for u in old), default="")
fresh = [u for u in new if u.get("at", "") > last and u.get("who") in NAMES][-5:]
for u in fresh:
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=u["text"][:200].encode(),
        headers={"Title": f"{NAMES[u['who']]} (Desk Crew)", "Tags": TAGS[u["who"]]},
        method="POST",
    )
    urllib.request.urlopen(req, timeout=15).read()
    print("sent:", u["who"], u["text"])
print(f"{len(fresh)} notification(s)")
