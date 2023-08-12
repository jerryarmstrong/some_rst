tests/ui/const-generics/type-dependent/qpath.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct A;
impl A {
    fn foo<const N: usize>() -> usize { N + 1 }
}

fn main() {
    assert_eq!(A::foo::<7>(), 8);
}


