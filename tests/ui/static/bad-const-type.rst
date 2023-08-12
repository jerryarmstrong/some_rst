tests/ui/static/bad-const-type.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static i: String = 10;
//~^ ERROR mismatched types
//~| expected struct `String`, found integer
fn main() { println!("{}", i); }


