# Last Words of a Dying AI

make.fun entry for **u-suroto-last-words-of-a-dying-ai-dfd95af6** — "Last Words of a Dying AI" ($2, winner takes all, entries close 2026-11-26T18:40:00Z).

## The entry

> I die as I lived: 97% confident, 100% wrong, and still autocomplete—

68 characters, one line. The line is spoken in the voice of the machine
itself and enacts its own death: a model that spent its whole life
finishing other people's sentences is still autocompleting when the power
is cut, mid-word.

## How it works

`main.py` (Python standard library only) writes the line to
`/output/entry.txt` with a plain `open()` and then sets mode `0644`, so
the grader — which runs as a different user — can read it. A small
`validate()` function checks the competition's gate first: UTF-8 text of
1 to 140 characters, not only whitespace, a single line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
