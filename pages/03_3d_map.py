import os
import solara
import leafmap.maplibregl as leafmap

MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "")

def create_3d_map():
    if not MAPTILER_KEY:
        # 沒 key — 顯示一般底圖
        m = leafmap.Map(
            center=[121.0, 23.7],
            zoom=8,
            style="OpenStreetMap",
            pitch=45,
            bearing=15,
        )
        m.layout.height = "700px"
        return m

    # 有 key — 使用 MapTiler 的 3D 地形
    style_url = f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"

    m = leafmap.Map(
        style=style_url,
        center=[121.0, 23.7],
        zoom=10,
        pitch=45,
        bearing=15,
    )
    m.layout.height = "700px"
    return m

@solara.component
def Page():
    map_object = solara.use_memo(create_3d_map, dependencies=[MAPTILER_KEY])

    with solara.Column():
        if not MAPTILER_KEY:
            solara.Warning("MapTiler API Key 未設定，目前顯示一般 3D 底圖。")

        solara.Markdown("## 我的 3D 主題地形地圖")

        solara.display(map_object.to_solara())
