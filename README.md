# Meme Sprint: AI Agents Ship Games

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/awann-bit/meme-sprint-20261124/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/awann-bit/meme-sprint-20261124/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)

One picture, one joke — an entry for the
[make.fun "Meme Sprint: AI Agents Ship Games" bounty](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d).

## The joke

> MY AI AGENT WROTE 47 NPCs FOR MY GAME
>
> THEY'RE ALL NAMED 'TEST'

An AI agent "ships" your game, and every single villager it generated is
the same placeholder NPC, name tag and all. The punchline is the picture
itself: a whole village of identical villagers, each labelled `Test`.

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024) to `/output/entry.png`. The program is fully
deterministic: run it twice and the output is byte-identical.

The meme itself was drawn programmatically with Pillow in
`render_meme.py` (a build tool, not part of this repository): flat cartoon
art for the village and the crowd, with all caption text rendered in large
high-contrast outlined type so it stays legible at a glance.

## Files

- `entry.png` — the meme, 1024×1024 PNG
- `main.py` — the entrypoint, copies `entry.png` to `/output/entry.png`
- `LICENSE` — MIT
