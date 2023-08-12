tests/rustdoc/synthetic_auto/manual.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has manual/struct.Foo.html
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// 'impl<T> Sync for Foo<T>where T: Sync'
//
// @has - '//*[@id="trait-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// 'impl<T> Send for Foo<T>'
//
// @count - '//*[@id="trait-implementations-list"]//*[@class="impl has-srclink"]' 1
// @count - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]' 4
pub struct Foo<T> {
    field: T,
}

unsafe impl<T> Send for Foo<T> {}


