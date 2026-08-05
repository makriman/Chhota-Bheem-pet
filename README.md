# Chhota Bheem Pet — Chotu 🥟💪

A pixel-art desktop companion pet, inspired by **Chhota Bheem**, built for AI coding CLIs that support
the open "pet-pack" format (`pet.json` + a sprite atlas). Chotu sits on your screen, idles while you
think, and reacts while your agent works.

Made primarily as a **Codex pet**, with instructions below for using the exact same package on
**Claude Code**, **Cursor**, and other agent CLIs via compatible companion apps.

## Table of contents

- [Meet Chotu](#meet-chotu)
- [About Chhota Bheem](#about-chhota-bheem)
- [What's in this repo](#whats-in-this-repo)
- [Use it with Codex (native)](#use-it-with-codex-native)
- [Use it with Claude Code](#use-it-with-claude-code)
- [Use it with Cursor, Windsurf & other agents](#use-it-with-cursor-windsurf--other-agents)
- [Pet package format](#pet-package-format)
- [Disclaimer & credits](#disclaimer--credits)
- [License](#license)

## Meet Chotu

| | |
|---|---|
| **Name** | Chotu |
| **Vibe** | A cheerful, brave young hero who keeps you company while you work |
| **Sprite version** | v2 (11-row atlas — 9 animation states + 16 look directions) |
| **Format** | `pet.json` + `spritesheet.webp`, transparent background, 1536×2288px |

Chotu idles quietly in the corner of your screen, perks up when your agent starts running, and
celebrates when a task finishes — the same "ambient status" idea Codex pioneered, just wearing a
different face.

## About Chhota Bheem

Chotu's look and spirit are inspired by **Chhota Bheem**, one of India's most iconic animated
characters. Created by **Green Gold Animation**, *Chhota Bheem* first aired in 2008 and has since
become a cornerstone of Indian children's television — following Bheem, an unusually strong and
endlessly brave young boy, and his friends in the fictional kingdom of **Dholakpur**. Over the
years the franchise has grown into dozens of TV seasons, feature films, and spin-offs, all built
around the same core values: courage, loyalty, and looking out for your friends (usually solved
with a well-timed **laddoo** for extra strength).

If you want a taste of the character, here's a classic clip:
[Chhota Bheem — YouTube](https://www.youtube.com/watch?v=5TN_9xCrWFA)

This project borrows that same "small hero, big heart" energy for a companion that roots for you
while you code — nothing more. See [Disclaimer & credits](#disclaimer--credits) below.

## What's in this repo

```text
.
├── pet.json          # Pet manifest (id, display name, sprite version, sprite path)
├── spritesheet.webp  # 1536x2288 sprite atlas, 8x11 grid, transparent background
└── README.md         # You are here
```

This is a **local custom pet package** in the open pet-pack format — no build step, no
dependencies. Point a compatible pet app at this folder (or copy it into that app's pets
directory) and it just works.

## Use it with Codex (native)

Codex has built-in pet support. Drop this folder under your Codex pets directory:

```bash
git clone https://github.com/makriman/Chhota-Bheem-pet.git "${CODEX_HOME:-$HOME/.codex}/pets/chhota-bheem"
```

Then open the pet switcher in Codex and select **Chotu**. That's it — no restart, no extra config.

## Use it with Claude Code

Claude Code has no built-in pet feature, but two community apps read the same pet-pack format
Codex uses, so this package works there unmodified.

### Option A — AgentPet (recommended, macOS/Windows/Linux)

[AgentPet](https://github.com/ntd4996/agentpet) is a native desktop-pet + agent monitor that
supports Claude Code, Codex, Cursor, and more, and explicitly uses this same pet-pack format.

```bash
# macOS (Homebrew)
brew install --cask ntd4996/tap/agentpet

# or download the signed .dmg / Windows installer / Linux AppImage from:
# https://github.com/ntd4996/agentpet/releases/latest
```

1. Launch AgentPet, then go to **Settings → General** and click **Install** next to Claude Code.
2. Clone this repo into AgentPet's local pets folder:
   ```bash
   git clone https://github.com/makriman/Chhota-Bheem-pet.git ~/.agentpet/pets/chhota-bheem
   ```
3. Open **Settings → Pet**, select **Chotu**, and it will appear on screen and react to Claude
   Code's running / waiting-for-input / done states.

### Option B — Claude Pet Companion (Windows only)

[Claude Pet Companion](https://github.com/zzp1221/claude-code-pet) is a Windows-only Tauri app
built specifically for Claude Code, with `/pet` slash-command integration and Codex-pet auto-sync.

1. Install it from the [latest release](https://github.com/zzp1221/claude-code-pet/releases/latest).
2. Import this pet folder via the app's **Import Pet Folder** option, or just clone it into
   `~/.codex/pets/` first — Claude Pet Companion auto-scans and syncs Codex pets from there.

## Use it with Cursor, Windsurf & other agents

AgentPet (above) also supports **Cursor, Windsurf, Antigravity, GitHub Copilot, Kiro CLI, Pi**,
and any other CLI agent via a universal wrapper (`agentpet run -- <command>`). The same
`~/.agentpet/pets/chhota-bheem` install from the Claude Code section covers these too — just
enable the relevant integration under **Settings → General** in AgentPet. Note that non-Claude/
Codex agents currently only report **working / done**, not the finer-grained
**waiting-for-input** state.

## Pet package format

`pet.json` describes the manifest:

```json
{
  "id": "chotu",
  "displayName": "Chotu",
  "description": "A cheerful, brave young hero who keeps you company while you work.",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

The spritesheet is an 8-column × 11-row grid of 192×208px cells on a transparent background:

- **Rows 0–8** — standard animation states (idle, running, waiting, failed, review, jumping,
  waving, and two extra slots), 8 frames each.
- **Rows 9–10** — 16 look directions in 22.5° steps, clockwise from "up" (row 9 = 0°–157.5°, row
  10 = 180°–337.5°). The front-facing "neutral" direction has no dedicated cell and falls back to
  idle.

Want to make your own variant? Fork this repo, swap in your own `spritesheet.webp` (same
1536×2288px / 8×11 layout), update `pet.json`, and it's compatible everywhere this one is.

## Disclaimer & credits

This is an **unofficial, fan-made** companion pet inspired by the *Chhota Bheem* character and
franchise. **Chhota Bheem** and all related characters, names, and imagery are trademarks and
copyrighted works of **Green Gold Animation Pvt. Ltd.** This project is not affiliated with,
endorsed by, or sponsored by Green Gold Animation, and no official show assets are redistributed
here. If you hold rights to this character and have concerns about this project, please open an
issue and it will be addressed promptly.

Thanks to the **Codex** team for the original pet-pack contract this format is built on, and to
the **AgentPet** and **Claude Pet Companion** projects for bringing pet support to other agent
CLIs.

## License

Application/format usage is free to reuse. The `spritesheet.webp` artwork in this repo is an
original fan creation and is shared here for personal, non-commercial use alongside compatible
pet apps. See the disclaimer above regarding the underlying character inspiration.
