tests/rustdoc/doc-assoc-item.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo<T> {
    x: T,
}

pub trait Bar {
    type Fuu;

    fn foo(foo: Self::Fuu);
}

// @has doc_assoc_item/struct.Foo.html '//*[@class="impl has-srclink"]' 'impl<T: Bar<Fuu = u32>> Foo<T>'
impl<T: Bar<Fuu = u32>> Foo<T> {
    pub fn new(t: T) -> Foo<T> {
        Foo {
            x: t,
        }
    }
}


