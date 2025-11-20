import solara

# 你的 Space 上檔案的基底網址
SPACE_BASE_URL = "https://huggingface.co/spaces/lien123/11-19/resolve/main/"


@solara.component
def Page():
    with solara.Column(
        gap="1.5rem",
        style={"maxWidth": "1100px", "margin": "0 auto"},
        align="center",
    ):
        solara.Markdown(
            """
# 連恆宥的花蓮馬太鞍溪堰塞湖災害地圖


"""
        )

        solara.Markdown(
            """
## 災害背景簡介

- 堰塞湖的形成  
  2025 年 7 月，受颱風帶來的豪雨影響，花蓮縣萬榮鄉馬太鞍溪上游發生大規模山崩，
  約數千萬立方公尺土石崩落並堵塞溪谷，形成大型堰塞湖。依花蓮縣政府與林業及自然保育署資料，
  壩體高度超過百公尺，湖面面積達數十公頃，屬於高潛勢的崩塌—堰塞湖。〔花蓮縣政府堰塞湖資訊專區、林業及自然保育署公告〕  

- 潰決與淹水* 
  2025 年 9 月 23 日下午約 14:50，受到強颱樺加沙帶來的歷史性豪雨影響，
  馬太鞍溪堰塞湖溢流並開始侵蝕壩體，短時間內釋放約 6,000 萬噸以上的水體與土砂，
  大量泥流沿溪道往下游沖刷。光復鄉多處聚落被淹沒，房屋、道路與農地嚴重受損，
  造成十餘人死亡與多人失聯，為近年臺灣重大水文災害之一。〔中央災害應變中心統計、中央社與路透社等報導〕  

- 目的 
  本透過互動地圖與 3D 地形視覺化，說明堰塞湖的位置、下游淹水區位與周遭地形條件，
  協助理解「上游山崩—堰塞湖形成—壩體潰決—下游淹水」的完整過程。
"""
        )

        solara.Markdown("## 災情照片")

        with solara.Row(
            gap="1rem",
            style={"flexWrap": "wrap", "justifyContent": "center"},
        ):
            _photo_card(
                SPACE_BASE_URL + "images/堰塞湖_01.jpg.jpg",
                "馬太鞍溪上游堰塞湖空拍影像（上游山區被崩塌物與湖水覆蓋）",
            )
            _photo_card(
                SPACE_BASE_URL + "images/橋梁損毀_02.jpg.jpg",
                "下游河道暴漲、沖斷橋梁，顯示洪峰能量與夾帶土砂規模",
            )
            _photo_card(
                SPACE_BASE_URL + "images/土石流_03.jpg",
                "土砂與泥流淹沒聚落，搜救人員在受災區域執行任務",
            )

        solara.Markdown(
            """
> 資料整理來源：  
> 花蓮縣政府「馬太鞍溪堰塞湖資訊專區」、農業部林業及自然保育署、  
> 水利署第九河川分署、中央災害應變中心新聞稿，  
> 以及中央社、路透社、Focus Taiwan、臺北時報等公開報導與  
> 〈花蓮馬太鞍溪堰塞湖災害〉維基百科條目等。
"""
        )


@solara.component
def _photo_card(url: str, caption: str):
    with solara.Card(style={"width": "340px"}):
        solara.Image(url, width="100%")
        solara.Markdown(f"*{caption}*")
