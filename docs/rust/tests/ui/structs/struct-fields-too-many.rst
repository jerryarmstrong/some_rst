tests/ui/structs/struct-fields-too-many.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BuildData {
    foo: isize,
}

fn main() {
    let foo = BuildData {
        foo: 0,
        bar: 0
        //~^ ERROR struct `BuildData` has no field named `bar`
    };
}


