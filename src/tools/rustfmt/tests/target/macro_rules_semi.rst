src/tools/rustfmt/tests/target/macro_rules_semi.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! expr {
    (no_semi) => {
        return true
    };
    (semi) => {
        return true;
    };
}

fn foo() -> bool {
    match true {
        true => expr!(no_semi),
        false if false => {
            expr!(semi)
        }
        false => {
            expr!(semi);
        }
    }
}

fn main() {}


