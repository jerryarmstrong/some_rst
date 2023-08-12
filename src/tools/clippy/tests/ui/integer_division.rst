src/tools/clippy/tests/ui/integer_division.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::integer_division)]

fn main() {
    let two = 2;
    let n = 1 / 2;
    let o = 1 / two;
    let p = two / 4;
    let x = 1. / 2.0;
}


