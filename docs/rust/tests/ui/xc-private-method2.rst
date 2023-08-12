tests/ui/xc-private-method2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:xc-private-method-lib.rs

extern crate xc_private_method_lib;

fn main() {
    let _ = xc_private_method_lib::Struct{ x: 10 }.meth_struct();
    //~^ ERROR associated function `meth_struct` is private

    let _ = xc_private_method_lib::Enum::Variant1(20).meth_enum();
    //~^ ERROR associated function `meth_enum` is private
}


