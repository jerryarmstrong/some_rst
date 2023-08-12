tests/ui/query-system/fn-sig-cycle-arity.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Dancer {
    fn dance(&self) -> _ {
        //~^ ERROR the placeholder `_` is not allowed within types on item signatures for return types
        self.dance()
    }
}

fn main() {}


