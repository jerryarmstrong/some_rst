tests/ui/borrowck/borrowck-lend-args.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

// pretty-expanded FIXME #23616

fn borrow(_v: &isize) {}

fn borrow_from_arg_imm_ref(v: Box<isize>) {
    borrow(&*v);
}

fn borrow_from_arg_mut_ref(v: &mut Box<isize>) {
    borrow(&**v);
}

fn borrow_from_arg_copy(v: Box<isize>) {
    borrow(&*v);
}

pub fn main() {
}


