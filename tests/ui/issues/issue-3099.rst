tests/ui/issues/issue-3099.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(x: String) -> String {
    format!("First function with {}", x)
}

fn a(x: String, y: String) -> String { //~ ERROR the name `a` is defined multiple times
    format!("Second function with {} and {}", x, y)
}

fn main() {
    println!("Result: ");
}


