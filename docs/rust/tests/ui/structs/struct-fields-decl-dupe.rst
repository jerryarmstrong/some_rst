tests/ui/structs/struct-fields-decl-dupe.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BuildData {
    foo: isize,
    foo: isize,
    //~^ ERROR field `foo` is already declared [E0124]
}

fn main() {
}


