tests/ui/unsized-locals/box-fnonce.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn call_it<T>(f: Box<dyn FnOnce() -> T>) -> T {
    f()
}

fn main() {
    let s = "hello".to_owned();
    assert_eq!(&call_it(Box::new(|| s)) as &str, "hello");
}


