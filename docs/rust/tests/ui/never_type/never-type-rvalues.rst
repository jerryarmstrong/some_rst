tests/ui/never_type/never-type-rvalues.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(never_type)]
#![allow(dead_code)]
#![allow(path_statements)]
#![allow(unreachable_patterns)]

fn never_direct(x: !) {
    x;
}

fn never_ref_pat(ref x: !) {
    *x;
}

fn never_ref(x: &!) {
    let &y = x;
    y;
}

fn never_pointer(x: *const !) {
    unsafe {
        *x;
    }
}

fn never_slice(x: &[!]) {
    x[0];
}

fn never_match(x: Result<(), !>) {
    match x {
        Ok(_) => {},
        Err(_) => {},
    }
}

pub fn main() { }


