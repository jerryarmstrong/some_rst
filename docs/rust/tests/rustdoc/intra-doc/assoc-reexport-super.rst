tests/rustdoc/intra-doc/assoc-reexport-super.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #93205

#![crate_name = "foo"]

mod generated {
    pub struct MyNewType;
    impl MyNewType {
        pub const FOO: Self = Self;
    }
}

pub use generated::MyNewType;

mod prelude {
    impl super::MyNewType {
        /// An alias for [`Self::FOO`].
        // @has 'foo/struct.MyNewType.html' '//a[@href="struct.MyNewType.html#associatedconstant.FOO"]' 'Self::FOO'
        pub const FOO2: Self = Self::FOO;
    }
}


