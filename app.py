import solara

# --- 各頁面的 Wrapper Component ---------------------------------

@solara.component
def Home():
    # 首頁內容
    with solara.Column():
        solara.Markdown("# 我的 StoryMap")
        solara.Markdown(
            """
歡迎來到互動式 GIS 故事網站。  

上方的導覽列可以切換不同章節：
- 01 Intro：故事封面與背景說明
- 02 2D Map：互動式 2D 故事地圖
- 03 3D Map：3D 地形視角
            """
        )

@solara.component
def IntroPage():
    # 直接呼叫 pages/01_intro.py 裡的 Page()
    solara.pages["01_intro"].Page()

@solara.component
def Map2DPage():
    # 直接呼叫 pages/02_2d_map.py 裡的 Page()
    solara.pages["02_2d_map"].Page()

@solara.component
def Map3DPage():
    # 直接呼叫 pages/03_3d_map.py 裡的 Page()
    solara.pages["03_3d_map"].Page()

# --- Route 設定 ---------------------------------------------------

routes = [
    solara.Route(path="/", component=Home, label="HOME"),
    solara.Route(path="/01_intro", component=IntroPage, label="01_INTRO"),
    solara.Route(path="/02_2d_map", component=Map2DPage, label="02_2D_MAP"),
    solara.Route(path="/03_3d_map", component=Map3DPage, label="03_3D_MAP"),
]

# --- 主入口 Component ----------------------------------------------

@solara.component
def Page():
    # 使用 AppLayout，自動產生上方面板 + Route 切換
    solara.AppLayout(
        title="我的 StoryMap",
        routes=routes,
    )
