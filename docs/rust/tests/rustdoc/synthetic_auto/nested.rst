tests/rustdoc/synthetic_auto/nested.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Inner<T> {
    field: T,
}

unsafe impl<T> Send for Inner<T>
where
    T: Copy,
{
}

// @has nested/struct.Foo.html
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// 'impl<T> Send for Foo<T>where T: Copy'
//
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// 'impl<T> Sync for Foo<T>where T: Sync'
pub struct Foo<T> {
    inner_field: Inner<T>,
}


