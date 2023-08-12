tests/ui/issues/issue-5550.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_assignments)]
// pretty-expanded FIXME #23616

pub fn main() {
    let s: String = "foobar".to_string();
    let mut t: &str = &s;
    t = &t[0..3]; // for master: str::view(t, 0, 3) maybe
}


