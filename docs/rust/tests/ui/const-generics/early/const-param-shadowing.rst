tests/ui/const-generics/early/const-param-shadowing.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type N = u32;
struct Foo<const M: usize>;
fn test<const N: usize>() -> Foo<N> { //~ ERROR type provided when
    Foo
}

fn main() {}


