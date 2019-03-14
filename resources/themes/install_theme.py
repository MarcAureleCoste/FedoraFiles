#!/usr/bin/python3
import os
import shutil
import argparse
import fileinput

from typing import Optional


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Tool to manage your theme (GTK3)',
        epilog='This tool is just an helper install theme by yourself with `tar xf archive/<theme> .` and by editing your gtk settings file.'
    )
    parser.add_argument('-c', dest='clear', action='store_true', help='Clear already installed theme.')
    parser.add_argument('-e', dest='edit', action='store_true', help='Edit your gtk3 settings.ini file.')
    parser.add_argument('name', type=str, help='The name of the theme (archive name without extension).')
    return parser


def clear_themes() -> None:
    root_path = os.path.dirname(__file__)
    for e in os.listdir(root_path):
        if e != 'archives' and os.path.isdir(os.path.join(root_path, e)):
            shutil.rmtree(os.path.join(root_path, e))


def edit_gtk_settings(theme_name) -> None:
    settings_path = os.path.join(
        os.environ['HOME'],
        '.config/gtk-3.0/settings.ini'
    )
    with fileinput.FileInput(settings_path, inplace=True) as settings_file:
        for line in settings_file:
            if line.startswith('gtk-theme-name'):
                line = f'gtk-theme-name = {theme_name}'
            print(line, end='')


def find_archive(archives_path: str, name: str) -> Optional[str]:
    themes = []
    for theme in os.listdir(archives_path):
        if os.path.isfile(os.path.join(archives_path, theme)):
            t_data = theme.split('.')
            t_name = t_data[0]
            t_ext = '.'.join(t_data[1:])
            if t_name == name:
                return os.path.join(archives_path, f'{t_name}.{t_ext}')
    return None


def install_theme(args):
    if args.clear:
        clear_themes()
    extract_path = os.path.dirname(__file__)
    archives_path = os.path.join(extract_path, 'archives')
    archive = find_archive(archives_path, args.name)
    if archive:
        shutil.unpack_archive(
            archive,
            extract_dir=extract_path
        )
    if args.edit:
        edit_gtk_settings(args.name)


if __name__ == '__main__':
    args = get_parser().parse_args()
    install_theme(args)

