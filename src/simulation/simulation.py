import arcade
import arcade.gui


class SecondPage(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Second Page", self.window.width/2, self.window.height/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")


class MainView(arcade.View):
    def __init__(self, window: arcade.Window):
        super().__init__(window)
        self.window = window
        self.v_box = None
        self.manager = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="SwarmBot Simulator",
                                              width=450,
                                              height=40,
                                              font_size=22,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        text = "This application is a simulation of a swarm of robots. " \
               "The aim of the simulation is to show how a swarm of robots " \
               "can be used to reach a target. "
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        ui_flatbutton = arcade.gui.UIFlatButton(text="Start", width=200)
        self.v_box.add(ui_flatbutton.with_space_around(bottom=20))

        @ui_flatbutton.event("on_click")
        def on_click_flatbutton(event):
            self.manager.disable()
            self.window.show_view(SecondPage(self.window))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()


def main():
    window = arcade.Window(800, 600, "SwarmBot Simulator")
    window.show_view(MainView(window))
    arcade.run()


if __name__ == "__main__":
    main()
