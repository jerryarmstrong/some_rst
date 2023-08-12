tests/rustdoc/auxiliary/issue-99221-aux.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Option;
impl Option {
    pub fn unwrap(self) {}
}

mod macros {
    use crate::Option;
    /// [`Option::unwrap`]
    #[macro_export]
    macro_rules! print {
        () => ()
    }
}

mod structs {
    use crate::Option;
    /// [`Option::unwrap`]
    pub struct Print;
}
pub use structs::Print;


