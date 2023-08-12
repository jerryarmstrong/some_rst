tests/run-make-fulldeps/share-generics-dylib/instance_provider_a.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;

pub fn foo() {
    let a: Cell<i32> = Cell::new(1);
    a.set(123);
}


