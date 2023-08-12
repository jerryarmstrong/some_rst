tests/ui/match/match-disc-bot.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:quux
// ignore-emscripten no processes

fn f() -> ! {
    panic!("quux")
}
fn g() -> isize {
    match f() {
        true => 1,
        false => 0,
    }
}
fn main() {
    g();
}


