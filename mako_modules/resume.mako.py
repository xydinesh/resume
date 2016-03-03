# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457025494.823
_enable_loop = True
_template_filename = 'resume.mako'
_template_uri = 'resume.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'{\r\n  "basics": { ')
        runtime._include_file(context, u'basic.json', _template_uri)
        __M_writer(u'\r\n  },\r\n  "work": [],\r\n  "volunteer": [],\r\n  "education": [],\r\n  "awards": [],\r\n  "skills": [],\r\n  "publications": [],\r\n  "languages": [],\r\n  "interests": [],\r\n  "references": []\r\n}\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "29": 23, "21": 1, "22": 2, "23": 2}, "uri": "resume.mako", "filename": "resume.mako"}
__M_END_METADATA
"""
