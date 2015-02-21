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

    @staticmethod
    def siteFactory(site_name):
        if site_name == 'slexy.org':
            return Slexy()
        else:
            raise NotSupported("This site is not supported")

    def __parse(self, args):
        """ Internal method used by the PasteSite class
        Returns a dictionary of the parsed input arguments.

        Parses the arguments given at the command line.
        Many pastebin like sites use different arguments
        for the paste so this method should be implemented
        for each subclass of PasteSite. 

        See the slexy class for an example of how to implement 
        this method for subclasses.
        """
        return args
        
    def paste(self, data):
        """Posts the data to the paste site.

        This method tries to post the data to the paste site.
        If the resulting request does not have a ok status the 
        program exits else we return the resulting paste url.
        The method assumes that the data is in a dictionary.
        """
        res = requests.post(self.url, data = form_data)
        if not res.ok:
            print('Bad response {0} {1}'.format(res.reason, res.status_code))
            sys.exit(-1)

        return res.url



class Slexy(PasteSite):

    def __init__(self, args):
        super().__init__('http://slexy.org/submit', translate(args))
    
    arg_translation = {'text' : 'raw_paste','syntax_highlight' : 'language', 'expire' : 'expire'}

    def translate(args):
        return args
