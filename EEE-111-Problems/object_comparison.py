import uuid
import random

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
                # Object attribute
                return attrs[attr_name]

            # Class attribute
            val = cls['get'](attr_name)
            return bind(val, instance)

        def set_v(attr_name, val):
            attrs[attr_name] = val
            
        def get_uuid():
            return uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)

        # FIXME: Edit `get_hash()` to return hash of object
        def get_hash():
            return get_v("hashcode")

        # FIXME: Edit `is_same(other)` to return whether this object is the
        #        same as other
        def is_same(other):
            if get_hash() == other['hash']():
                return True
            return False

        # FIXME: Edit `clone_o()` to return the clone of this object
        def clone_o():
            return instance

            # FIXME: Generate a hash for this function using the `get_uuid()` function
        hashcode = get_uuid()
        #return None
   
        # FIXME: Edit the instance dictionary to add `hash`, `is_same` and `clone`
        #        functions
        attrs = {
            'hashcode': hashcode,
        }
        instance = {
            'get': get_v,
            'set': set_v,
            'hash': get_hash,
            'is_same': is_same,
            'clone': clone_o,
        }

        return instance

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

    def set_a(attr_name, val):
        attrs[attr_name] = val

    def new_o(*args):
        return init(cls, *args)
    
    random.seed('EEE111')

    cls = {
        'get': get_a,
        'set': set_a,
        'new': new_o,
    }

    return cls

# Don't edit anything below this to make your life easier. :)
def main():
    def DynamicClassFactoryMaker(fun_name, props_dict):
        def f():
            def __init__(self):
                for prop_name, (prop_val, is_get, is_set) in props_dict.items():
                    self['set'](prop_name, prop_val)
                    self['modify'](prop_name, is_get, is_set)
            
            return make_class(locals())
            
        f.__name__ = fun_name
        return f
        
    n_testcases = int(input())

    for t in range(n_testcases):
        obj_dict = {}

        n_commands = int(input())
        class_name = input()
        
        DynamicClassFactory = DynamicClassFactoryMaker(class_name, {})
        DynamicClass = DynamicClassFactory()

        print(f'Case #{t + 1}:')
        
        for _ in range(n_commands):
            cmd_line = input().split()

            if cmd_line[0] == 'create':
                obj_name = cmd_line[1]

                class_obj = DynamicClass['new']()
                obj_dict[obj_name] = class_obj
            elif cmd_line[0] == 'hash':
                obj_name = cmd_line[1]

                print(obj_dict[obj_name]['hash']())
            elif cmd_line[0] == 'clone':
                a, b = cmd_line[1:]

                obj_dict[b] = obj_dict[a]['clone']()
            elif cmd_line[0] == 'is_equal':
                a, b = cmd_line[1:]
                print(obj_dict[a]['is_same'](obj_dict[b]))

if __name__ == '__main__':
    main()
