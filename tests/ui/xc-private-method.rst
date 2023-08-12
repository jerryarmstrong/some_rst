tests/ui/xc-private-method.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:xc-private-method-lib.rs

extern crate xc_private_method_lib;

fn main() {
    let _ = xc_private_method_lib::Struct::static_meth_struct();
    //~^ ERROR: associated function `static_meth_struct` is private

    let _ = xc_private_method_lib::Enum::static_meth_enum();
    //~^ ERROR: associated function `static_meth_enum` is private
}


