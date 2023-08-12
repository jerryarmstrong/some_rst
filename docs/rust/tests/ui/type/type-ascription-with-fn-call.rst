tests/ui/type/type-ascription-with-fn-call.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![feature(type_ascription)]

fn main() {
    f()  :
    f(); //~ ERROR expected type, found function
}

fn f() {}


