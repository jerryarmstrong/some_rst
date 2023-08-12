tests/ui/borrowck/borrowck-pat-enum.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// ignore-pretty issue #37199

fn match_ref(v: Option<isize>) -> isize {
    match v {
      Some(ref i) => {
        *i
      }
      None => {0}
    }
}

fn match_ref_unused(v: Option<isize>) {
    match v {
      Some(_) => {}
      None => {}
    }
}

fn impure(_i: isize) {
}

fn match_imm_reg(v: &Option<isize>) {
    match *v {
      Some(ref i) => {impure(*i)} // OK because immutable
      None => {}
    }
}

fn match_mut_reg(v: &mut Option<isize>) {
    match *v {
      Some(ref i) => {impure(*i)} // OK, frozen
      None => {}
    }
}

pub fn main() {
}


