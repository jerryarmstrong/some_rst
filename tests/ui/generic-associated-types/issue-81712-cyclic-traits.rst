tests/ui/generic-associated-types/issue-81712-cyclic-traits.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #81712.

trait A {
    type BType: B<AType = Self>;
}

trait B {
    type AType: A<BType = Self>;
}
trait C {
    type DType<T>: D<T, CType = Self>;
}
trait D<T> {
    type CType: C<DType = Self>;
    //~^ ERROR missing generics for associated type
}

fn main() {}


