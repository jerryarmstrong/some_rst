tests/rustdoc/ensure-src-link.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// This test ensures that the [src] link is present on traits items.

// @has foo/trait.Iterator.html '//*[@id="method.zip"]//a[@class="srclink rightside"]' "source"
pub use std::iter::Iterator;


