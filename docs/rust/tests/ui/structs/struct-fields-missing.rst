tests/ui/structs/struct-fields-missing.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BuildData {
    foo: isize,
    bar: Box<isize>,
}

fn main() {
    let foo = BuildData { //~ ERROR missing field `bar` in initializer of `BuildData`
        foo: 0
    };
}


