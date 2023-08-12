tests/ui/typeck/issue-89044-wrapped-expr-method.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let a = Some(42);
    println!(
        "The value is {}.",
        (a.unwrap) //~ERROR [E0615]
    );
}


