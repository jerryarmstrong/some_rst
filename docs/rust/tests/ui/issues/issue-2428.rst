tests/ui/issues/issue-2428.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]


pub fn main() {
    let _foo = 100;
    const quux: isize = 5;

    enum Stuff {
        Bar = quux
    }

    assert_eq!(Stuff::Bar as isize, quux);
}


