tests/ui/hygiene/pattern-macro.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo { () => ( x ) }

fn main() {
    let foo!() = 2;
    x + 1; //~ ERROR cannot find value `x` in this scope
}


