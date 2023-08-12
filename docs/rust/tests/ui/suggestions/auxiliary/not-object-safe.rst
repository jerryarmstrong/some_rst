tests/ui/suggestions/auxiliary/not-object-safe.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::sync::Arc;

pub trait A {
    fn f();
    fn f2(self: &Arc<Self>);
}


