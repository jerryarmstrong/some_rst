tests/rustdoc/strip-enum-variant.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has strip_enum_variant/enum.MyThing.html
// @has - '//code' 'Shown'
// @!has - '//code' 'NotShown'
// @has - '//code' '// some variants omitted'
// Also check that `NotShown` isn't displayed in the sidebar.
// @snapshot no-not-shown - '//*[@class="sidebar-elems"]/section/*[@class="block"][1]'
pub enum MyThing {
    Shown,
    #[doc(hidden)]
    NotShown,
}


