# StarLine — Level Design Guidelines
> For Level Designers · Neon Monk · March 2026

---

## The Game in One Sentence

**"The sky faded because people stopped looking up."** Players restore the universe by connecting stars into constellations. Lumen, the last light, guides them.

---

## Core Mechanic: Free Connection Model

This is the single most important rule. Everything flows from this.

**Any star can connect to any star.** There are no adjacency constraints. Wrong moves are allowed and stay visible. The player's goal is to recreate exactly the target edges — no more, no less.

**Win condition:** Player's drawn edges = target edges, with zero extra edges.

This means players create their own traps through wrong assumptions about the constellation shape. The silhouette draws them in; completing the correct edge set is the satisfaction.

This is NOT a Hamiltonian path game. Don't think about "paths." Think about **which edges define the shape** and which edges players will **incorrectly assume** are part of it.

---

## Design Philosophy

### Shape = Motivation, Solve = Satisfaction

1. The constellation **silhouette** is shown as a faint preview — this hooks the player
2. The **puzzle** is figuring out which connections form that shape
3. **Wrong assumptions** create discovery moments
4. **Completion** triggers a celebration — the constellation comes alive

### The Squint Test

If you squint at the connected dots, you should immediately recognize the object. If not, redesign.

### Tell Everything, Then Remove

Hybrid-casual players need maximum clarity upfront. The shape should be obvious. The challenge is the edges, not figuring out what you're making.

---

## Difficulty Scaling

| Factor | Easy | Medium | Hard |
|--------|------|--------|------|
| Star count | 4–6 | 7–10 | 11–16 |
| Trap complexity | 1 obvious trap | 2–3 traps, layered | Multiple interacting traps |
| Target edges | 3–5 | 6–10 | 10–18 |
| Target solve time | 15–25s | 25–45s | 45–90s |

**Target win rate: 70-80% on first attempt.**

### Difficulty Wave Pattern

Within each chapter, levels follow a wave:

```
Easy → Medium → Hard → Easy (relief) → Medium → Hard
```

**Never** put two hard levels in a row. **Never** introduce a new concept in a hard level.

---

## Trap Taxonomy

Every level must have at least one trap. These are what make StarLine special.

| Trap | Description | Best For |
|------|-------------|----------|
| **Core Lockout** | Completing outer ring blocks center access | Circular/ring shapes |
| **Spiral Dead-end** | Following obvious spiral leads to isolated star | Spiral/nautilus shapes |
| **Choke Point** | Critical node connecting subgraphs — timing matters | Complex multi-part shapes |
| **Ring Completion** | Completing a ring feels good but leaves nodes unreachable | Layered shapes |
| **Wrong Start** | Most prominent star is the wrong starting point | Animals (nose/head traps) |
| **Edge Sharing** | Two close stars look like they should connect, but don't | Dense star clusters |
| **Ray Skipping** | Skipping a radial arm seems fine but creates dead end | Star/radial shapes |
| **Wave Isolation** | Staying on one curve leaves parallel curve unvisited | Wave/helix patterns |
| **Base-first** | Building foundation blocks upper structure | Vertical shapes (trees, towers) |
| **Center Timing** | Visiting center too early/late splits graph | Symmetric shapes |

---

## Narrative Tiers

Tag every level with one tier:

- **Ambient** (majority): Beautiful shapes, standard completion. Most levels.
- **Discovery** (chapter-defining): First of a type, special text. 2–3 per chapter.
- **Revelation** (rare peaks): Emotional, hardest puzzles. 1 per chapter max.

---

## Chapter Structure (~50 levels total)

| Ch | Name | Levels | Theme | Status |
|----|------|--------|-------|--------|
| 1 | First Light | 5 | Tutorial — basic shapes, teaching the mechanic | In Progress |
| 2 | Creature Sky | 10–12 | Animals — instant recognition, strongest D1-D3 | Designing |
| 3 | World Around Us | 10–12 | Nature & objects — trees, mountains, tools | Planned |
| 4 | Myth & Legend | 10–12 | Mythical creatures, cultural symbols | Planned |
| 5 | Cosmos | 8–10 | Zodiac, galaxies, abstract celestial | Planned |

Plus: 3 locked teaser levels + Celestial Boutique shop.

**Regional content:** 1–2 regional objects per UA market sprinkled into chapters. Philippines soft launch → include Tarsier, Sampaguita, or Jeepney.

---

## What Makes a Good Constellation

### Star Placement Rules

- Stars go at **structural points** — joints, tips, corners, extremities
- NOT evenly distributed along the outline
- An animal: head, tail tip, leg joints, wing tips, dorsal fin
- An object: corners, key features, handles, points

### Edge Economy

Use the **minimum edges** needed for shape recognition. Extra edges that don't improve readability become confusion (bad), not design traps (good).

### Natural Trap Integration

The shape should naturally create at least one "obvious wrong connection" — two stars that look like they should connect but that edge isn't in the target.

### Example

**Good dolphin:** Stars at nose, eye, dorsal fin, tail tip, belly curve (6 stars). The tail-to-nose edge looks obvious but isn't target → natural trap.

**Bad dolphin:** 12 stars evenly spaced along outline. No natural traps, no structural clarity, boring.

---

## Level Design Workflow

1. **Find reference** — simple silhouette image of the object/animal
2. **Open StarLine Designer** — upload reference as overlay
3. **Place stars** at structural points over the reference
4. **Draw target edges** — the connections that form the recognizable shape
5. **Name the level** and set the trap type
6. **Play-test** in the Designer's built-in test mode
7. **Export "Claude format"** → paste into Claude for validation
8. **Share** via GitHub PR or shared doc

**Target: ~20 minutes per level** once you're practiced.

---

## Export & Coordinate System

The Designer exports normalized coordinates (0–1 range).

**Y-axis note:** Designer uses canvas coords (y=0 at top). Unity uses y=0 at bottom. Integration handles the flip automatically — don't worry about it in the Designer.

**Export formats:**
- **Claude format** — paste into Claude for analysis
- **Unity C#** — ready-to-paste pattern code
- **JSON** — structured data

---

## Fun Facts (Completion Screen)

Every level shows a one-line fun fact on completion. Rules:

- **One-breath read** — must be readable in a single breath
- Surprising or delightful, not educational/dry
- Relates to the actual constellation/object
- Example: "Dolphins sleep with one eye open — half their brain stays awake."

---

## Anti-Patterns (Things to Avoid)

- Two hard levels in a row
- Levels where the shape isn't recognizable
- Trap-less levels (every level needs at least one trap)
- More than 16 stars (phone screen gets crowded)
- Edges that players can't distinguish at phone scale
- Requiring perfect play — there should always be room for mistakes and recovery
- Subtle traps that most players won't even notice

---

## Working with Claude

Create a Claude Project called "StarLine Level Design" and upload this document as knowledge.

**Useful prompts:**

```
Validate my level: [paste Claude format export]
— Analyze trap, difficulty, solution paths

Design a constellation for [OBJECT] with [N] stars, 
difficulty [easy/medium/hard], using [TRAP TYPE] trap.

Review my chapter difficulty curve: [list levels with star counts and traps]
```

Claude can validate graph theory, suggest traps, write fun facts, and convert between formats.

---

*✦ Neon Monk · "The sky faded because people stopped looking up."*
