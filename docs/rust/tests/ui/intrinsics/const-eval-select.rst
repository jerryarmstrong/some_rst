tests/ui/intrinsics/const-eval-select.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(const_eval_select)]
#![feature(core_intrinsics)]

use std::intrinsics::const_eval_select;

const fn yes() -> bool {
    true
}

fn no() -> bool {
    false
}

// not a sound use case; testing only
const fn is_const_eval() -> bool {
    unsafe { const_eval_select((), yes, no) }
}

fn main() {
    const YES: bool = is_const_eval();
    let no = is_const_eval();

    assert_eq!(true, YES);
    assert_eq!(false, no);
}


