tests/ui/const-generics/const-generic-type_name.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Debug)]
struct S<const N: usize>;

fn main() {
    assert_eq!(std::any::type_name::<S<3>>(), "const_generic_type_name::S<3>");
}


