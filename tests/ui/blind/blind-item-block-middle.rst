tests/ui/blind/blind-item-block-middle.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_camel_case_types)]

mod foo { pub struct bar; }

fn main() {
    let bar = 5;
    //~^ ERROR mismatched types
    use foo::bar;
}


