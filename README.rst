.. -*- mode: rst; coding: utf-8 -*-

======================================================================
gaenv - Command line utility for managing appengine thirdparty packages
======================================================================

:Authors: Faisal Raja <support@altlimit.com>
:Version: 0.1.1
:Date:    2013-06-14
:Code: http://github.com/faisalraja/gaenv


Overview
======================================================================
This will create symbolic links from your default python version packages to
the current directory that you execute it on. By default it will create
gaenv_lib folder with all packages in your requirements.txt and will
ask you if you want this utility to insert the import statement that updates
your sys.path, or you can just do it manually.


Installation
---------------
You need to have setuptools/easy_install installed. Installation
should be as easy as typing::

  easy_install gaenv
  or
  pip install gaenv


Example Usage::

  Create a requirements.txt and put all requirements then run
  $ gaenv
  For more
  $ gaenv -h
  Note that this not run "pip install -r requirements.txt" so you'll
  have to run it manually first before running this.


Contact
---------------
If you have any questions/suggestions you can email me at http://www.altlimit.com/contact


Change-Log
======================================================================
2013-06-14	Initial release 0.1
-----------------------------------------------

LICENSE
======================================================================
MIT