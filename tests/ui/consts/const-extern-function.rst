tests/ui/consts/const-extern-function.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

extern "C" fn foopy() {}

static f: extern "C" fn() = foopy;
static s: S = S { f: foopy };

struct S {
    f: extern "C" fn()
}

pub fn main() {
    assert!(foopy as extern "C" fn() == f);
    assert!(f == s.f);
}


