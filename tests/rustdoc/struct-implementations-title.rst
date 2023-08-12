tests/rustdoc/struct-implementations-title.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub struct Struc;

// @has foo/struct.Struc.html
// @has - '//*[@id="main-content"]/h2[@id="implementations"]' "Implementations"
impl Struc {
    pub const S: u64 = 0;
}


