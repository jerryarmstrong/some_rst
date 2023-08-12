tests/ui/impl-trait/auto-trait-leak-rpass.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Fast path, main can see the concrete type returned.
fn before() -> impl FnMut(i32) {
    let mut p = Box::new(0);
    move |x| *p = x
}

fn send<T: Send>(_: T) {}

fn main() {
    send(before());
    send(after());
}

// Deferred path, main has to wait until typeck finishes,
// to check if the return type of after is Send.
fn after() -> impl FnMut(i32) {
    let mut p = Box::new(0);
    move |x| *p = x
}


