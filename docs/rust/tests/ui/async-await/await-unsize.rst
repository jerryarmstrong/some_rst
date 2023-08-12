tests/ui/async-await/await-unsize.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #62312

// check-pass
// edition:2018

async fn make_boxed_object() -> Box<dyn Send> {
    Box::new(()) as _
}

async fn await_object() {
    let _ = make_boxed_object().await;
}

fn main() {}


