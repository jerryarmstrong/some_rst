src/tools/rustfmt/tests/source/issue-4398.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl Struct {
    /// Documentation for `foo`
    #[rustfmt::skip] // comment on why use a skip here
    pub fn foo(&self) {}
}

impl Struct {
    /// Documentation for `foo`
       #[rustfmt::skip] // comment on why use a skip here
    pub fn foo(&self) {}
}

/// Documentation for `Struct`
#[rustfmt::skip] // comment
impl Struct {
    /// Documentation for `foo`
       #[rustfmt::skip] // comment on why use a skip here
    pub fn foo(&self) {}
}


