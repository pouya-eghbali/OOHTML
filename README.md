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

    >>> R = r('Hello World', 'message') #a raw element with id 'message'
    >>> O = o('div', {}, 'menu')        #opening element with id 'menu'
    >>> S = s('img', {}, 'bg')          #singleton with id 'bg'
    >>> C.feed(R)
    >>> C.getElementById('message')
    >>> C.removeElementById('message')
    
You can insert a Constructor object inside another Constructor::

    >>> sampleConstructor = Constructor()
    >>> C.addAfterId('sampleID', sampleConstructor)

There are numerous methods for accessing elements and changing its data::

    >>> C.getElementById('message').value          #Raw elements use .value to store their data
    >>> C.getElementById('sample').attributes      #Opening and Singleton elements have .attribute
    >>> C.getElementById('sample').tag             #Opening, Closing & Singleton elements have .tag
    >>> C.getElementById('sample').id              #All elements have .id

Opening and Singleton Elements can have attributes::

    >>> div = o('div', {'class':['message', 'floater']}, 'contents')
    >>> C.feed(div)
    >>> div.addAtributes({'id': ['sample']})

You can use this attributes to select elements::

    >>> C.getElementsByAttributes({'class': ['test']})    #This returns a generator
    
To show you an example::

    >>> from OOHTML import *
    >>> C = Constructor()
     
    >>> C.feed(o('html'),
             o('head'),
               o('script', {'type': ['text/javascript'], 'src':['script.js']}),
               c('script'),
               o('style', {'type': ['text/css'], 'src':['style.css']}),
               c('style'),
             c('head'),
             o('body'),
               o('div', {'class':['message']}),
                 r('Hello World!!!', 'message'),
                 s('img', {'alt': ['Hello'], 'src':['img.jpeg']}),
               c('div'),
               o('div', {'class':['message', 'floater']}, 'contents'), c('div'),
             c('body'),
           c('html'))
           
    >>> C.getElementById('message').value = "HTML CONSTRUCTOR!!!"
    >>> C.addAfterId('contents', Constructor().open('div').raw('OOHTML').single('br').close('div'))
    >>> print(C.render())

The above outputs::

    <html>
        <head>
            <script type = "text/javascript" src = "script.js">
            </script>
            <style type = "text/css" src = "style.css">
            </style>
        </head>
        <body>
            <div class = "message">
                HTML CONSTRUCTOR!!!
                <img src = "img.jpeg" alt = "Hello"/>
            </div>
            <div class = "message floater">
                <div>
                    OOHTML
                    <br/>
                </div>
            </div>
        </body>
    </html>

Explore source code for more info.

Download
========

Download package from here: https://pypi.python.org/pypi/OOHTML or simply install with pip install OOHTML

Project Info
============

Github project page: https://github.com/pooya-eghbali/OOHTML
PyPi: https://pypi.python.org/pypi/OOHTML
Mail me at: persian.writer [at] Gmail.com
