tests/ui/async-await/drop-and-assign.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// compile-flags: -Zdrop-tracking
// build-pass

struct A;
impl Drop for A { fn drop(&mut self) {} }

pub async fn f() {
    let mut a = A;
    a = A;
    drop(a);
    async {}.await;
}

fn assert_send<T: Send>(_: T) {}

fn main() {
    let _ = f();
}


