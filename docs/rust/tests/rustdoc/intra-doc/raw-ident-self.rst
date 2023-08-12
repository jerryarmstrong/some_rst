tests/rustdoc/intra-doc/raw-ident-self.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]
pub mod r#impl {
    pub struct S;

    impl S {
        /// See [Self::b].
        // @has raw_ident_self/impl/struct.S.html
        // @has - '//a[@href="struct.S.html#method.b"]' 'Self::b'
        pub fn a() {}

        pub fn b() {}
    }
}


