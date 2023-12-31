src/tools/clippy/tests/ui/overly_complex_bool_expr.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lint_reasons)]
#![allow(unused, clippy::diverging_sub_expression)]
#![warn(clippy::overly_complex_bool_expr)]

fn main() {
    let a: bool = unimplemented!();
    let b: bool = unimplemented!();
    let c: bool = unimplemented!();
    let d: bool = unimplemented!();
    let e: bool = unimplemented!();
    let _ = a && b || a;
    let _ = !(a && b);
    let _ = false && a;
    // don't lint on cfgs
    let _ = cfg!(you_shall_not_not_pass) && a;
    let _ = a || !b || !c || !d || !e;
    let _ = !(a && b || c);
}

fn equality_stuff() {
    let a: i32 = unimplemented!();
    let b: i32 = unimplemented!();
    let _ = a == b && a != b;
    let _ = a < b && a >= b;
    let _ = a > b && a <= b;
    let _ = a > b && a == b;
}

fn check_expect() {
    let a: i32 = unimplemented!();
    let b: i32 = unimplemented!();
    #[expect(clippy::overly_complex_bool_expr)]
    let _ = a < b && a >= b;
}


