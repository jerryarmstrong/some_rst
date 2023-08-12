tests/ui/deref-patterns/refs.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(string_deref_patterns)]

fn foo(s: &String) -> i32 {
    match *s {
        "a" => 42,
        _ => -1,
    }
}

fn bar(s: Option<&&&&String>) -> i32 {
    match s {
        Some(&&&&"&&&&") => 1,
        _ => -1,
    }
}

fn main() {}


