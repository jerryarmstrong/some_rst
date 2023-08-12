tests/ui/issues/issue-2074.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(non_camel_case_types)]

pub fn main() {
    let one = || {
        enum r { a }
        r::a as usize
    };
    let two = || {
        enum r { a }
        r::a as usize
    };
    one(); two();
}


