##############################################################################
#
# Copyright (c) 2017 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import shutil
import subprocess
import sys
import tempfile
import os
import unittest

from zc.buildout.testing import Buildout

from z3c.recipe import sphinxdoc

EMPTY_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '__init__.py',
    )
)

class TestZopeOrgSetup(unittest.TestCase):

    def setUp(self):
        self.here = os.getcwd()
        self.tmpdir = tempfile.mkdtemp('.sphinxdoctests')
        os.chdir(self.tmpdir)
        os.mkdir('bin')

    def tearDown(self):
        os.chdir(self.here)
        shutil.rmtree(self.tmpdir)

    def _makeOne(self, name='docs', options=None):
        opts = {
            'doc-eggs': 'z3c.recipe.sphinxdoc',
            'eggs': 'z3c.recipe.sphinxdoc'
        }
        if options:
            opts.update(options)
        buildout = Buildout()

        docs = sphinxdoc.ZopeOrgSetup(buildout, name, opts)
        return docs, buildout

    @property
    def part_path(self):
        return os.path.join('parts', 'docs', 'z3c.recipe.sphinxdoc')

    @property
    def templates_path(self):
        return os.path.join(self.part_path, '.templates')

    @property
    def static_path(self):
        return os.path.join(self.part_path, '.static')

    def _check_conf_py_can_be_evald(self):
        args = [sys.executable,
                '-c',
                'import sys; sys.path.insert(0, "%s"); import conf' % self.part_path]
        subprocess.check_call(args)

    def _read_conf_file(self):
        conf_path = os.path.join(self.part_path, 'conf.py')
        with open(conf_path, 'r') as f:
            conf = f.read()
        return conf

    def test_construct_sets_script(self):
        docs, buildout = self._makeOne()
        self.assertEqual(docs.options['script'],
                         os.path.join(buildout['buildout']['bin-directory'], 'docs'))

    def test_openfile_falls_to_url(self):
        docs, _ = self._makeOne()
        self.assertRaises(IOError,
                          docs.openfile, 'file:///')

    def test_basic_install(self):
        docs, _ = self._makeOne()
        docs.install()
        self._check_conf_py_can_be_evald()
        conf = self._read_conf_file()

        self.assertIn(os.path.abspath(self.templates_path), conf)
        self.assertIn(os.path.abspath(self.static_path), conf)

        script_path = os.path.join('bin', docs.name)
        with open(script_path, 'r') as f:
            script = f.read()
        self.assertIn("sys.exit(z3c.recipe.sphinxdoc.main({'z3c.recipe.sphinxdoc':",
                      script)

        # Go ahead and generate it, or at least try to, it shouldn't fail, even though there's no
        # index.rst
        subprocess.check_call('bin/docs')

        # likewise, we can directly try to do it and it doesn't raise an exception
        sphinxdoc.main(docs._projectsData, argv=['docs', '-W'])

        # We can add another entry to the projectsData and we still don't raise anything
        projects = dict(docs._projectsData)
        projects['another'] = projects['z3c.recipe.sphinxdoc']
        projects['another'][0] = '-W'

        sphinxdoc.main(docs._projectsData, argv=['docs'], exit_on_error=True)

    def test_override_css(self):
        docs, _ = self._makeOne(options={'default.css': EMPTY_FILE})
        docs.install()

        css_path = os.path.join(self.static_path, 'default.css')
        with open(css_path, 'r') as f:
            css = f.read()
            self.assertEqual(css, '')

    def test_override_layout(self):
        docs, _ = self._makeOne(options={'layout.html': EMPTY_FILE})
        docs.install()

        html_path = os.path.join(self.templates_path, 'layout.html')
        with open(html_path, 'r') as f:
            html = f.read()
            self.assertEqual(html, '')

    def test_extra_conf(self):
        import textwrap
        docs, _ = self._makeOne(options={
            'extra-conf': textwrap.dedent("""\
            autodoc_default_flags = ['members', 'show-inheritance',]
            autoclass_content = 'both'
            intersphinx_mapping = {
            'python':  ('http://docs.python.org/2.7/', None),
            'boto': ('http://boto.readthedocs.org/en/latest/', None),
            'gunicorn': ('http://docs.gunicorn.org/en/latest/', None),
            'pyquery': ('http://packages.python.org/pyquery/', None) }
            intersphinx_cache_limit = -1
            """
            )
        })
        docs.install()
        self._check_conf_py_can_be_evald()
        conf = self._read_conf_file()
        self.assertIn('intersphinx_mapping', conf)
