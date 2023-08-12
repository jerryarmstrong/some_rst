tests/ui/generic-associated-types/const-generics-gat-in-trait-return-type-2.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// This test unsures that with_opt_const_param returns the
// def_id of the N param in the Foo::Assoc GAT.

trait Foo {
    type Assoc<const N: usize>;
    fn foo<const N: usize>(&self) -> Self::Assoc<N>;
}

impl Foo for () {
    type Assoc<const N: usize> = [(); N];
    fn foo<const N: usize>(&self) -> Self::Assoc<N> {
        [(); N]
    }
}

fn main() {
    assert_eq!(().foo::<10>(), [(); 10]);
}


