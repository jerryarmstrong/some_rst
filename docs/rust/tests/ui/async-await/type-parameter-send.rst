tests/ui/async-await/type-parameter-send.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --crate-type lib
// edition:2018

fn assert_send<F: Send>(_: F) {}

async fn __post<T>() -> T {
    if false {
        todo!()
    } else {
        async {}.await;
        todo!()
    }
}

fn foo<T>() {
    assert_send(__post::<T>());
}


