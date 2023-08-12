tests/ui/usize-generic-argument-parent.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let x: usize<foo>; //~ ERROR const arguments are not allowed on builtin type `usize`
}

fn main() {}


