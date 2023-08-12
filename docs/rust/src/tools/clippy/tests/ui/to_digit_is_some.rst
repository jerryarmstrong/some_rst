src/tools/clippy/tests/ui/to_digit_is_some.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //run-rustfix

#![warn(clippy::to_digit_is_some)]

fn main() {
    let c = 'x';
    let d = &c;

    let _ = d.to_digit(8).is_some();
    let _ = char::to_digit(c, 8).is_some();
}


