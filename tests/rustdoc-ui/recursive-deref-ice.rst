tests/rustdoc-ui/recursive-deref-ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// ICE found in https://github.com/rust-lang/rust/issues/83123

pub struct Attribute;

pub struct Map<'hir> {}
impl<'hir> Map<'hir> {
    pub fn attrs(&self) -> &'hir [Attribute] { &[] }
}

pub struct List<T>(T);

impl<T> std::ops::Deref for List<T> {
    type Target = [T];
    fn deref(&self) -> &[T] {
        &[]
    }
}


