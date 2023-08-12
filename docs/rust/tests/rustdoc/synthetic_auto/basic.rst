tests/rustdoc/synthetic_auto/basic.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has basic/struct.Foo.html
// @has - '//h3[@class="code-header"]' 'impl<T> Send for Foo<T>where T: Send'
// @has - '//h3[@class="code-header"]' 'impl<T> Sync for Foo<T>where T: Sync'
// @count - '//*[@id="implementations-list"]//*[@class="impl has-srclink"]' 0
// @count - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]' 5
pub struct Foo<T> {
    field: T,
}


