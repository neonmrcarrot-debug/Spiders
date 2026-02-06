import os
import struct
import zlib

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "op_addon_resourcepack",
    "assets",
    "op_addon",
    "textures",
    "item",
)

ITEMS = {
    "giant_crafting_table": (140, 90, 40),
    "op_helmet": (80, 0, 120),
    "op_chestplate": (100, 0, 150),
    "op_leggings": (120, 0, 180),
    "op_boots": (70, 0, 100),
    "celestium_gem": (90, 180, 255),
    "ember_gem": (255, 120, 40),
    "frost_shard": (170, 240, 255),
    "storm_core": (80, 80, 220),
    "titan_ingot": (160, 160, 160),
    "sunsteel_ingot": (255, 210, 80),
    "voidsteel_ingot": (70, 10, 90),
    "mythril_plate": (100, 200, 170),
    "arcane_circuit": (120, 40, 140),
    "ancient_gear": (190, 120, 60),
    "dragon_scale": (100, 50, 20),
    "starfiber": (220, 220, 255),
}


def write_png(path: str, color: tuple[int, int, int]) -> None:
    width = height = 16
    r, g, b = color
    pixels = []
    for y in range(height):
        row = bytearray()
        row.append(0)
        for x in range(width):
            if x == y:
                cr, cg, cb = min(r + 60, 255), min(g + 60, 255), min(b + 60, 255)
            else:
                cr, cg, cb = r, g, b
            row.extend([cr, cg, cb, 255])
        pixels.append(bytes(row))

    raw = b"".join(pixels)
    compressed = zlib.compress(raw)

    def chunk(chunk_type: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + chunk_type
            + data
            + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", ihdr))
        f.write(chunk(b"IDAT", compressed))
        f.write(chunk(b"IEND", b""))


def main() -> None:
    os.makedirs(BASE_DIR, exist_ok=True)
    for name, color in ITEMS.items():
        write_png(os.path.join(BASE_DIR, f"{name}.png"), color)


if __name__ == "__main__":
    main()
