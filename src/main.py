import flet as ft

from views.home_view import build_home
from views.explore_view import build_explore
from views.detail_view import build_detail
from views.search_view import build_search
from views.profile_view import build_profile
from views.settings_view import build_settings
from views.about_view import build_about
from views.language_view import build_language
from views.region_view import build_region
from views.account_security_view import build_account_security
from views.login_view import build_login
from views.register_view import build_register

STATUS_BAR_HEIGHT = 48


def main(page: ft.Page):
    page.title = "TikTok"
    page.window.width = 412
    page.window.height = 760
    page.window.resizable = False
    page.padding = 0
    page.bgcolor = "white"
    share_service = ft.Share()
    page.services.append(share_service)
    page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_visibility=False, track_visibility=False, thickness=0))
    page.dark_theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_visibility=False, track_visibility=False, thickness=0))

    # ── 共享状态 ──
    current_index = [0]
    is_settings = [False]
    bottom_tab_buttons = []
    home_tabs = ["关注", "发现", "上海"]
    home_tab_index = [0]
    secondary_tabs = {
        "关注": ["最新", "精选", "动态"],
        "发现": ["推荐", "热门", "关注"],
        "上海": ["本地", "热门", "最新"],
    }
    secondary_index = [0]
    content_area = ft.Container(expand=True)
    bottom_bar = ft.Container()
    primary_tab_row = ft.Row(spacing=4)
    secondary_tab_row = ft.Row(spacing=0)
    home_content = ft.Container(expand=True)
    profile_list_ref = ft.Ref[ft.ListView]()
    profile_scroll_offset = [0.0]
    selected_language = ["中文简体"]
    selected_region = ["中国"]

    # ── 主题辅助 ──
    def is_dark():
        return page.theme_mode == ft.ThemeMode.DARK

    def text_color():
        return "0xE0E0E0" if is_dark() else "0x333333"

    def text_color2():
        return "0xBBBBBB" if is_dark() else "0x666666"

    def text_color3():
        return "0x888888" if is_dark() else "0x999999"

    def gradient_colors():
        if is_dark():
            return ["0x1A1A2E", "0x121212"]
        return ["0xE3F2FD", "0xFFFFFF"]

    # ── 设置相关 ──
    dark_mode_switch = ft.Switch(value=False, active_color="0x4A90D9")

    def _apply_dark_mode(enabled):
        if enabled:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = "0x121212"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = "white"

    def _toggle_dark_mode(e):
        _apply_dark_mode(dark_mode_switch.value)
        _refresh_settings()

    dark_mode_switch.on_change = _toggle_dark_mode

    def _refresh_settings():
        content_area.content = build_settings(
            page, gradient_colors, text_color, text_color2, text_color3,
            dark_mode_switch, on_back=lambda: _switch(2),
        )
        page.update()

    def _show_register():
        bottom_bar.visible = False
        content_area.content = build_register(
            page,
            gradient_colors,
            text_color,
            text_color2,
            on_back=_show_login,
        )
        page.update()

    def _hide_bottom_bar(hide):
        bottom_bar.visible = not hide
        page.update()

    def _show_about():
        bottom_bar.visible = False
        content_area.content = build_about(
            page, gradient_colors, text_color, text_color2, text_color3,
            on_back=lambda: _switch(2),
        )
        page.update()

    def _show_language():
        bottom_bar.visible = False
        content_area.content = build_language(
            page, gradient_colors, text_color, text_color2, text_color3,
            selected_language[0],
            on_back=lambda: _switch(2),
            on_select=_select_language,
        )
        page.update()

    def _select_language(language):
        selected_language[0] = language
        _switch(2)

    def _show_region():
        bottom_bar.visible = False
        content_area.content = build_region(
            page, gradient_colors, text_color, text_color2, text_color3,
            selected_region[0],
            on_back=lambda: _switch(2),
            on_select=_select_region,
        )
        page.update()

    def _select_region(region):
        selected_region[0] = region
        _switch(2)

    def _show_account_security():
        bottom_bar.visible = False
        content_area.content = build_account_security(
            page, gradient_colors, text_color, text_color2, text_color3,
            on_back=lambda: _switch(2),
        )
        page.update()

    def _show_login():
        bottom_bar.visible = False
        content_area.content = build_login(
            page,
            gradient_colors,
            text_color,
            text_color2,
            on_back=lambda: _switch(2),
            on_register=_show_register,
        )
        page.update()

    def _show_search():
        bottom_bar.visible = False
        publish_button.visible = False
        content_area.content = build_explore(
            page,
            gradient_colors,
            text_color,
            text_color2,
            on_search_focus=_hide_bottom_bar,
            on_back=lambda: _switch(0),
        )
        page.update()

    def _show_detail(item_index):
        bottom_bar.visible = False
        publish_button.visible = False

        async def _share_detail():
            try:
                await share_service.share_text(
                    text=(
                        f"用户{item_index}的内容："
                        "这是一段内容详情文字，展示卡片中的完整描述信息。"
                    )
                )
            except RuntimeError:
                page.show_dialog(
                    ft.SnackBar(content=ft.Text("当前平台暂不支持系统分享"))
                )

        content_area.content = build_detail(
            page,
            gradient_colors,
            text_color,
            text_color2,
            item_index,
            on_back=lambda: _switch(0),
            on_share=_share_detail,
        )
        page.update()

    # ── 页面构建 ──
    def _build_home():
        return build_home(
            page, home_tabs, home_tab_index, secondary_tabs, secondary_index,
            primary_tab_row, secondary_tab_row, home_content,
            gradient_colors, text_color, text_color2, text_color3,
            on_search_click=_show_search,
            on_card_click=_show_detail,
        )

    def _build_explore():
        return build_explore(
            page, gradient_colors, text_color, text_color2,
            on_search_focus=_hide_bottom_bar,
        )

    def _build_profile():
        return build_profile(
            page, gradient_colors, text_color, text_color2, text_color3,
            on_about=_show_about,
            on_language=_show_language,
            on_region=_show_region,
            on_account_security=_show_account_security,
            on_login=_show_login,
            selected_language=selected_language[0],
            selected_region=selected_region[0],
            scroll_ref=profile_list_ref,
            on_scroll=lambda e: profile_scroll_offset.__setitem__(0, e.pixels),
        )

    async def _restore_profile_scroll():
        if profile_scroll_offset[0] > 0 and profile_list_ref.current:
            await profile_list_ref.current.scroll_to(offset=profile_scroll_offset[0])

    pages = [_build_home, _build_explore, _build_profile]
    tabs_config = [
        (ft.Icons.HOME_OUTLINED, ft.Icons.HOME, "首页"),
        (ft.Icons.SEARCH, ft.Icons.SEARCH, "发现"),
        (ft.Icons.PERSON_OUTLINE, ft.Icons.PERSON, "我的"),
    ]

    def _make_tab(idx, icon_out, icon_in, label):
        btn_icon = ft.Icon(icon_out, size=22, color="0x999999")
        btn_label = ft.Text(label, size=11, color="0x999999")
        inner = ft.Container(
            expand=True, height=64,
            padding=ft.padding.Padding(left=0, top=8, right=0, bottom=4),
            alignment=ft.Alignment.CENTER,
            on_click=lambda e, i=idx: _switch(i),
            content=ft.Column([btn_icon, btn_label], spacing=2,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
        bottom_tab_buttons.append((inner, btn_icon, btn_label, icon_out, icon_in))
        return inner

    def _switch(idx):
        is_settings[0] = False
        bottom_bar.visible = True
        current_index[0] = idx
        publish_button.visible = idx == 0
        for i, (_, icon_w, label_w, icon_out, icon_in) in enumerate(bottom_tab_buttons):
            active = i == idx
            icon_w.name = icon_in if active else icon_out
            label_w.weight = ft.FontWeight.BOLD if active else ft.FontWeight.NORMAL
            icon_w.color = "0x4A90D9" if active else "0x999999"
            label_w.color = "0x4A90D9" if active else "0x999999"
        content_area.content = pages[idx]()
        page.update()
        if idx == 2 and profile_scroll_offset[0] > 0:
            page.run_task(_restore_profile_scroll)

    tab_row = ft.Row(
        controls=[_make_tab(i, *t) for i, t in enumerate(tabs_config)],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY, spacing=0, expand=True,
    )

    def _bottom_bar_bg():
        if page.theme_mode == ft.ThemeMode.DARK:
            return ft.Colors.with_opacity(0.6, "0x1E1E1E")
        return ft.Colors.with_opacity(0.6, "white")

    bottom_bar = ft.Container(
        height=64,
        bgcolor=_bottom_bar_bg(),
        border=ft.border.Border(
            top=ft.BorderSide(0.5, ft.Colors.with_opacity(0.15, "0x4A90D9")),
            left=ft.BorderSide(0, "transparent"),
            right=ft.BorderSide(0, "transparent"),
            bottom=ft.BorderSide(0, "transparent"),
        ),
        padding=ft.padding.Padding(left=8, top=0, right=8, bottom=0),
        content=tab_row,
        blur=ft.Blur(25, 25, ft.BlurTileMode.MIRROR),
    )

    def _open_publish(e):
        page.show_dialog(
            ft.SnackBar(content=ft.Text("发布功能即将开放"))
        )

    publish_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.with_opacity(0.62, "0x64B5F6"),
        foreground_color=ft.Colors.WHITE,
        tooltip="发布",
        elevation=8,
        on_click=_open_publish,
    )

    page.add(
        ft.Stack([
            ft.Column([content_area], spacing=0, expand=True),
            ft.Container(
                bottom=0, left=0, right=0,
                content=bottom_bar,
            ),
            ft.Container(
                right=36,
                bottom=96,
                content=publish_button,
            ),
        ], expand=True)
    )

    _switch(0)


if __name__ == "__main__":
    ft.run(main)
