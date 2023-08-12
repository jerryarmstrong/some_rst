tests/ui/structs-enums/struct-new-as-field-name.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo {
    new: isize,
}

pub fn main() {
    let foo = Foo{ new: 3 };
    assert_eq!(foo.new, 3);
}


