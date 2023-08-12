tests/ui/consts/promoted-validation-55454.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/55454
// build-pass (FIXME(62277): could be check-pass?)

#[derive(PartialEq)]
struct This<T>(T);

fn main() {
    This(Some(&1)) == This(Some(&1));
}


