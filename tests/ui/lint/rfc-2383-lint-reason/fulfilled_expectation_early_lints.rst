tests/ui/lint/rfc-2383-lint-reason/fulfilled_expectation_early_lints.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(lint_reasons)]

fn expect_early_pass_lints() {
    #[expect(while_true)]
    while true {
        println!("I never stop")
    }

    #[expect(unused_doc_comments)]
    /// This comment triggers the `unused_doc_comments` lint
    let _sheep = "wolf";

    let x = 123;
    #[expect(ellipsis_inclusive_range_patterns)]
    match x {
        0...100 => {}
        _ => {}
    }
}

fn main() {}


