
# Object Oriented HTML Construction Toolkit        #
# Author: Pooya Eghbali - persian.writer@gmail.com #

class ElementStart(object):
    def __init__(self, tag, options = {}, id = None):
        self.tag = tag
        self.id = id
        self.options = options
        
    def addOptions(self, options, value):
        for opt in options:
            if opt in self.options:
                self.options[opt] += options[opt]
            else:
                self.options[opt] = value

class ElementSingleton(object):
    def __init__(self, tag, options = {}, id = None):
        self.tag = tag
        self.id = id
        self.options = options
        
    def addOptions(self, options, value):
        for opt in options:
            if opt in self.options:
                self.options[opt] += options[opt]
            else:
                self.options[opt] = value

class ElementEnd(object):
    def __init__(self, tag):
        self.tag = tag

class ElementRaw(object):
    def __init__(self, value, id = None):
        self.value = value
        self.id = id

class Constructor(object):
    def __init__(self):
        self.elements = []
        
    def open(self, tag, options = {}, id = None):
        self.elements += [ElementStart(tag, options, id)]
        return self
        
    def close(self, tag):
        self.elements += [ElementEnd(tag)]
        return self
    def raw(self, raw, id = None):
        self.elements += [ElementRaw(raw, id)]
        return self

    def single(self, tag, options = {}, id = None):
        self.elements += [ElementSingleton(tag, options, id)]
        return self
    
    def feed(self, *elems):
        self.elements += elems
        
    def getElementById(self, id):
        for item in self.elements:
            if hasattr(item, 'id') and item.id == id:
                return item

    def getElementsByOptions(self, options):
        for item in self.elements:
            if hasattr(item, 'options'):
                for opt in options:
                    if not opt in item.options: continue
                    if not all([val in item.options[opt]\
                                for val in options[opt]]): continue
                    yield item
            
    def removeElementById(self, id):
        for index, item in enumerate(self.elements):
            if hasattr(item, 'id') and item.id == id:
                return self.elements.pop(index)
                
    def addAfterId(self, id, constructor):
        for index, item in enumerate(self.elements):
            if hasattr(item, 'id') and item.id == id:
                self.elements = self.elements[:index+1] + \
                                constructor.elements    + \
                                self.elements[index+1:]
    def render(self):
        output = ""
        tabs = 0
        for elem in self.elements:
            if isinstance(elem, ElementStart):
                output += " "*4*tabs + '<%s'%elem.tag
                for option in elem.options:
                    output += ' %s = "%s"'%(option,
                                            ' '.join(elem.options[option]))
                output += ">\n"
                tabs += 1
            elif isinstance(elem, ElementSingleton):
                output += " "*4*tabs + '<%s'%elem.tag
                for option in elem.options:
                    output += ' %s = "%s"'%(option,
                                            ' '.join(elem.options[option]))
                output += "/>\n"
            elif isinstance(elem, ElementEnd):
                tabs -= 1
                output += " "*4*tabs + "</%s>\n"%elem.tag
            elif isinstance(elem, ElementRaw):
                output += " "*4*tabs + elem.value.replace('\n',
                                             " "*4*tabs + '\n') + '\n'
        return output

o,c,r,s = ElementStart, ElementEnd, ElementRaw, ElementSingleton
