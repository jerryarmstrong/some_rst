tests/ui/binding/borrowed-ptr-pattern-2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo(s: &String) -> bool {
    match &**s {
        "kitty" => true,
        _ => false
    }
}

pub fn main() {
    assert!(foo(&"kitty".to_string()));
    assert!(!foo(&"gata".to_string()));
}


