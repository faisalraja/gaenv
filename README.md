**gaenv** - Command line utility for managing appengine thirdparty packages

Installation::

    $ sudo pip install gaenv

Or download directly at [PyPI](https://pypi.python.org/pypi/gaenv)


Example Usage::

    Create a requirements.txt and put all requirements then run
    $ gaenv
    For more
    $ gaenv -h
    or with python extracted source
    python gaenv-0.x.x/ggaenv -h
    
Note that this not run "pip install -r requirements.txt" so you'll have to run it manually first before running this.


This will create symbolic links from your default python version packages to
the current directory that you execute it on. By default it will create
gaenv_lib folder with all packages in your requirements.txt and will
ask you if you want this utility to insert the import statement that updates
your sys.path, or you can just do it manually.

If you have questions/suggestions you can contact me at [contact form here](http://www.altlimit.com)