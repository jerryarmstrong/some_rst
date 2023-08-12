src/tools/miri/tests/fail/issue-miri-2432.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(where_clauses_object_safety)]

trait Trait {}

trait X {
    fn foo(&self)
    where
        Self: Trait;
}

impl X for () {
    fn foo(&self) {}
}

impl Trait for dyn X {}

pub fn main() {
    <dyn X as X>::foo(&()); //~ERROR: trying to call something that is not a method
}


