tests/rustdoc/auxiliary/mod-stackoverflow.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Cmetadata=aux

pub mod tree {
    pub use tree;
}

pub mod tree2 {
    pub mod prelude {
        pub use tree2;
    }
}


