tests/ui/macro_backtrace/main.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the macro backtrace facility works
// aux-build:ping.rs
// revisions: default -Zmacro-backtrace
//[-Zmacro-backtrace] compile-flags: -Z macro-backtrace

#[macro_use] extern crate ping;

// a local macro
macro_rules! pong {
    () => { syntax error };
}
//~^^ ERROR expected one of
//~| ERROR expected one of
//~| ERROR expected one of

#[allow(non_camel_case_types)]
struct syntax;

fn main() {
    pong!();
    ping!();
    deep!();
}


