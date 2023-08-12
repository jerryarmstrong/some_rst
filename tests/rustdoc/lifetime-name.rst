tests/rustdoc/lifetime-name.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has 'foo/type.Resolutions.html'
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' "pub type Resolutions<'tcx> = &'tcx u8;"
pub type Resolutions<'tcx> = &'tcx u8;


