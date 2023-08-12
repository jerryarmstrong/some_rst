tests/ui/lint/rfc-2383-lint-reason/expect_inside_macro.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(lint_reasons)]

#![warn(unused)]

macro_rules! expect_inside_macro {
    () => {
        #[expect(unused_variables)]
        let x = 0;
    };
}

fn main() {
    expect_inside_macro!();
}


