# ZScan NFT registry

The list of Zcash NFT collections shown on [ZScan](https://zscan.cash/collections): names, descriptions, logos and official links, each backed by public sources.

ZScan reads the collections themselves from the Zcash chain: items, owners, transfers and sales. This registry adds what the chain doesn't say, such as a collection's name, its website, or which launchpad mints belong together. Changes merged here show up on ZScan within about ten minutes.

## Add or correct a collection

- **Easiest:** [open an issue](../../issues/new?template=collection.yml) with the form. We'll check it and add it.
- **Pull request:** edit `collections.json`, one collection per pull request. CI checks the format.

Every entry needs **public sources** confirming its facts, such as an announcement, the deploy inscription or a marketplace page. Descriptions stay factual. We don't list price predictions or marketing claims, and we don't list collections whose items can't be tied to Zcash.

## Fields

| Field | Required | Notes |
|---|---|---|
| `slug` | yes | URL key on ZScan: lowercase letters, digits, dashes. |
| `name` | yes | |
| `description` | yes | One or two factual sentences. |
| `kind` | yes | `inscription`: the items are Zcash inscriptions. `marketplace`: the items exist only in a marketplace's own records, and ZScan shows the marketplace's figures and labels them as such. |
| `onchain` | for `inscription` | `zrc721`: the collection's ZRC-721 name (uppercase, as in its deploy inscription). `drop`: for launchpad mints without an on-chain collection name, the transparent address that every mint's commit transaction paid (usually the creator). |
| `website`, `x`, `discord`, `telegram` | no | HTTPS links. |
| `logo` | no | Square image, `https://` or `ipfs://`. |
| `supply`, `minted_at` (YYYY-MM-DD), `mint_price_zec` | no | As announced. |
| `market` | no | A marketplace with an API ZScan supports (`zemon`, `zilkroad`, `zeccat`, `zecpad`), for floor, listings and volume. |
| `marketplaces` | no | Other places it trades: `{ "label", "url" }`. |
| `confidence` | yes | `verified`: the sources tie the name to the items. `likely`: they strongly suggest it. |
| `sources` | yes | `{ "label", "url" }`, at least one. |

Check a change locally:

```bash
pip install jsonschema
python scripts/validate.py
```

## License

The data is dedicated to the public domain under [CC0 1.0](LICENSE): anyone can reuse it.
