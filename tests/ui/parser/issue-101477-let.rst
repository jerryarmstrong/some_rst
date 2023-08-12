tests/ui/parser/issue-101477-let.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let x == 2; //~ ERROR unexpected `==`
    println!("x: {}", x)
}


