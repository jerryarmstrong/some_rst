tests/run-make-fulldeps/use-suggestions-rust-2018/ep-nested-lib.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

pub mod foo {
    pub mod bar {
        pub struct Baz;
    }
}


