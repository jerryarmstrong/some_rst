tests/ui/structs/struct-path-alias-bounds.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #36286

struct S<T: Clone> { a: T }

struct NoClone;
type A = S<NoClone>;

fn main() {
    let s = A { a: NoClone };
    //~^ ERROR the trait bound `NoClone: Clone` is not satisfied
}


