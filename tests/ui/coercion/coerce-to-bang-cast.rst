tests/ui/coercion/coerce-to-bang-cast.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]

fn cast_a() {
    let y = {return; 22} as !;
    //~^ ERROR non-primitive cast
}

fn cast_b() {
    let y = 22 as !; //~ ERROR non-primitive cast
}

fn main() { }


