tests/ui/generic-associated-types/const-generics-gat-in-trait-return-type-3.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// This test unsures that with_opt_const_param returns the
// def_id of the N param in the Bar::Assoc GAT.

trait Bar {
    type Assoc<const N: usize>;
}
trait Foo: Bar {
    fn foo(&self) -> Self::Assoc<3>;
}

impl Bar for () {
    type Assoc<const N: usize> = [(); N];
}

impl Foo for () {
    fn foo(&self) -> Self::Assoc<3> {
        [(); 3]
    }
}

fn main() {
    assert_eq!(().foo(), [(); 3]);
}


