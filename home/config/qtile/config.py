# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget

from typing import List

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, 'control'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'k', lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], 'space', lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, 'shift'], 'space', lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),
    Key([mod], 'Return', lazy.spawn('st')),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod, 'shift'], 'Tab', lazy.prev_layout()),
    Key([mod], 'w', lazy.window.kill()),

    # Lock screen
    Key([mod], 'l', lazy.spawn('lockscreen')),

    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'p', lazy.spawncmd()),

    # Launch applications
    Key([mod], 'c', lazy.spawn('code')),
    Key([mod], 'f', lazy.spawn('firefox')),
    Key([mod], 'g', lazy.spawn('google-chrome')),
    Key([mod], 'm', lazy.spawn('spotify')),

    Key([mod], 's', lazy.spawn("prtscr-select")),
    Key([mod, 'shift'], 's', lazy.spawn("prtscr-full")),

    # Volume
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -q sset Master 3%+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -q sset Master 3%-')),
]

# Colors
colors = {
    'n_black': '#222222',
    'n_red': '#e84f4f',
    'n_green': '#b7ce42',
    'n_yellow': '#fea63c',
    'n_blue': '#66aabb',
    'n_magenta': '#b7416e',
    'n_cyan': '#6d878d',
    'n_gray': '#dddddd',

    'b_black': '#666666',
    'b_red': '#d23d3d',
    'b_green': '#bde077',
    'b_yellow': '#ffe863',
    'b_blue': '#aaccbb',
    'b_magenta': '#e16a98',
    'b_cyan': '#42717b',
    'b_gray': '#cccccc',
}

# Fontawesome characters
fa_icons = {
    'code': '',
    'database': '',
    'headphones-alt': '',
    'microchip': '',
    'memory': '',
    'random': '',
    'server': '',
    'signal': '',
    'terminal': '',
    'th-list': '',
    'video': '',
    'wifi': '',
    'wrench': '',
    'battery-full': '',
    'battery-three-quarters': '',
    'battery-half': '',
    'battery-quarter': '',
    'battery-empty': '',
    'thermometer-full': '',
    'thermometer-three-quarters': '',
    'thermometer-half': '',
    'thermometer-quarter': '',
    'thermometer-empty': '',
    'volume-off': '',
    'volume-down': '',
    'volume-up': '',
    'globe-africa': '',
    'globe-americas': '',
    'globe-asia': '',
    'windows': '',
    'steam': '',
    'discord': '',
    'docker': '',
    'gitkraken': '',
    'fedora': '',
}

groups_data = [
    {
        'label': fa_icons['fedora'],
        'name': '1',
        'matches': None
    },
    {
        'label': fa_icons['globe-africa'],
        'name': '2',
        'matches': [Match(wm_class=['Firefox Developer Edition']),]
    },
    {
        'label': fa_icons['terminal'],
        'name': '3',
        'matches': None
    },
    {
        'label': fa_icons['code'],
        'name': '4',
        'matches': [Match(wm_class=['Visual Studio Code']),],
    },
    {
        'label': fa_icons['video'],
        'name': '5',
        'matches': None
    },
    {
        'label': fa_icons['steam'],
        'name': '6',
        'matches': [Match(wm_class=['steam'], role=['game']),],
    },
    {
        'label': fa_icons['windows'],
        'name': '7',
        'matches': [Match(wm_class=['qemu']),],
    },
    {
        'label': fa_icons['random'],
        'name': '0',
        'matches': None
    }
]

# groups = [Group(i) for i in "1234567890"]
groups = [Group(name=i['name'], label=i['label'], matches=i['matches']) for i in groups_data]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(margin=10, border_focus=colors['b_cyan'], border_normal=colors['b_gray'], border_width=5),
    layout.MonadWide(margin=10, border_focus=colors['b_cyan'], border_normal=colors['b_gray'], border_width=5),
    layout.Max()
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(highlight_method='line', this_current_screen_border='fea63c'),
                widget.Prompt(),
                widget.WindowName(),
                widget.Sep(),
                widget.TextBox(fa_icons['wifi'], foreground=colors['n_green']),
                widget.Net(interface='wlp59s0', foreground=colors['n_green']),
                widget.TextBox(fa_icons['microchip'], foreground=colors['n_yellow']),
                widget.CPUGraph(frequency=2, graph_color=colors['n_yellow'], line_width=1),
                widget.TextBox(fa_icons['memory'], foreground=colors['n_blue']),
                widget.MemoryGraph(frequency=2, graph_color=colors['n_blue'], line_width=1),
                widget.TextBox(fa_icons['battery-full'], foreground=colors['n_magenta']),
                widget.Battery(foreground=colors['n_magenta']),
                widget.Sep(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=colors['n_cyan']),
                widget.Systray(),
                widget.Sep(),
                # widget.CapsNumLockIndicator(),
                # widget.KeyboardLayout(configured_keyboards=['us', 'fr']),
                # widget.Sep(),
                widget.CurrentLayoutIcon(scale=0.7)
            ],
            24
        )
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(highlight_method='line', this_current_screen_border='fea63c'),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=colors['n_cyan']),
                widget.CurrentLayoutIcon(scale=0.7)
            ],
            24
        )
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(highlight_method='line', this_current_screen_border='fea63c'),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=colors['n_cyan']),
                widget.CurrentLayoutIcon(scale=0.7)
            ],
            24
        )
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(highlight_method='line', this_current_screen_border='fea63c'),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=colors['n_cyan']),
                widget.CurrentLayoutIcon(scale=0.7)
            ],
            24
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules: List = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
