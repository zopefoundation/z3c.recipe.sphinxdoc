=========
 CHANGES
=========

1.1.0 (2017-07-05)
==================

- Add support for Python 3.4, 3.5 and 3.6 and PyPy.

- Remove support for Python 2.6 and 3.3.

- Change the default source suffix from ``.txt`` to ``.rst``. You can
  override this using the new ``extra-conf`` setting.

- Add the ability to specify arbitrary configuration in the
  ``extra-conf`` setting. This is useful for things like configuring
  extensions, overriding the defaults set by this recipe, and
  configuring a sphinx theme.

- Stop forcing a value of ``default.css`` for ``html_style`` even when
  the ``default.css`` setting is configured to an empty value. This
  makes it possible to use ``html_theme`` to set a sphinx theme, and
  it properly lets the default Sphinx theme be used (by setting both
  ``default.css`` and ``layout.html`` to empty values).

- Ignore bad eggs in the documentation working set. Previously they
  would raise internal errors without any explanation. Now, they log a
  warning pinpointing the bad egg. Fixes `issue 6
  <https://github.com/zopefoundation/z3c.recipe.sphinxdoc/issues/6>`_.


1.0.0 (2013-02-23)
==================

- Added Python 3.3 support.

- Bug: fix layout directory if layout is overriden by user

0.0.8 (2009-05-01)
==================

- Feature: Added new option `doc-eggs` which specifies the list of eggs for
  which to create documentation explicitely.

- Feature: Changed building behavior so that the documentation for each
  package is built in its own sub-directory.

- Feature: Added new option `extensions` which takes a whitespace
  separated list of sphinx extension modules. This extensions can be
  used to build the documentation.

0.0.7 (2009-02-15)
==================

- Bug: fix python 2.4 support

- Bug: fix broken srcDir path generation for windows

0.0.6 (2009-01-19)
==================

- Feature: Allow you to specify a url or local file path to your own
  default.css and layout.html files.

0.0.5 (2008-05-11)
==================

- Initial release.
