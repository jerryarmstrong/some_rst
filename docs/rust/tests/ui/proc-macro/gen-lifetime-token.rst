tests/ui/proc-macro/gen-lifetime-token.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:gen-lifetime-token.rs

extern crate gen_lifetime_token as bar;

bar::bar!();

fn main() {
    let x: &'static i32 = FOO;
    assert_eq!(*x, 1);
}


