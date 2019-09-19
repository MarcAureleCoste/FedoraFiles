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
from typing import List

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget

from keys import keys
from layouts import layouts, floating_layout, mouse
from resources import MOD, COLORS, FA_ICONS, wmname


groups_data = [
    {
        'label': FA_ICONS['fedora'],
        'name': '1',
        'matches': [Match(wm_class=['Slack', 'bitwarden']),]
    },
    {
        'label': FA_ICONS['globe-africa'],
        'name': '2',
        'matches': [Match(wm_class=['Firefox Developer Edition']),]
    },
    {
        'label': FA_ICONS['terminal'],
        'name': '3',
        'matches': None
    },
    {
        'label': FA_ICONS['code'],
        'name': '4',
        'matches': [Match(wm_class=['Visual Studio Code']),],
    },
    {
        'label': FA_ICONS['video'],
        'name': '5',
        'matches': None
    },
    {
        'label': FA_ICONS['steam'],
        'name': '6',
        'matches': [Match(wm_class=['Steam'], role=['game']),],
    },
    {
        'label': FA_ICONS['windows'],
        'name': '7',
        'matches': [Match(wm_class=['qemu']),],
    },
    {
        'label': FA_ICONS['random'],
        'name': '0',
        'matches': [Match(wm_class=['google-chrome', 'pavucontrol']),]
    }
]

groups = [Group(name=i['name'], label=i['label'], matches=i['matches']) for i in groups_data]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([MOD], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([MOD, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

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
                widget.TextBox(FA_ICONS['wifi'], foreground=COLORS['n_green']),
                widget.Net(interface='wlp59s0', foreground=COLORS['n_green']),
                widget.TextBox(FA_ICONS['microchip'], foreground=COLORS['n_yellow']),
                widget.CPUGraph(frequency=2, graph_color=COLORS['n_yellow'], line_width=1),
                widget.TextBox(FA_ICONS['memory'], foreground=COLORS['n_blue']),
                widget.MemoryGraph(frequency=2, graph_color=COLORS['n_blue'], line_width=1),
                widget.TextBox(FA_ICONS['battery-full'], foreground=COLORS['n_magenta']),
                widget.Battery(foreground=COLORS['n_magenta']),
                widget.Sep(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=COLORS['n_cyan']),
                widget.Systray(),
                widget.Sep(),
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
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=COLORS['n_cyan']),
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
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=COLORS['n_cyan']),
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
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', foreground=COLORS['n_cyan']),
                widget.CurrentLayoutIcon(scale=0.7)
            ],
            24
        )
    ),
]

dgroups_key_binder = None
dgroups_app_rules: List = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
