import solara
import importlib.util
from pathlib import Path

# 取得專案根目錄
ROOT = Path(__file__).parent


def load_page_module(module_name: str, relative_path: str):
    """手動載入 pages 資料夾裡的 .py 檔，檔名可以是 01_xxx.py 這種。"""
    file_path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


# 載入三個分頁的 Page()
intro_mod = load_page_module("page_intro", "pages/01_intro.py")
map2d_mod = load_page_module("page_2d", "pages/02_2d_map.py")
map3d_mod = load_page_module("page_3d", "pages/03_3d_map.py")


# -------- 各頁面的 Wrapper Component --------

@solara.component
def IntroPage():
    intro_mod.Page()


@solara.component
def Map2DPage():
    map2d_mod.Page()


@solara.component
def Map3DPage():
    map3d_mod.Page()


# -------- Route 設定 --------

routes = [
    solara.Route(path="/", component=IntroPage, label="01_INTRO"),
    solara.Route(path="/02_2d_map", component=Map2DPage, label="02_2D_MAP"),
    solara.Route(path="/03_3d_map", component=Map3DPage, label="03_3D_MAP"),
]


# -------- 主入口 Component --------

@solara.component
def Page():
    solara.AppLayout(
        title="連恆宥的花蓮馬太鞍溪堰塞湖災害地圖",
        routes=routes,
    )
