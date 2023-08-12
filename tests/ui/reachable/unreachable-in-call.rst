tests/ui/reachable/unreachable-in-call.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![deny(unreachable_code)]

fn diverge() -> ! { panic!() }

fn get_u8() -> u8 {
    1
}
fn call(_: u8, _: u8) {

}
fn diverge_first() {
    call(diverge(),
         get_u8()); //~ ERROR unreachable expression
}
fn diverge_second() {
    call( //~ ERROR unreachable call
        get_u8(),
        diverge());
}

fn main() {}


