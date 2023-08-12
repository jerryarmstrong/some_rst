tests/ui/borrowck/access-mode-in-closures.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(Vec<isize>);

fn unpack<F>(_unpack: F) where F: FnOnce(&S) -> Vec<isize> {}

fn main() {
    let _foo = unpack(|s| {
        // Test that `s` is moved here.
        match *s { S(v) => v } //~ ERROR cannot move out
    });
}


