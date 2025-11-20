import solara

routes = [
    solara.Route(path="/", component=lambda: solara.Markdown("# 我的 StoryMap\n請從左側選擇章節")),
    solara.Route(path="/01_intro", component=lambda: solara.pages["01_intro"].Page()),
    solara.Route(path="/02_2d_map", component=lambda: solara.pages["02_2d_map"].Page()),
    solara.Route(path="/03_3d_map", component=lambda: solara.pages["03_3d_map"].Page()),
]

@solara.component
def Page():
    with solara.AppLayout(
        title="我的 StoryMap",
        sidebar=True,
        navigation=True,
        # 左側導覽的內容
        sidebar_content=solara.VBox(
            [
                solara.Markdown("## 章節選單"),
                solara.Link("01 Intro", "/01_intro"),
                solara.Link("02 2D Map", "/02_2d_map"),
                solara.Link("03 3D Map", "/03_3d_map"),
            ]
        ),
    ):
        solara.RouteFrame(routes=routes)
