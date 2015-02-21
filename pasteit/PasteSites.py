import requests
import sys

class NotSupported(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class PasteSite:

    def __init__(self, url):
        self.url       = url
        self.paste_url = None
        self.data      = None

    @staticmethod
    def siteFactory(site_name):
        if site_name == 'slexy.org':
            return Slexy()
        elif site_name == 'pastebin.mozilla.org':
            return Mozilla()
        else:
            raise NotSupported("This site is not supported")

    def parse(self, args):
        """ Internal method used by the PasteSite class.
        Returns a dictionary of the parsed input arguments.

        Parses the arguments given at the command line.
        Many pastebin like sites use different arguments
        for the paste so this method should be implemented
        for each subclass of PasteSite.

        See the slexy class for an example of how to implement
        this method for subclasses.
        """
        self.data = args

    def paste(self):
        """Posts the data to the paste site.

        This method tries to post the data to the paste site.
        If the resulting request does not have a ok status the
        program exits else we return the resulting paste url.
        The method assumes that the data is in a dictionary.
        """
        if self.data == None:
            print('You can only paste after a parse')
            sys.exit(-1)
        res = requests.post(self.url, self.data)
        if not res.ok:
            print('Bad response {0} {1}'.format(res.reason, res.status_code))
            sys.exit(-1)

        self.paste_url = res.url



class Slexy(PasteSite):

    def __init__(self):
        super(Slexy, self).__init__('http://slexy.org/submit')

    def parse(self, args):
        form_data = {}
        arg_translation = {'text'             : 'raw_paste',
                           'syntax_highlight' : 'language',
                           'expiration'       : 'expire',
                           'comment'          : 'comment',
                           'description'      : 'descr',
                           'visibility'       : 'permissions',
                           'linum'            : 'linenumbers'}
        for k,v in args.items():
            if arg_translation.get(k):
                form_data[arg_translation[k]] =  v
        form_data['submit'] = 'Submit Paste'

        self.data = form_data

class Mozilla(PasteSite):
    def __init__(self):
        super(Mozilla, self).__init__('https://pastebin.mozilla.org')

    def parse(self, args):
        form_data = {}
        arg_translation = {'text'             : 'code2',
                           'expiration'       : 'expiry',
                           'syntax_highlight' : 'format',
                           'author'           : 'poster'}
        for k,v in args.items():
            if arg_translation.get(k):
                form_data[arg_translation[k]] = v
        form_data['paste'] = 'Send'
        form_data['parent_pid'] = ''

        self.data = form_data
