gaenv - Command line utility for managing appengine thirdparty packages
***********************************************************************

Install
=======

Simply run the following::

    $ python setup.py install

or `PyPi`_::

    $ pip install gaenv


Example Usage
=============

Note that this not run "pip install -r requirements.txt" so you'll have to run it manually first before running this::

    Create a requirements.txt and put all requirements then run
    $ gaenv
    For more
    $ gaenv -h
    or with python extracted source
    $ python gaenv-0.x.x/gaenv -h
    

This will create symbolic links from your default python version packages to
the current directory that you execute it on. By default it will create
gaenv_lib folder with all packages in your requirements.txt and will
ask you if you want this utility to insert the import statement that updates
your sys.path, or you can just do it manually.

Change log
==========

0.1.7

 * bug fix on git repo on requirements.txt
 * symlink fix for windows
 * added --no-import to skip auto import statement

0.1.6 (2013-09-03)

 * switched to appengine_config.py sys.path

0.1.5 (2013-06-25)

 * improved lookup using setuptools

0.1.4 (2013-06-15)

 * added run from source

0.1 (2013-06-13)


Links
=====
* `github.com`_ - source code
* `altlimit.com`_ - website

.. _github.com: https://github.com/faisalraja/gaenv
.. _PyPi: https://pypi.python.org/pypi/gaenv
.. _altlimit.com: http://www.altlimit.com