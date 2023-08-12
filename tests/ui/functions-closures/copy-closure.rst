tests/ui/functions-closures/copy-closure.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that closures implement `Copy`.

fn call<T, F: FnOnce() -> T>(f: F) -> T { f() }

fn main() {
    let a = 5;
    let hello = || {
        println!("Hello {}", a);
        a
    };

    assert_eq!(5, call(hello.clone()));
    assert_eq!(5, call(hello));
    assert_eq!(5, call(hello));
}


