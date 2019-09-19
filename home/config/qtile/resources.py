MOD = "mod4"

# Colors
COLORS = {
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
FA_ICONS = {
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
    'python': '',
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
