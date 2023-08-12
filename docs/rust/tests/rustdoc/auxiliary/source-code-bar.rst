tests/rustdoc/auxiliary/source-code-bar.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! just some other file. :)

use crate::Foo;

pub struct Bar {
    field: Foo,
}

pub struct Bar2 {
    field: crate::Foo,
}

pub mod sub {
    pub trait Trait {
        fn tadam() {}
    }
}


