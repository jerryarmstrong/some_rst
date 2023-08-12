tests/ui/traits/associated_type_bound/check-trait-object-bounds-6.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we validate associated type bounds on super traits for trait
// objects

trait Is {
    type T;
}

impl<U> Is for U {
    type T = U;
}

trait Obj {
    type U: Is<T = Self::V>;
    type V;
}

fn is_obj<T: ?Sized + Obj>(_: &T) {}

fn f(x: &dyn Obj<U = i32, V = i64>) {
    is_obj(x)
    //~^ ERROR type mismatch resolving `<i32 as Is>::T == i64`
}

fn main() {}


