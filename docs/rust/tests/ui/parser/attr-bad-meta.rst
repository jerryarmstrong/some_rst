tests/ui/parser/attr-bad-meta.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[path*] //~ ERROR expected one of `(`, `::`, `=`, `[`, `]`, or `{`, found `*`
mod m {}


