
# Object Oriented HTML Construction Toolkit        #
# Author: Pooya Eghbali - persian.writer@gmail.com #

class ElementStart(object):
    def __init__(self, tag, attributes = {}, id = None):
        self.tag = tag
        self.id = id
        self.attributes = attributes
        
    def addattributes(self, attributes):
        for opt in attributes:
            if opt in self.attributes:
                self.attributes[opt] += attributes[opt]
            else:
                self.attributes[opt] = attributes[opt]

class ElementSingleton(object):
    def __init__(self, tag, attributes = {}, id = None):
        self.tag = tag
        self.id = id
        self.attributes = attributes
        
    def addattributes(self, attributes):
        for opt in attributes:
            if opt in self.attributes:
                self.attributes[opt] += attributes[opt]
            else:
                self.attributes[opt] = attributes[opt]

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
        
    def open(self, tag, attributes = {}, id = None):
        self.elements += [ElementStart(tag, attributes, id)]
        return self
        
    def close(self, tag):
        self.elements += [ElementEnd(tag)]
        return self
    def raw(self, raw, id = None):
        self.elements += [ElementRaw(raw, id)]
        return self

    def single(self, tag, attributes = {}, id = None):
        self.elements += [ElementSingleton(tag, attributes, id)]
        return self
    
    def feed(self, *elems):
        self.elements += elems
        
    def getElementById(self, id):
        for item in self.elements:
            if hasattr(item, 'id') and item.id == id:
                return item

    def getElementsByattributes(self, attributes):
        for item in self.elements:
            if hasattr(item, 'attributes'):
                for opt in attributes:
                    if not opt in item.attributes: continue
                    if not all([val in item.attributes[opt]\
                                for val in attributes[opt]]): continue
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
                for attribute in elem.attributes:
                    output += ' %s = "%s"'%(attribute,
                                            ' '.join(elem.attributes[attribute]))
                output += ">\n"
                tabs += 1
            elif isinstance(elem, ElementSingleton):
                output += " "*4*tabs + '<%s'%elem.tag
                for attribute in elem.attributes:
                    output += ' %s = "%s"'%(attribute,
                                            ' '.join(elem.attributes[attribute]))
                output += "/>\n"
            elif isinstance(elem, ElementEnd):
                tabs -= 1
                output += " "*4*tabs + "</%s>\n"%elem.tag
            elif isinstance(elem, ElementRaw):
                output += " "*4*tabs + elem.value.replace('\n',
                                             " "*4*tabs + '\n') + '\n'
        return output

o,c,r,s = ElementStart, ElementEnd, ElementRaw, ElementSingleton
