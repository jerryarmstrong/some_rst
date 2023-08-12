tests/ui/underscore-imports/auxiliary/underscore-imports.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! do_nothing {
    () => ()
}

mod m1 {
    pub trait InScope1 {
        fn in_scope1(&self) {}
    }
    impl InScope1 for () {}
}
mod m2 {
    pub trait InScope2 {
        fn in_scope2(&self) {}
    }
    impl InScope2 for () {}
}

pub use m1::InScope1 as _;
pub use m2::InScope2 as _;


