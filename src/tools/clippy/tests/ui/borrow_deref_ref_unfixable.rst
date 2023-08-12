src/tools/clippy/tests/ui/borrow_deref_ref_unfixable.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code, unused_variables)]

fn main() {}

mod should_lint {
    fn two_helps() {
        let s = &String::new();
        let x: &str = &*s;
    }
}


