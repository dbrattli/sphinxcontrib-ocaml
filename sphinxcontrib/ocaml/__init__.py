# coding: utf8

# Copyright 2017 Vincent Jacques <vincent@vincent-jacques.net>

"""
A `Sphinx <http://www.sphinx-doc.org>`_ extension providing an `OCaml`
`domain <http://www.sphinx-doc.org/en/stable/domains.html>`_
and `autodocumenters <>`_ for `OCaml` elements.
"""

from . import domain
from . import autodocumenters

# @todo A doctest-like extension


def setup(app):
    app.add_domain(domain.OCamlDomain)
    app.add_autodocumenter(autodocumenters.ModuleDocumenter)
    app.add_config_value("ocaml_autoocamldoc_executable", "autoocamldoc", "env")
    app.add_config_value("ocaml_source_directories", None, "env")
    app.add_config_value("ocaml_findlib_packages", [], "env")
    app.add_config_value("ocaml_include_directories", [], "env")
