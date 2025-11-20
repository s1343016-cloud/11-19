# pages/01_intro.py
import solara

@solara.component
def Page():
    solara.Title("故事封面與背景")

    with solara.Column():
        solara.Markdown("# 故事主題標題")
        solara.Markdown(
            """
這裡是故事地圖的開場（模仿 StoryMaps 的封面段落）。

你可以放：
- 主題說明
- 背景資料
- 研究問題 / 政策議題
- 一張代表性的圖片（可以用 HTML `<img>` 或 solara.Image）
            """
        )
