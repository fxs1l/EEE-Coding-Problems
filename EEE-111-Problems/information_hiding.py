

def make_class(attrs, base=None):
    def make_instance(cls):
        def bind(val, instance):
            if callable(val):
                def method(*args):
                    return val(instance, *args)

                return method
            
            return val

        def get_v(attr_name):
            if attr_name in attrs:
                return attrs[attr_name]
            val = cls['get'](attr_name)
            return bind(val, instance)

        def set_v(attr_name, val):
            attrs[attr_name] = val
        
        # FIXME: Edit set_protected to set attr_name as protected.
        #        This is the only "helping" stub you are given.
        #        You are on your own now.
        def set_protected(attr_name):
            if attr_name in attrs:
                protected[attr_name] = get_v(attr_name)
            else:
                set_v(attr_name, None)

        # TIP: One of the possible solutions is to create or use another
        #      instance dictionary that has the protected attributes
        #      and somehow inject it via the bind() call in the get()
        #      method. This means that you may need to add or amend more
        #      stuff than the ones given in this function.
        #
        #      Feel free to change this make_instance() function in any way
        #      as long as the dictionary returned by this function has
        #      the three methods get(), set(), and set_protected().
        
        attrs = {}
        protected = {}
        instance = {
            'get': get_v,
            'set': set_v,
            'set_protected': set_protected,
        }

        return instance

    # PS. Please do not edit anything below this comment to make your life
    #     easier. :)
    def init(cls, *args):
        obj = make_instance(cls)
        init_m = cls['get']('__init__')

        if init_m:
            init_m(obj, *args)

        return obj

    def get_a(attr_name):
        if attr_name == 'super':
            return base
        elif attr_name in attrs:
            return attrs[attr_name]
        elif base is not None:
            return base['get'](attr_name)
        else:
              return None

    def set_a(attr_name, val):
        attrs[attr_name] = val

    def new_o(*args):
        return init(cls, *args)

    cls = {
        'get': get_a,
        'set': set_a,
        'new': new_o,
    }

    return cls

def main():
    print('hooray!')

if __name__ == '__main__':
    main()
