# Copright (C) 2015 Eric Skoglund
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see http://www.gnu.org/licenses/gpl-2.0.html

#!/usr/bin/env/ python3

import argparse
import os
import requests
import sys

from . import PasteSites

class _ListAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest='==SUPRESS==',
                 default='==SUPRESS==',
                 help=None):
        super(_ListAction, self).__init__(option_strings=option_strings,
                                        dest=dest,
                                        default=default,
                                        nargs=0,
                                        help=help)
    def __call__(self, parser, namespace, values, option_strins=None):
        self.__list()
        parser.exit()

    def __list(self):
        sites = ['slexy.org','pastebin.mozilla.org']
        for site in sites:
            print(site)


def __get_arguments():
    parser  = argparse.ArgumentParser(prog='pasteit', description='Paste files to paste sites.')
    parser.add_argument('file', metavar='FILE', type=str, help='the file that you want pasted.')
    parser.add_argument('-s', '--site', metavar="pastesite", default='slexy.org',
                        help='''The site you want to paste to, default is slexy.org.
                        Use 'pasteit --list' to show a list of supported sites.''')
    parser.add_argument('-l', '--language', help='What syntax highlighting to use')
    parser.add_argument('-a', '--author', help='Name of the author')
    parser.add_argument('--list', help='Prints a list of supported sites and exits' ,action=_ListAction)

    return parser.parse_args()


def __read_file(filename):
    try:
        f = open(filename)
    except IOError as e:
        print('Unable to open file {0}: {1}'.format(filename, e.strerror))
        sys.exit(-1)

    return f.read()


def __print_not_supported():
    print('''This website is not supported. Use `pasteit --list` to see a list of supported website.
If you want this site to be supported please visit http://github.com/ErioIO/pasteit and open a ticket.''')


def __main():
    args = vars(__get_arguments())

    try:
        site = PasteSites.PasteSite.siteFactory(args.get('site'))
    except PasteSites.NotSupported:
        __print_not_supported()
        sys.exit(-1)

    args['text'] = __read_file(args.get('file'))

    site.parse(args)
    url = site.paste()

    if site.paste_url:
        print(site.paste_url)
        return 1
    else:
        print('Unable to paste text')
        return -1


if __name__ == '__main__':
    sys.exit(__main())
