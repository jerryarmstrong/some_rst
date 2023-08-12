tests/ui/generic-associated-types/auxiliary/foo_defn.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::{future::Future, pin::Pin};

pub trait Foo {
    type Bar: AsRef<()>;
    fn foo(&self) -> Pin<Box<dyn Future<Output = Self::Bar> + '_>>;
}


