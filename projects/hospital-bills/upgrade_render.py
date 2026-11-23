import os

p = r"C:\Users\Lenovo\.claude\skills\stickman-hybrid\scripts\render.py"
content = open(p, "r", encoding="utf-8").read()

target = """        sc = scenes[si]
        prog = [min(1.0, max(0.0, (t - o["t"]) / 0.4)) for o in sc["ov"]]
        counting = any((o["img"] == "count" and 0 < t - o["t"] < 0.95) or
                       (o.get("cross") and 0.25 < t - o["t"] < 0.65) for o in sc["ov"])
        key = (si, tuple(round(p, 3) for p in prog), round(t, 3) if counting else 0)
        if key != last_key:
            fr = base(sc).copy()"""

replacement = """        sc = scenes[si]
        extra_spec = sc["row"][4].strip() if len(sc["row"]) > 4 else ""
        has_zoom = any(x in extra_spec for x in ("zoom:in", "zoom:out", "zoom:slow"))
        scale = 1.0
        if has_zoom:
            dur = max(0.1, sc["t1"] - sc["t0"])
            u = min(1.0, max(0.0, (t - sc["t0"]) / dur))
            if "zoom:in" in extra_spec:
                scale = 1.0 + 0.08 * u
            elif "zoom:out" in extra_spec:
                scale = 1.08 - 0.08 * u
            elif "zoom:slow" in extra_spec:
                scale = 1.0 + 0.05 * u
        prog = [min(1.0, max(0.0, (t - o["t"]) / 0.4)) for o in sc["ov"]]
        counting = any((o["img"] == "count" and 0 < t - o["t"] < 0.95) or
                       (o.get("cross") and 0.25 < t - o["t"] < 0.65) for o in sc["ov"])
        key = (si, tuple(round(p, 3) for p in prog), round(t, 2) if (counting or has_zoom) else 0)
        if key != last_key:
            fr = base(sc).copy()
            if has_zoom and scale != 1.0:
                cw, ch = int(W / scale), int(H / scale)
                x0, y0 = (W - cw) // 2, (H - ch) // 2
                fr = fr.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)"""

content_norm = content.replace("\r\n", "\n")
target_norm = target.replace("\r\n", "\n")
replacement_norm = replacement.replace("\r\n", "\n")

if target_norm in content_norm:
    new_content = content_norm.replace(target_norm, replacement_norm)
    open(p, "w", encoding="utf-8").write(new_content)
    print("SUCCESS: render.py upgraded with camera zoom engine!")
else:
    print("ERROR: Target block not found in render.py")
