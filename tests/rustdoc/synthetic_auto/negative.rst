tests/rustdoc/synthetic_auto/negative.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Inner<T: Copy> {
    field: *mut T,
}

// @has negative/struct.Outer.html
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// "impl<T> !Send for Outer<T>"
//
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// "impl<T> !Sync for Outer<T>"
pub struct Outer<T: Copy> {
    inner_field: Inner<T>,
}


