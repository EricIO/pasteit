import setuptools

setuptools.setup(name = 'pasteit',
      version = '1.0.0',
      description = 'Program that allows you to paste files to pastebin like sites',
      url = 'http://github.com/ErioIO/pasteit',
      author = 'Eric Skoglund',
      author_email = 'eric@pagefault.se',
      license = 'GPLv3',
      packages = setuptools.find_packages(),
      install_requires = [
          'requests',
      ],
      entry_points = {
          'console_scripts' : ['pasteit = pasteit.pasteit:__main']})
