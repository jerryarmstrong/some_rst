tests/ui/match/match-bot-panic.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

#![allow(unreachable_code)]
#![allow(unused_variables)]

fn foo(s: String) {}

fn main() {
    let i = match Some::<isize>(3) {
        None::<isize> => panic!(),
        Some::<isize>(_) => panic!(),
    };
    foo(i);
}


