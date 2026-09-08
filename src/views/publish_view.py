"""
Publish view - 发布页面
"""
import flet as ft


STATUS_BAR_HEIGHT = 48


def build_publish(page, gradient_colors, text_color, text_color2, file_picker, on_back):
    title_field = ft.TextField(
        hint_text="请输入标题",
        width=360,
        border_radius=10,
        border=ft.InputBorder.NONE,
        text_size=14,
        content_padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
        height=44,
    )
    content_field = ft.TextField(
        hint_text="请输入内容",
        width=360,
        multiline=True,
        min_lines=10,
        max_lines=16,
        height=260,
        border_radius=10,
        border=ft.InputBorder.NONE,
        text_size=14,
        content_padding=ft.padding.Padding(left=12, top=10, right=12, bottom=10),
    )
    selected_images = []
    image_row = ft.Row(spacing=8, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    add_image_button = ft.OutlinedButton(
        "+",
        width=52,
        height=52,
        on_click=None,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=0,
        ),
    )
    image_row.controls.append(add_image_button)
    publish_button = ft.FilledButton(
        "发布",
        width=300,
        bgcolor="0x64B5F6",
        color="white",
    )

    def _preview_image(image_path):
        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="transparent",
            inset_padding=ft.padding.Padding(left=0, top=0, right=0, bottom=0),
            content_padding=ft.padding.Padding(left=0, top=0, right=0, bottom=0),
            content=ft.Stack(
                [
                    ft.Image(src=image_path, fit="contain"),
                    ft.Container(
                        top=8,
                        right=8,
                        content=ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color="0x666666",
                            bgcolor="white",
                            on_click=lambda e: _close_preview(dialog),
                        ),
                    ),
                ],
            ),
        )
        page.show_dialog(dialog)

    def _close_preview(dialog):
        dialog.open = False
        page.update()

    def _remove_image(index):
        selected_images.pop(index)
        _refresh_image_row()
        page.update()

    def _refresh_image_row():
        image_row.controls.clear()
        for index, image_path in enumerate(selected_images):
            image_row.controls.append(
                ft.Stack(
                    [
                        ft.Container(
                            width=52,
                            height=52,
                            border_radius=8,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            on_click=lambda e, path=image_path: _preview_image(path),
                            content=ft.Image(
                                src=image_path,
                                width=52,
                                height=52,
                                fit="cover",
                            ),
                        ),
                        ft.Container(
                            top=2,
                            right=2,
                            content=ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_size=14,
                                icon_color="white",
                                bgcolor=ft.Colors.with_opacity(0.65, "black"),
                                width=20,
                                height=20,
                                padding=0,
                                on_click=lambda e, item_index=index: _remove_image(item_index),
                            ),
                        ),
                    ],
                    width=52,
                    height=52,
                )
            )
        if len(selected_images) < 4:
            image_row.controls.append(add_image_button)

    async def _choose_image(e):
        files = await file_picker.pick_files(
            allow_multiple=True,
            file_type=ft.FilePickerFileType.IMAGE,
        )
        if files:
            remaining = 4 - len(selected_images)
            selected_images.extend(file.path for file in files[:remaining])
            _refresh_image_row()
            page.update()

    add_image_button.on_click = _choose_image

    def _publish(e):
        if not title_field.value or not title_field.value.strip():
            page.show_dialog(ft.SnackBar(content=ft.Text("请输入标题")))
            return
        if not content_field.value or not content_field.value.strip():
            page.show_dialog(ft.SnackBar(content=ft.Text("请输入内容")))
            return
        page.show_dialog(ft.SnackBar(content=ft.Text("发布成功")))

    publish_button.on_click = _publish

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column(
            [
                ft.Container(height=STATUS_BAR_HEIGHT),
                ft.Container(
                    padding=ft.padding.Padding(left=12, top=0, right=12, bottom=8),
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
                            ft.Text("发布", size=16, weight=ft.FontWeight.BOLD, color=text_color()),
                        ],
                        spacing=0,
                    ),
                ),
                ft.Container(
                    width=360,
                    margin=ft.margin.Margin(left=26, top=0, right=26, bottom=0),
                    padding=ft.padding.Padding(left=0, top=0, right=0, bottom=24),
                    content=ft.Column(
                        [
                            ft.Container(
                                width=360,
                                padding=ft.padding.Padding(left=12, top=7, right=12, bottom=7),
                                border_radius=8,
                                bgcolor="0xFFFBEA",
                                content=ft.Text(
                                    "完善标题、内容、图片以获取更多推荐",
                                    size=12,
                                    color=text_color2(),
                                ),
                            ),
                            ft.Container(
                                padding=ft.padding.Padding(left=0, top=8, right=0, bottom=0),
                                content=ft.Column(
                                    [
                                        title_field,
                                        ft.Container(
                                            margin=ft.margin.Margin(
                                                left=12, top=0, right=12, bottom=0
                                            ),
                                            content=ft.Divider(
                                                height=1,
                                                thickness=1,
                                                color="0xE8DDBD",
                                            ),
                                        ),
                                        content_field,
                                    ],
                                    spacing=0,
                                ),
                            ),
                            image_row,
                            ft.Text(
                                "最多选择4张图片",
                                size=12,
                                color=text_color2(),
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=publish_button,
                            ),
                        ],
                        spacing=16,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                    ),
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )
