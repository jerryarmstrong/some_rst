tests/rustdoc/recursion2.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

mod m {
    pub use self::a::Foo;

    mod a {
        pub struct Foo;
    }

    mod b {
        pub use super::*;
    }
}


