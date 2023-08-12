tests/ui/unconstrained-ref.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<'a, T:'a> {
    o: &'a Option<T>
}

fn main() {
    S { o: &None }; //~ ERROR type annotations needed [E0282]
}


