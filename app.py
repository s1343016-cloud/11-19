# app.py
import solara

@solara.component
def Page():
    solara.Title("我的 StoryMap：互動式 GIS 故事網站")

    with solara.Column():
        solara.Markdown("# 我的 StoryMap")
        solara.Markdown(
            """
歡迎來到互動式 GIS 故事網站。  
左側（或上方）的導覽可以切換不同章節：
- 01 Intro：故事封面與背景說明
- 02 2D Map：互動式 2D 故事地圖
- 03 3D Map：3D 地形視角
            """
        )
