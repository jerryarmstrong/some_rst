tests/ui/parser/bad-recover-kw-after-impl.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// edition:2021
// for the `impl` + keyword test

macro_rules! impl_primitive {
    ($ty:ty) => {
        compile_error!("whoops");
    };
    (impl async) => {};
}

impl_primitive!(impl async);

fn main() {}


