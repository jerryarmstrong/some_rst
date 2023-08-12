tests/ui/macros/macro_path_as_generic_bound.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

macro_rules! foo(($t:path) => {
    impl<T: $t> Foo for T {}
});

foo!(m::m2::A); //~ ERROR failed to resolve

fn main() {}


