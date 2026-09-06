"""
Content detail view - 内容详情页
"""
import flet as ft


STATUS_BAR_HEIGHT = 48


def build_detail(
    page: ft.Page,
    gradient_colors,
    text_color,
    text_color2,
    item_index,
    on_back,
    on_share,
):
    user_name = f"用户{item_index}"
    like_count = item_index * 128
    comment_field = ft.TextField(
        hint_text="说点什么...",
        height=40,
        border_radius=20,
        border_color="0xDDDDDD",
        text_size=13,
        content_padding=ft.padding.Padding(left=14, top=0, right=14, bottom=0),
        expand=True,
    )

    async def _share(e):
        await on_share()

    detail_page = ft.Column(
        [
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(
                height=52,
                padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
                content=ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.CHEVRON_LEFT,
                            icon_size=26,
                            icon_color=text_color2(),
                            width=28,
                            height=40,
                            padding=0,
                            on_click=lambda e: on_back(),
                        ),
                        ft.Container(
                            width=32,
                            height=32,
                            border_radius=16,
                            bgcolor="0x90CAF9",
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(str(item_index), color="white"),
                        ),
                        ft.Text(
                            user_name,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=text_color(),
                        ),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.SHARE_OUTLINED,
                            icon_color=text_color2(),
                            tooltip="分享",
                            on_click=_share,
                        ),
                    ],
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            ft.Column(
                [
                    ft.Container(
                        height=300,
                        margin=ft.margin.Margin(left=28, top=12, right=28, bottom=0),
                        border_radius=12,
                        bgcolor="0xD1C4E9",
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(ft.Icons.IMAGE_OUTLINED, size=64, color="white"),
                    ),
                    ft.Container(
                        padding=ft.padding.Padding(left=28, top=16, right=28, bottom=8),
                        content=ft.Text(
                            "这是一段内容详情文字，展示卡片中的完整描述信息。"
                            "这里可以放置更完整的图文内容介绍，包括事件背景、相关说明和详细信息。"
                            "用户可以通过上下滑动阅读全部内容，了解内容的来龙去脉和更多细节。"
                            "我们会持续补充有价值的信息，帮助用户更全面地理解当前内容。"
                            "请结合实际情况进行判断，并关注后续更新。"
                            "\n\n"
                            "在使用过程中，如果你对内容有任何疑问，可以通过下方评论区域进行交流。"
                            "欢迎分享你的看法和经验，也可以收藏当前内容，方便之后再次查看。"
                            "不同用户可能会有不同的理解，评论内容仅代表发布者个人观点。"
                            "\n\n"
                            "以上内容经过整理后展示，部分信息可能会因为时间变化而更新。"
                            "建议在阅读后结合可靠来源进行进一步核实，并根据自己的实际需求作出决定。",
                            size=15,
                            color=text_color(),
                        ),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(left=28, top=18, right=28, bottom=88),
                        padding=ft.padding.Padding(left=14, top=10, right=14, bottom=10),
                        border_radius=8,
                        bgcolor="0xF2F2F2",
                        content=ft.Text(
                            "免责声明：以上内容仅供参考，不构成任何建议或承诺。"
                            "相关信息可能存在滞后或误差，请结合实际情况独立判断。",
                            size=11,
                            color="0x888888",
                        ),
                    ),
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
        ],
        spacing=0,
        expand=True,
    )
    favorite_button = ft.IconButton(
        icon=ft.Icons.STAR_BORDER,
        icon_color=text_color2(),
        tooltip="收藏",
    )
    favorite_active = [False]

    def _toggle_favorite(e):
        favorite_active[0] = not favorite_active[0]
        favorite_button.icon = (
            ft.Icons.STAR if favorite_active[0] else ft.Icons.STAR_BORDER
        )
        favorite_button.icon_color = "0xE53935" if favorite_active[0] else text_color2()
        page.update()

    favorite_button.on_click = _toggle_favorite

    like_active = [False]
    like_group = ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.FAVORITE_BORDER,
                icon_color="0xE57373",
                tooltip="点赞",
                padding=0,
            ),
            ft.Text(str(like_count), size=12, color=text_color2()),
        ],
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    like_button = like_group.controls[0]

    def _toggle_like(e):
        like_active[0] = not like_active[0]
        like_button.icon = (
            ft.Icons.FAVORITE if like_active[0] else ft.Icons.FAVORITE_BORDER
        )
        like_button.icon_color = "0xE53935" if like_active[0] else "0xE57373"
        page.update()

    like_button.on_click = _toggle_like

    def _send_comment(e):
        if comment_field.value and comment_field.value.strip():
            comment_field.value = ""
            page.update()

    send_button = ft.Container(
        width=36,
        alignment=ft.Alignment.CENTER,
        content=ft.Text("发送", size=13, color="0x4A90D9"),
        on_click=_send_comment,
        visible=False,
    )

    comment_bar = ft.Container(
        left=12,
        right=12,
        bottom=8,
        padding=ft.padding.Padding(left=8, top=6, right=8, bottom=6),
        border_radius=26,
        bgcolor="white",
        content=ft.Row(
            [
                comment_field,
                send_button,
                favorite_button,
                ft.Container(width=6),
                like_group,
            ],
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    def _set_comment_mode(active):
        send_button.visible = active
        favorite_button.visible = not active
        like_group.visible = not active
        page.update()

    comment_field.on_focus = lambda e: _set_comment_mode(True)
    comment_field.on_blur = lambda e: _set_comment_mode(False)

    async def _share(e):
        await on_share()

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Stack(
            [
                detail_page,
                ft.Container(
                    left=0,
                    right=0,
                    bottom=0,
                    height=80,
                    bgcolor="white",
                ),
                comment_bar,
            ],
            expand=True,
        ),
    )
