# pages/03_3d_map.py
import solara
import leafmap.maplibregl as leafmap

def create_3d_map():
    # 不使用 API Key 的簡單 3D 地圖（類似 PDF 裡的 fallback 寫法）
    m = leafmap.Map(
        center=[121.0, 23.7],
        zoom=7,
        style="OpenStreetMap",  # 不需金鑰的樣式
        pitch=60,               # 俯仰角
        bearing=15              # 旋轉角度
    )
    # 高度設定（控制 widget 高度）
    m.layout.height = "650px"

    # 未來如果要 DEM / 3D 地形，可加 add_terrain / add_deckgl_layer
    return m

@solara.component
def Page():
    solara.Title("3D 地形故事地圖")

    map_obj = solara.use_memo(create_3d_map, dependencies=[])

    with solara.Column():
        solara.Markdown("## 故事章節：3D 視角")
        solara.Markdown(
            """
這一頁可以用來：
- 從 3D 視角觀察地形與空間分布
- 搭配高度、坡度、視線等分析結果
            """
        )

        with solara.Column(style={"width": "100%", "height": "700px"}):
            solara.display(map_obj)
