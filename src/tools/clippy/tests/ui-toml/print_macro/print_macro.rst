src/tools/clippy/tests/ui-toml/print_macro/print_macro.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test
#![warn(clippy::print_stdout)]
#![warn(clippy::print_stderr)]

fn foo(n: u32) {
    print!("{n}");
    eprint!("{n}");
}

#[test]
pub fn foo1() {
    print!("{}", 1);
    eprint!("{}", 1);
}

#[cfg(test)]
fn foo3() {
    print!("{}", 1);
    eprint!("{}", 1);
}


