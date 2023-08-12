tests/ui/traits/object/bounds-cycle-2.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we don't have a cycle when we try to normalize `Self::V` in the
// bound below.

// check-pass

trait Is {
    type T;
}

impl<U> Is for U {
    type T = U;
}

trait Super {
    type V;
}

trait Obj: Super {
    type U: Is<T = Self::V>;
}

fn is_obj<T: ?Sized + Obj>(_: &T) {}

fn f(x: &dyn Obj<U = i32, V = i32>) {
    is_obj(x)
}

fn main() {}


