tests/rustdoc/synthetic_auto/static-region.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait OwnedTrait<'a> {
    type Reader;
}

// @has static_region/struct.Owned.html
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// "impl<T> Send for Owned<T>where <T as OwnedTrait<'static>>::Reader: Send"
pub struct Owned<T> where T: OwnedTrait<'static> {
    marker: <T as OwnedTrait<'static>>::Reader,
}


