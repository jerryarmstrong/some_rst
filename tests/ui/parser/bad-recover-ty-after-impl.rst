tests/ui/parser/bad-recover-ty-after-impl.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! impl_primitive {
    ($ty:ty) => { impl_primitive!(impl $ty); };
    (impl $ty:ty) => { fn a(_: $ty) {} }
}

impl_primitive! { u8 }

macro_rules! test {
    ($ty:ty) => { compile_error!("oh no"); };
    (impl &) => {};
}

test!(impl &);

fn main() {}


