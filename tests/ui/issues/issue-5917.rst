tests/ui/issues/issue-5917.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

struct T (&'static [isize]);
static t : T = T (&[5, 4, 3]);
pub fn main () {
    let T(ref v) = t;
    assert_eq!(v[0], 5);
}


