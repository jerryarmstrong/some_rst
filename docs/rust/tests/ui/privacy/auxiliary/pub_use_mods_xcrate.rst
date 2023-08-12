tests/ui/privacy/auxiliary/pub_use_mods_xcrate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod a {
    pub use a::b::c;

    pub mod b {
        pub mod c {
            fn f(){}
            fn g(){}
        }
    }
}


