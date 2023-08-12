tests/ui/parser/removed-syntax-mode.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(+x: isize) {}
//~^ ERROR expected parameter name, found `+`

fn main() {}


