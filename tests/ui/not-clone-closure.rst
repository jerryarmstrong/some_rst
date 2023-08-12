tests/ui/not-clone-closure.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that closures do not implement `Clone` if their environment is not `Clone`.

struct S(i32);

fn main() {
    let a = S(5);
    let hello = move || {
        println!("Hello {}", a.0);
    };

    let hello = hello.clone(); //~ ERROR the trait bound `S: Clone` is not satisfied
}


