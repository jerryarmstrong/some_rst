tests/ui/issues/issue-3121.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

#[derive(Copy, Clone)]
enum side { mayo, catsup, vinegar }
#[derive(Copy, Clone)]
enum order { hamburger, fries(side), shake }
#[derive(Copy, Clone)]
enum meal { to_go(order), for_here(order) }

fn foo(m: Box<meal>, cond: bool) {
    match *m {
      meal::to_go(_) => { }
      meal::for_here(_) if cond => {}
      meal::for_here(order::hamburger) => {}
      meal::for_here(order::fries(_s)) => {}
      meal::for_here(order::shake) => {}
    }
}

pub fn main() {
    foo(Box::new(meal::for_here(order::hamburger)), true)
}


