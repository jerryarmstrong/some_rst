tests/ui/not-copy-closure.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that closures do not implement `Copy` if their environment is not `Copy`.

fn main() {
    let mut a = 5;
    let hello = || {
        a += 1;
    };

    let b = hello;
    let c = hello; //~ ERROR use of moved value: `hello` [E0382]
}


