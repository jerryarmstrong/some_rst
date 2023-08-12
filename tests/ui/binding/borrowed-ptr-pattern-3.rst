tests/ui/binding/borrowed-ptr-pattern-3.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo<'r>(s: &'r usize) -> bool {
    match s {
        &3 => true,
        _ => false
    }
}

pub fn main() {
    assert!(foo(&3));
    assert!(!foo(&4));
}


