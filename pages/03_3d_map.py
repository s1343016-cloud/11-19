import os
import solara
import leafmap.maplibregl as leafmap

MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "")

# 堰塞湖中心位置
MATAIAN_DAM = [23.6995, 121.2955]


def create_3d_map():
    if MAPTILER_KEY:
        style_url = (
            f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"
        )
        m = leafmap.Map(
            style=style_url,
            center=MATAIAN_DAM,
            zoom=12,
            pitch=60,   # 仰角
            bearing=25,  # 水平旋轉角
        )
    else:
        # 沒有 key 時的備用：普通 2D 地圖
        m = leafmap.Map(center=MATAIAN_DAM, zoom=11)

    m.layout.height = "700px"

    m.add_marker(
        MATAIAN_DAM,
        popup="""
馬太鞍溪堰塞湖位置（3D 地形視角）
- 可觀察到上游集水區、崩塌地與堰塞湖所在谷地
""",
    )

    return m


@solara.component
def Page():
    m = solara.use_memo(create_3d_map, dependencies=[MAPTILER_KEY])

    with solara.Column(
        gap="1rem",
        style={"maxWidth": "1100px", "margin": "0 auto"},
    ):
        solara.Markdown("## 馬太鞍溪堰塞湖的 3D 地形視覺化")

        if not MAPTILER_KEY:
            solara.Warning(
                "尚未在 Hugging Face Space 的 Settings → Variables 中設定 "
                "MAPTILER_API_KEY，目前僅顯示備用 2D 地圖。"
            )

        solara.Markdown(
            """
### 為何需要 3D 地形圖？

- 了解崩塌與堰塞湖位置：  
  堰塞湖位於深切谷地上游，大規模山崩沿陡峭山坡滑落至溪谷，
  堆積形成天然壩體，3D 地形有助於看出崩塌來源區與堆積區高差。

- 評估潰決可能路徑：  
  從 3D 視角可以觀察到下游河谷收斂與開展的變化，
  有助於推估洪峰能量在峽谷與平原段的不同表現。  

- 教學與溝通：  
  對於非專業者，平面地圖較難理解地形起伏，
  3D 視覺化可以更直覺地呈現「高山崩塌—谷地壩體—下游平原」的關係，
  有助於防災教育與風險溝通。
"""
        )

        solara.display(m.to_solara())
