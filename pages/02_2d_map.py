import os
import solara
import leafmap.maplibregl as leafmap

# MapTiler API key 從 HF 的變數 MAPTILER_API_KEY 讀取
MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "")

# 主要位置座標（WGS84）
# 堰塞湖：23.6995°N, 121.2955°E（維基百科座標）
MATAIAN_DAM = [23.6995, 121.2955]
# 光復鄉市區：約 23.67°N, 121.42°E（以公開地理資料估計）
GUANGFU_TOWN = [23.669, 121.422]


def create_map():
    if MAPTILER_KEY:
        style_url = f"https://api.maptiler.com/maps/streets-v2/style.json?key={MAPTILER_KEY}"
        m = leafmap.Map(
            style=style_url,
            center=[23.685, 121.36],
            zoom=11,
        )
    else:
        # 備用：如果沒有 key，就用預設樣式
        m = leafmap.Map(center=[23.685, 121.36], zoom=11)

    m.layout.height = "600px"

    # 堰塞湖位置
    m.add_marker(
        MATAIAN_DAM,
        popup="""
馬太鞍溪堰塞湖
- 位置：花蓮縣萬榮鄉馬太鞍溪上游
- 座標：約 23.6995°N, 121.2955°E
- 由大規模山崩堵塞溪谷所形成的堰塞湖
""",
    )

    # 光復鄉主要受災區（示意）
    m.add_marker(
        GUANGFU_TOWN,
        popup="""
光復鄉受災區（示意）
- 光復鄉多處聚落位在馬太鞍溪下游沖積扇上
- 2025/9/23 堰塞湖潰決後，泥流沿溪道湧入市區與周邊農地
""",
    )

    # 用折線表示上游往下游的流向
    m.add_polyline(
        locations=[MATAIAN_DAM, GUANGFU_TOWN],
        color="red",
        weight=4,
        opacity=0.8,
        popup="堰塞湖溢流與潰決後的主要流向示意",
    )

    return m


@solara.component
def Page():
    m = solara.use_memo(create_map, dependencies=[MAPTILER_KEY])

    with solara.Column(
        gap="1rem",
        style={"maxWidth": "1100px", "margin": "0 auto"},
    ):
        solara.Markdown("## 災害發生位置：上游堰塞湖與下游光復鄉")

        with solara.Row(gap="1.5rem", style={"flexWrap": "wrap"}):
            with solara.Column(style={"flex": "1 1 320px"}):
                solara.Markdown(
                    """
### 空間關係說明

- 上游山區：堰塞湖所在位置 
  馬太鞍溪發源於中央山脈東側，流經萬榮鄉山區。
  2025 年豪雨引發的大規模山崩堵塞溪谷，在海拔約 1,100 公尺附近形成堰塞湖，
  座標約為 23.6995°N, 121.2955°E。〔維基百科與政府勘查資料〕  

- 中游峽谷：能量傳遞路段 
  河道在明利村上游一帶呈狹窄峽谷地形，崩塌物與洪水能量難以快速擴散，
  泥流在此段維持高流速與高沖刷力。〔水利署第九河川分署資料〕  

- 下游平原：光復鄉受災區
  馬太鞍溪於出山口後，河道進入光復鄉平原與沖積扇，
  聚落與農地集中於此區，因此堰塞湖潰決所產生的洪峰
  在短時間內造成嚴重淹水與土砂堆積。  

以兩個代表點（上游堰塞湖、下游光復市區）與一條折線，
簡化呈現「山崩—堰塞湖—下游淹水」的空間關係。
"""
                )

            with solara.Column(style={"flex": "1 1 420px", "minHeight": "520px"}):
                solara.display(m.to_solara())
