tests/ui/rfc-0107-bind-by-move-pattern-guards/rfc-reject-double-move-in-first-arm.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

struct A { a: Box<i32> }

fn if_guard(n: i32) {
    let x = A { a: Box::new(n) };
    let _y = match x {
        A { a: v } if { drop(v); true } => v,
        //~^ ERROR cannot move out of `v` in pattern guard
        _ => Box::new(0),
    };
}

fn if_let_guard(n: i32) {
    let x = A { a: Box::new(n) };
    let _y = match x {
        A { a: v } if let Some(()) = { drop(v); Some(()) } => v,
        //~^ ERROR cannot move out of `v` in pattern guard
        _ => Box::new(0),
    };
}

fn main() {
    if_guard(107);
    if_let_guard(107);
}


