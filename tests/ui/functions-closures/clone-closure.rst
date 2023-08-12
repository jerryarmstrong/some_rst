tests/ui/functions-closures/clone-closure.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that closures implement `Clone`.

#[derive(Clone)]
struct S(i32);

fn main() {
    let mut a = S(5);
    let mut hello = move || {
        a.0 += 1;
        println!("Hello {}", a.0);
        a.0
    };

    let mut hello2 = hello.clone();
    assert_eq!(6, hello2());
    assert_eq!(6, hello());
}


