tests/ui/linkage-attr/linkage2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(linkage)]

extern "C" {
    #[linkage = "extern_weak"]
    static foo: i32;
//~^ ERROR: invalid type for variable with `#[linkage]` attribute
}

fn main() {
    println!("{}", unsafe { foo });
}


