import tkinter
from gui.components import labels, buttons


class Sidebar(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "#BEB7A4"
        super().__init__(parent, width=150, height=600, bg=self.bg)
        self.parent = parent

        self.title = labels.SidebarLabel(self, text="Sidebar")
        self.title.pack()

        self.npc_button = buttons.Sidebarbutton(
            self, text="NPC", command=lambda: self.switch_frame(self.parent.npc_frame)
        )
        self.npc_button.pack()

        # self.attack_button = buttons.Sidebarbutton(
        #     self,
        #     text="Attack",
        #     command=lambda: self.switch_frame(self.parent.attack_frame),
        # )
        # self.attack_button.pack()

        self.construction_button = buttons.Sidebarbutton(
            self,
            text="Construction",
            command=lambda: self.switch_frame(self.parent.construction_frame),
        )
        self.construction_button.pack()

        self.recruitment_button = buttons.Sidebarbutton(
            self,
            text="Recruitment",
            command=lambda: self.switch_frame(self.parent.recruitment_frame),
        )
        self.recruitment_button.pack()

        self.alliance_button = buttons.Sidebarbutton(
            self,
            text="Alliance",
            command=lambda: self.switch_frame(self.parent.alliance_frame),
        )
        self.alliance_button.pack()

        # self.lookup_button = buttons.Sidebarbutton(
        #     self,
        #     text="Lookup",
        #     command=lambda: self.switch_frame(self.parent.lookup_frame),
        # )
        # self.lookup_button.pack()

        self.outposts_button = buttons.Sidebarbutton(
            self,
            text="Outposts",
            command=lambda: self.switch_frame(self.parent.outposts_frame),
        )
        self.outposts_button.pack()

        self.market_button = buttons.Sidebarbutton(
            self,
            text="Market",
            command=lambda: self.switch_frame(self.parent.market_frame),
        )
        self.market_button.pack()

        self.apiKey_button = buttons.Sidebarbutton(
            self,
            text="API Key",
            command=lambda: self.switch_frame(self.parent.api_key_frame),
        )
        self.apiKey_button.pack()
        self.version_label = labels.InputLabel(
            self, text="v0.2.0-alpha (Dev)", font=("Arial", 10)
        )
        self.version_label.place(x=0, y=580)

    def disable_option(self, button: str) -> None:
        if button == "npc":
            btn = self.npc_button
        # elif button == "attack":
        #    btn = self.attack_button
        elif button == "construction":
            btn = self.construction_button
        elif button == "recruitment":
            btn = self.recruitment_button
        elif button == "alliance":
            btn = self.alliance_button
        # elif button == "lookup":
        #    btn = self.lookup_button
        elif button == "outposts":
            btn = self.outposts_button
        elif button == "apiKey":
            btn = self.apiKey_button

        if btn:  # type: ignore
            btn.pack_forget()

    def switch_frame(self, frame):
        self.master.change_frame(frame)  # type: ignore # this seems to be right? I'm not sure why it's throwing an error with pyright
