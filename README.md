# OP Armor + Giant Crafting Table (Minecraft Java 1.20.1)

This repository contains a **data pack** and **resource pack** that add:

- **OP Armor** (helmet, chestplate, leggings, boots) with powerful stats.
- A **Giant Crafting Table** item used to craft a large collection of custom items.
- **12 custom items** with unique textures.

## Install

1. Run `python scripts/generate_textures.py` to generate the PNG textures.
   - Keep the `scripts` folder next to the packs in this repo; you do **not** copy it into Minecraft.
2. Copy `op_addon_datapack` into your world’s `datapacks` folder.
3. Copy `op_addon_resourcepack` into your Minecraft `resourcepacks` folder.
4. Enable the resource pack in Minecraft.
5. Run `/reload` in your world.

### Windows folder paths

- **Datapack folder (per world):**  
  `%AppData%\\.minecraft\\saves\\<YourWorld>\\datapacks`
- **Resource pack folder (global):**  
  `%AppData%\\.minecraft\\resourcepacks`

### Troubleshooting

- If the **Giant Crafting Table** texture is purple/black or missing, run the texture generator again and re-copy the resource pack. The PNGs are not shipped in the repo and must be generated locally. 
- If you see `<<<<<<<`, `=======`, `>>>>>>>` in `README.md`, you have a **merge conflict**. Remove the conflict markers and keep the Windows paths + troubleshooting text, then save the file.

## Recipes

### Giant Crafting Table
Craft in a normal crafting table:

```
N N N
N C N
N N N
```
- `N` = Netherite Ingot
- `C` = Crafting Table

### OP Armor
Each piece uses a **Giant Crafting Table** in the center, netherite armor in the middle row, and custom materials around it.

### Custom Items
Each custom item uses a **Giant Crafting Table** plus themed vanilla ingredients and returns a **large stack** (64) of the custom item.

## Notes

- The Giant Crafting Table is consumed in recipes.
- The OP armor uses built-in netherite armor visuals (custom item icons are provided in the inventory).
- All custom items are identified via `CustomModelData` and custom names/lore.
