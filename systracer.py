import sys
from beeprint import pp

class SetTrace(object):
    def __init__(self, func, condition=lambda file_name, func_name, line_no: True, skip_condition=True, path_to_save="./"):
        self.func = func
        self.traced_lines = []
        self.path_to_save = path_to_save
        self.func.__defaults__ = (self.traced_lines, condition, skip_condition,)

    def __enter__(self):
        sys.settrace(self.func)
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.settrace(None)
        import json
        with open(self.path_to_save, 'w') as stl:
            json.dump(self.traced_lines, stl)

def print_frame(f, limit=160):
    attrs = [attr for attr in dir(f) if not attr.startswith('__')]
    for attr in attrs:
        info = repr(getattr(f, attr))
        print("%s: %s" % (attr, info[:limit]))
    print()
          
def tracer(frame, event, arg, traced_lines=None, condition=None, skip_condition=False):
    co = frame.f_code
    file_name = co.co_filename
    func_name = co.co_name
    line_no = frame.f_lineno

    if condition(file_name, func_name, line_no) and not skip_condition:
        return
    
    #print('%s line %s event %s ' % (func_name, line_no, event))
    trace = []
    for f in frame.f_locals:
        try:
            trace.append((f, pp(frame.f_locals[f], output=False)))
        except:
            trace.append((f, str(frame.f_locals[f])))
    traced_lines.append((func_name, line_no, event, file_name, trace))
    return tracer
        