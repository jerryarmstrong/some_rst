tests/rustdoc/sidebar-link-generation.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/struct.SomeStruct.html '//*[@class="sidebar-elems"]//section//li/a[@href="#method.some_fn-1"]' \
//          "some_fn"
pub struct SomeStruct<T> { _inner: T }

impl SomeStruct<()> {
    pub fn some_fn(&self) {}
}

impl SomeStruct<usize> {
    pub fn some_fn(&self) {}
}


