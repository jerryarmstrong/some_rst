tests/rustdoc-js/foreign-type-path.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

pub mod aaaaaaa {

    extern {
        pub type MyForeignType;
    }

    impl MyForeignType {
        pub fn my_method() {}
    }

}


