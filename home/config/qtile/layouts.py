from libqtile.config import Drag, Click
from libqtile import layout
from libqtile.command import lazy

from resources import MOD, COLORS


layouts = [
    layout.MonadTall(margin=10, border_focus=COLORS['b_cyan'], border_normal=COLORS['b_gray'], border_width=5),
    layout.MonadWide(margin=10, border_focus=COLORS['b_cyan'], border_normal=COLORS['b_gray'], border_width=5),
    layout.Max()
]

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wname': 'Steam Login'},
    {'wname': 'About Steam'}
])

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]
