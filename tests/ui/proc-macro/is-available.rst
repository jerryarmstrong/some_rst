tests/ui/proc-macro/is-available.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

extern crate proc_macro;

// aux-build:is-available.rs
extern crate is_available;

fn main() {
    let a = proc_macro::is_available();
    let b = is_available::from_inside_proc_macro!();
    let c = proc_macro::is_available();
    assert!(!a);
    assert!(b);
    assert!(!c);
}


