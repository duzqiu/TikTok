"""
Home view — 首页页面
"""
import flet as ft

STATUS_BAR_HEIGHT = 48


def build_home(
    page: ft.Page,
    home_tabs,
    home_tab_index,
    secondary_tabs,
    secondary_index,
    primary_tab_row,
    secondary_tab_row,
    home_content,
    gradient_colors,
    text_color,
    text_color2,
    text_color3,
):
    def _update_primary_tabs():
        primary_tab_row.controls.clear()
        for i, t in enumerate(home_tabs):
            is_active = (i == home_tab_index[0])
            primary_tab_row.controls.append(
                ft.Container(
                    padding=ft.padding.Padding(left=12, top=6, right=12, bottom=6),
                    border_radius=16,
                    bgcolor=ft.Colors.with_opacity(0.3, "0x4A90D9") if is_active else None,
                    on_click=lambda e, idx=i: _on_primary_click(idx),
                    content=ft.Text(t, size=14,
                                    weight=ft.FontWeight.W_900,
                                    color="0x333333" if is_active else "0x333333"),
                )
            )

    def _update_secondary_tabs():
        primary = home_tabs[home_tab_index[0]]
        subs = secondary_tabs.get(primary, [])
        sub_idx = secondary_index[0] if secondary_index[0] < len(subs) else 0
        secondary_tab_row.controls.clear()
        for i, t in enumerate(subs):
            is_active = (i == sub_idx)
            secondary_tab_row.controls.append(
                ft.Container(
                    padding=ft.padding.Padding(left=10, top=6, right=10, bottom=4),
                    on_click=lambda e, idx=i: _on_secondary_click(idx),
                    content=ft.Column([
                        ft.Text(t, size=12,
                                weight=ft.FontWeight.W_500 if is_active else ft.FontWeight.NORMAL,
                                color=text_color() if is_active else text_color3()),
                        ft.Container(height=2, border_radius=1,
                                     bgcolor="0x4A90D9" if is_active else None),
                    ], spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                )
            )

    def _update_home_content():
        import random
        random.seed(home_tab_index[0] * 100 + secondary_index[0])
        colors = ["0xFFCDD2", "0xF8BBD0", "0xD1C4E9", "0xC5CAE9", "0xBBDEFB",
                  "0xB2EBF2", "0xB2DFDB", "0xC8E6C9", "0xFFF9C4", "0xFFE0B2",
                  "0xD7CCC8", "0xCFD8DC"]
        cards = []
        for i in range(12):
            bg = random.choice(colors)
            cards.append(
                ft.Container(
                    expand=True, border_radius=8,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    content=ft.Column([
                        ft.Container(
                            height=130, bgcolor=bg, border_radius=8,
                            alignment=ft.Alignment.CENTER,
                            content=ft.Icon(ft.Icons.PLAY_CIRCLE_OUTLINE, size=40, color="white"),
                        ),
                        ft.Container(
                            padding=ft.padding.Padding(left=0, top=8, right=0, bottom=8),
                            content=ft.Column([
                                ft.Text("这是一段描述文字，最多显示两行，超出部分用省略号显示",
                                        size=11, color=text_color2(), max_lines=2,
                                        overflow=ft.TextOverflow.ELLIPSIS),
                                ft.Row([
                                    ft.Container(
                                        width=24, height=24, border_radius=12, bgcolor=bg,
                                        alignment=ft.Alignment.CENTER,
                                        content=ft.Text(str(i+1), size=10, color="white",
                                                        weight=ft.FontWeight.BOLD),
                                    ),
                                    ft.Text(f"用户{i+1}", size=12, color=text_color3(),
                                            overflow=ft.TextOverflow.ELLIPSIS),
                                ], spacing=6, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                            ], spacing=4),
                        ),
                    ], spacing=0),
                )
            )

        left_col = [cards[i] for i in range(0, len(cards), 2)]
        right_col = [cards[i] for i in range(1, len(cards), 2)]
        while len(left_col) > len(right_col):
            right_col.append(ft.Container(height=0))
        while len(right_col) > len(left_col):
            left_col.append(ft.Container(height=0))

        rows = [ft.Row([l, r], spacing=10, expand=True) for l, r in zip(left_col, right_col)]
        scrollable = ft.Column(rows, spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)

        home_content.content = ft.Column([
            ft.Container(
                padding=ft.padding.Padding(left=24, top=4, right=24, bottom=80),
                content=scrollable, expand=True,
            ),
        ], spacing=0, expand=True)

    def _on_primary_click(idx):
        home_tab_index[0] = idx
        secondary_index[0] = 0
        _update_primary_tabs()
        _update_secondary_tabs()
        _update_home_content()
        page.update()

    def _on_secondary_click(idx):
        secondary_index[0] = idx
        _update_secondary_tabs()
        _update_home_content()
        page.update()

    _update_primary_tabs()
    _update_secondary_tabs()
    _update_home_content()

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column([
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(height=16),
            ft.Container(
                padding=ft.padding.Padding(left=12, top=8, right=12, bottom=8),
                content=ft.ListView(controls=[primary_tab_row], horizontal=True, height=36),
            ),
            ft.Container(
                padding=ft.padding.Padding(left=12, top=0, right=12, bottom=4),
                content=ft.ListView(controls=[secondary_tab_row], horizontal=True, height=32),
            ),
            home_content,
        ], spacing=0, expand=True),
    )
