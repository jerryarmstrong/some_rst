tests/rustdoc/fn-sidebar.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.bar.html
// @has - '//*[@class="sidebar-elems"]' ''
pub fn bar() {}

// @has foo/constant.BAR.html
// @has - '//*[@class="sidebar-elems"]' ''
pub const BAR: u32 = 0;


