tests/ui/enum/enum-in-scope.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_camel_case_types)]

struct hello(isize);

fn main() {
    let hello = 0; //~ERROR let bindings cannot shadow tuple structs
}


