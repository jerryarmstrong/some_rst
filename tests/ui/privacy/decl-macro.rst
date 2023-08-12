tests/ui/privacy/decl-macro.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod m {
    macro mac() {}
}

fn main() {
    m::mac!(); //~ ERROR macro `mac` is private
}


