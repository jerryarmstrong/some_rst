tests/ui/moves/moves-based-on-type-capture-clause-bad.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::thread;

fn main() {
    let x = "Hello world!".to_string();
    thread::spawn(move|| {
        println!("{}", x);
    });
    println!("{}", x); //~ ERROR borrow of moved value
}


