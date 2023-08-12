tests/ui/associated-types/associated-types-unsized.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(dead_code, unused_variables)]

trait Get {
    type Value: ?Sized;
    fn get(&self) -> <Self as Get>::Value;
}

fn foo<T:Get>(t: T) {
    let x = t.get(); //~ ERROR the size for values of type
}

fn main() {
}


