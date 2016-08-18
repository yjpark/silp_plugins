# -*- coding: utf8 -*-

import silp

import os
import sys

def compile_include(folder):
    lines = []
    root = os.path.abspath(folder)
    silp.term.info('Adding files to compile include: %s' % root)
    files = [os.path.join(dirpath, f)
             for dirpath, dirnames, files in os.walk(root)
             for f in files if f.endswith(".cs")]
    for path in files:
        path = path.replace(root, '')
        path = path.replace('/', '\\')
        line = '<Compile Include="%s%s" />' % (folder, path)
        lines.append(line)
    return lines

