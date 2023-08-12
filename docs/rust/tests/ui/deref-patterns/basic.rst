tests/ui/deref-patterns/basic.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// check-run-results
#![feature(string_deref_patterns)]

fn main() {
    test(Some(String::from("42")));
    test(Some(String::new()));
    test(None);
}

fn test(o: Option<String>) {
    match o {
        Some("42") => println!("the answer"),
        Some(_) => println!("something else?"),
        None => println!("nil"),
    }
}


