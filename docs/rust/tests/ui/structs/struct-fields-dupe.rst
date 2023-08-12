tests/ui/structs/struct-fields-dupe.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BuildData {
    foo: isize,
}

fn main() {
    let foo = BuildData {
        foo: 0,
        foo: 0 //~ ERROR field `foo` specified more than once
    };
}


