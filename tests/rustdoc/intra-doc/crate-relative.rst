tests/rustdoc/intra-doc/crate-relative.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Test<'a> {
    data: &'a (),
}

impl<'a> Test<'a> {
    pub fn do_test(&self) {}
}

// @has crate_relative/demo/index.html
// @has - '//a/@href' '../struct.Test.html#method.do_test'
pub mod demo {
    //! [`crate::Test::do_test`]
}


