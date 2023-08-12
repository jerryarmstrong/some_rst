tests/rustdoc/blanket-reexport-item.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/struct.S.html '//*[@id="impl-Into%3CU%3E-for-S"]//h3[@class="code-header"]' 'impl<T, U> Into<U> for T'
pub struct S2 {}
mod m {
    pub struct S {}
}
pub use m::*;


