# OOHTML
Object Oriented HTML Construction Toolkit for Python

Simple Usage
============

you can construct HTML in two ways, first with feeding the Constructor::

    >>> from OOHTML import *
    >>> C = Constructor()
    >>> C.feed([o('html'),                 #open HTML tag
                 o('head'),                #open Head
                 c('head'),                #close Head
                 o('body'),
                   o('div'),
                     r('Hello World!'),    #raw content
                     s('area'),            #singleton (self closing element)
                   c('div'),
                 c('body'),
                c('html')])

Or using class methods, the above example can be rewriten as::

    >>> from OOHTML import *
    >>> C = Constructor()
    >>> C.open('html').open('head').close('head').open('body')
    >>> C.open('div').raw('Hello World!').single('area').close('div')
    >>> C.close('body').close('html')

to render the constructor as html, you can use render() method::

    >>> C.render()

Each of opening, singleton or raw elements can have an id (not the HTML ID of the element) so they can be accessible::

    >>> r = ('Hello World', 'message') #a raw element with id 'message'
    >>> C.feed(r)
    >>> C.getElementById('message')

There are numerous methods for accessing elements and changing its data::

    >>> C.getEle

Explore source code for more info.

Download
========

Download package from here: https://pypi.python.org/pypi/OOHTML or simply install with pip install OOHTML

Project Info
============

Github project page: https://github.com/pooya-eghbali/OOHTML
PyPi: https://pypi.python.org/pypi/OOHTML
Mail me at: persian.writer [at] Gmail.com
