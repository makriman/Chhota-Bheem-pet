# Validation record — 2026-10-05

The exact v2 WebP SHA256 is `3390a7b481c3feea87ed94a67d09393cf62621d0be47852c83a6c58d7605af14` (1,505,180 bytes).

- Bundled atlas, frame, chroma, and pet-quality checks passed.
- Pets cloud preflight returned `valid: true`, 1536×2288, sprite version 2, with no errors.
- Independent visual review of ordered decoded frames passed: head scale is consistent, jump lift is 20 px at alpha >16 (19 px including faint edge pixels), and landing returns to idle.
- Isolated blind reviewers agreed on all four cardinal look directions. Some intermediate diagonal poses are similar; 112.5° has subtle downward pitch. These reviewed warnings are recorded in the semantic and continuity reports.
- The blind review preceded the final jump-only repair. `look-row-byte-equivalence.json` proves the sixteen look cells are unchanged in the final WebP.
- v1 is a pixel-identical crop of the first nine v2 rows, encoded losslessly. Both repository geometry checks passed, with no hidden RGB in fully transparent pixels.

Previews are rendered from the encoded sheet. Review covered contact sheets and ordered frames; live runtime animation and dot selection must be verified in the target app. The repository scripts provide geometry checks and previews, not substitutes for semantic review or the cloud import validation.
