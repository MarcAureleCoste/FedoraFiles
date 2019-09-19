from libqtile.config import Key
from libqtile.command import lazy

from resources import MOD


keys = [
    # Switch between windows in current stack pane
    Key([MOD], 'j', lazy.layout.down()),
    Key([MOD], 'k', lazy.layout.up()),

    # Move windows up or down in current stack
    Key([MOD, 'control'], 'j', lazy.layout.shuffle_down()),
    Key([MOD, 'control'], 'k', lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([MOD], 'space', lazy.layout.next()),

    # Swap panes of split stack
    Key([MOD, 'shift'], 'space', lazy.layout.rotate()),

    # Toggle floating
    Key([MOD], "t", lazy.window.toggle_floating()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, 'shift'], 'Return', lazy.layout.toggle_split()),
    Key([MOD], 'Return', lazy.spawn('st')),

    # Toggle between different layouts as defined below
    Key([MOD], 'Tab', lazy.next_layout()),
    Key([MOD, 'shift'], 'Tab', lazy.prev_layout()),
    # Key([MOD], '-', lazy.layout.increase_ratio()),
    # Key([MOD], '=', lazy.layout.decrease_ratio()),
    Key([MOD], 'w', lazy.window.kill()),

    # Lock screen
    Key([MOD], 'l', lazy.spawn('lockscreen')),

    Key([MOD, 'control'], 'r', lazy.restart()),
    Key([MOD, 'control'], 'q', lazy.shutdown()),
    Key([MOD], 'p', lazy.spawncmd()),

    # Launch applications
    Key([MOD], 'c', lazy.spawn('code')),
    Key([MOD], 'f', lazy.spawn('firefox')),
    Key([MOD], 'g', lazy.spawn('google-chrome')),
    Key([MOD], 'm', lazy.spawn('spotify')),

    Key([MOD], 's', lazy.spawn("prtscr-select")),
    Key([MOD, 'shift'], 's', lazy.spawn("prtscr-full")),

    # Volume
    Key([], 'XF86AudioMute', lazy.spawn('amixer -q set Master toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -q sset Master 5%+ unmute')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -q sset Master 5%- unmute')),
]
