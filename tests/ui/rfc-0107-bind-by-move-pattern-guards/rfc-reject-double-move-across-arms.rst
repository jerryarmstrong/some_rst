tests/ui/rfc-0107-bind-by-move-pattern-guards/rfc-reject-double-move-across-arms.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

enum VecWrapper { A(Vec<i32>) }

fn if_guard(x: VecWrapper) -> usize {
    match x {
        VecWrapper::A(v) if { drop(v); false } => 1,
        //~^ ERROR cannot move out of `v` in pattern guard
        VecWrapper::A(v) => v.len()
    }
}

fn if_let_guard(x: VecWrapper) -> usize {
    match x {
        VecWrapper::A(v) if let Some(()) = { drop(v); None } => 1,
        //~^ ERROR cannot move out of `v` in pattern guard
        VecWrapper::A(v) => v.len()
    }
}

fn main() {
    if_guard(VecWrapper::A(vec![107]));
    if_let_guard(VecWrapper::A(vec![107]));
}


