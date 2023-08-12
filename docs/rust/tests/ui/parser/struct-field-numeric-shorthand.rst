tests/ui/parser/struct-field-numeric-shorthand.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Rgb(u8, u8, u8);

fn main() {
    let _ = Rgb { 0, 1, 2 };
    //~^ ERROR expected identifier, found `0`
    //~| ERROR expected identifier, found `1`
    //~| ERROR expected identifier, found `2`
    //~| ERROR missing fields `0`, `1` and `2` in initializer of `Rgb`
}


