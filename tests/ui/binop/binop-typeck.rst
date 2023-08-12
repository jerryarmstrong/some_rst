tests/ui/binop/binop-typeck.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #500

fn main() {
    let x = true;
    let y = 1;
    let z = x + y;
    //~^ ERROR cannot add `{integer}` to `bool`
}


