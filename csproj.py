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
    folder = folder.replace('/', '\\')
    for path in files:
        name = os.path.basename(path)
        path = path.replace(root, '')
        path = path.replace('/', '\\')
        if name.endswith('.xaml.cs'):
            line = '<Compile Include="$(MSBuildThisFileDirectory)%s%s">' % (folder, path)
            lines.append(line)
            line = '  <DependentUpon>%s</DependentUpon>' % name.replace('.cs', '')
            lines.append(line)
            line = '</Compile>'
            lines.append(line)
        else:
            line = '<Compile Include="$(MSBuildThisFileDirectory)%s%s" />' % (folder, path)
            lines.append(line)
    return lines


def _embedded_resource_include(folder, ext):
    lines = []
    root = os.path.abspath(folder)
    silp.term.info('Adding files to embedded resource include: %s' % root)
    files = [os.path.join(dirpath, f)
             for dirpath, dirnames, files in os.walk(root)
             for f in files if f.endswith(ext)]
    folder = folder.replace('/', '\\')
    for path in files:
        path = path.replace(root, '')
        path = path.replace('/', '\\')
        line = '<EmbeddedResource Include="$(MSBuildThisFileDirectory)%s%s" />' % (folder, path)
        lines.append(line)
    return lines


def xaml_include(folder):
    return _embedded_resource_include(folder, ".xaml")


def html_include(folder):
    return _embedded_resource_include(folder, ".html")

