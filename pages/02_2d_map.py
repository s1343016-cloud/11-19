# pages/02_2d_map.py
import solara
import leafmap.leafmap as leafmap

def create_2d_map():
    # 建立 2D 地圖物件（ipyleaflet 後端）
    m = leafmap.Map(center=[23.7, 120.9], zoom=7)

    # 底圖（可換成你喜歡的）
    m.add_basemap("CartoDB.DarkMatter")

    # 範例：加入一個 GeoJSON（換成你自己的資料）
    # 假設檔案放在 data/your_data.geojson
    try:
        m.add_geojson("data/your_data.geojson", layer_name="故事圖層")
    except Exception as e:
        print("載入 GeoJSON 發生錯誤：", e)

    return m

@solara.component
def Page():
    solara.Title("2D 互動式故事地圖")

    # 使用 use_memo，避免每次重建地圖（跟 PDF 的快取示範同理）
    map_obj = solara.use_memo(create_2d_map, dependencies=[])

    with solara.Column():
        solara.Markdown("## 故事章節：2D 地圖視角")
        solara.Markdown(
            """
在這個章節，你可以：
- 利用圖層顯示不同時期、不同主題的資料
- 搭配文字說明地圖上看到的空間變化
            """
        )

        # 左文右圖的排版（模仿 StoryMaps 文字 + 地圖）
        with solara.Row():
            solara.Markdown(
                """
### 這裡是敘事文字區

說明：
- 這個圖層代表什麼？
- 有哪些空間 pattern？
- 你希望讀者注意哪個地區？
                """,
                style={"width": "40%", "padding": "10px"}
            )

            with solara.Column(style={"width": "60%", "height": "600px"}):
                solara.display(map_obj)
