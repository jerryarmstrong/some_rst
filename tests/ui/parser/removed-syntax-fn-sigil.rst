tests/ui/parser/removed-syntax-fn-sigil.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: fn~() = || (); //~ ERROR expected `(`, found `~`
}


