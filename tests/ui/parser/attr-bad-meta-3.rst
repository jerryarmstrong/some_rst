tests/ui/parser/attr-bad-meta-3.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[path() token] //~ ERROR expected `]`, found `token`
mod m {}


