#!/usr/bin/env python3
"""Checks collections.json: the JSON schema plus rules a schema can't express."""
import json
import sys

from jsonschema import Draft202012Validator

registry = json.load(open("collections.json"))
schema = json.load(open("schema.json"))
errors = [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in Draft202012Validator(schema).iter_errors(registry)]

seen, zrc721, drops = set(), set(), set()
for c in registry.get("collections", []):
    slug = c.get("slug", "?")
    if slug in seen:
        errors.append(f"{slug}: duplicate slug")
    seen.add(slug)
    onchain = c.get("onchain") or {}
    if onchain and c.get("kind") != "inscription":
        errors.append(f"{slug}: only inscription collections can link to the chain")
    if c.get("kind") == "inscription" and not onchain:
        errors.append(f"{slug}: an inscription collection needs onchain.zrc721 or onchain.drop")
    for key, pool in (("zrc721", zrc721), ("drop", drops)):
        if key in onchain:
            if onchain[key] in pool:
                errors.append(f"{slug}: onchain.{key} {onchain[key]} is already claimed")
            pool.add(onchain[key])
    if c.get("kind") == "marketplace" and not c.get("market"):
        errors.append(f"{slug}: a marketplace collection needs a supported market")

for e in errors:
    print("error:", e)
if errors:
    sys.exit(1)
print(f"ok: {len(registry['collections'])} collections")
