import argparse
import os
import requests
import sys

import PasteSites

NOT_SUPPORTED_MSG = '''That site is not supported yet. 
Please visit http://www.github.com/EricIO/pasteit and open a ticket for your site'''

def __get_arguments():
    parser  = argparse.ArgumentParser(prog='pasteit', description='Paste files to paste sites.')
    parser.add_argument('file', metavar='FILE', type=str, help='the file that you want pasted.')
    parser.add_argument('-s', '--site', metavar="pastesite", default='slexy.org',
                        help='''The site you want to paste to, default is slexy.org. 
                        Use 'pasteit --list' to show a list of supported sites.''')

    return parser.parse_args()

def __main():
    
    args = __get_arguments()
    try:
        site = PasteSites.PasteSite.siteFactory(args.site, args)
    except PasteSites.NotSupported:
        print(NOT_SUPPORTED_MSG)
        sys.exit(-1)

    site.parse(vars(args))
    url = site.paste()

    print("sadf")

    return url


if __name__ == '__main__':
    sys.exit(__main())
