tests/ui/rfc-2294-if-let-guard/warns.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

#[deny(irrefutable_let_patterns)]
fn irrefutable_let_guard() {
    match Some(()) {
        Some(x) if let () = x => {}
        //~^ ERROR irrefutable `if let` guard
        _ => {}
    }
}

#[deny(unreachable_patterns)]
fn unreachable_pattern() {
    match Some(()) {
        x if let None | None = x => {}
        //~^ ERROR unreachable pattern
        _ => {}
    }
}

fn main() {}


