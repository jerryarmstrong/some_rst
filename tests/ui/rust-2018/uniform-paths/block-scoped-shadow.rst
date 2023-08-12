tests/ui/rust-2018/uniform-paths/block-scoped-shadow.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![allow(non_camel_case_types)]

enum Foo {}

struct std;

fn main() {
    enum Foo { A, B }
    use Foo::*;
    //~^ ERROR `Foo` is ambiguous

    let _ = (A, B);

    fn std() {}
    enum std {}
    use std as foo;
    //~^ ERROR `std` is ambiguous
    //~| ERROR `std` is ambiguous
}


