tests/ui/consts/const-validation-fail-55455.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/55454
// build-pass (FIXME(62277): could be check-pass?)

struct This<T>(T);

const C: This<Option<&i32>> = This(Some(&1));

fn main() {
}


