tests/ui/suggestions/const-in-struct-pat.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(non_camel_case_types)]
struct foo;
struct Thing {
    foo: String,
}

fn example(t: Thing) {
    let Thing { foo } = t; //~ ERROR mismatched types
}

fn main() {}


