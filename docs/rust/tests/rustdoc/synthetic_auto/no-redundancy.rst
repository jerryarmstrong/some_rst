tests/rustdoc/synthetic_auto/no-redundancy.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Inner<T> {
    field: T,
}

unsafe impl<T> Send for Inner<T>
where
    T: Copy + Send,
{
}

// @has no_redundancy/struct.Outer.html
// @has - '//*[@id="synthetic-implementations-list"]//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// "impl<T> Send for Outer<T>where T: Send + Copy"
pub struct Outer<T> {
    inner_field: Inner<T>,
}


