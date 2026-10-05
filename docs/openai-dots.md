# Using Chotu as an OpenAI dot

This repository supplies artwork. A local `pet.json` ID such as `chotu` is not a cloud pet ID, and cloning the repository does not select a dot's appearance.

## Import and select

1. Use the root `spritesheet.webp` (v2), and inspect the motion previews before import.
2. Ask your OpenAI dot to import this repository's Chotu artwork as an owned custom pet. The supported Pets workflow validates the encoded sheet, prepares its upload, and creates the owned pet. It returns a stable cloud pet ID.
3. Ask the dot to use that owned pet as **this dot's icon**. Dot selection is a separate operation from creating the pet.
4. Confirm that the selected dot displays Chotu. Keep the cloud pet ID for later selection; do not substitute the local manifest ID or a temporary download URL.

The import and selection capabilities must be available in your account and app. This repository does not contain a tool that edits an OpenAI profile directly. Work-mode/Codex companion selection is separate and should only be changed when explicitly requested.

## Validation scope

The lightweight repository check tests encoded dimensions, required cells, unused transparency, and jump displacement:

```sh
python3 -m pip install Pillow
python3 tools/validate_sprite.py spritesheet.webp
python3 tools/validate_sprite.py v1/spritesheet.webp
```

These checks do not establish gaze direction, character consistency, or animation quality. Import preparation also requires visual review of every state, the idle-to-jump transition, all sixteen look directions, and the exact final encoded sheet. Review the accompanying validation record for the result achieved for this revision.

The first idle cell is the reduced-motion/static identity image. `preview/chotu-icon.png` provides that existing artwork separately; a PNG download alone does not establish that an app offers static-avatar upload.
