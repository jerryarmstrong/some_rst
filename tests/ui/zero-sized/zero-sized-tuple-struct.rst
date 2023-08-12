tests/ui/zero-sized/zero-sized-tuple-struct.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_braces)]
#![allow(unused_assignments)]

// Make sure that the constructor args are codegened for zero-sized tuple structs

struct Foo(());

fn main() {
    let mut a = 1;
    Foo({ a = 2 });
    assert_eq!(a, 2);
}


