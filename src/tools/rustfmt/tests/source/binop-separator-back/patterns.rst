src/tools/rustfmt/tests/source/binop-separator-back/patterns.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-binop_separator: Back

fn main() {
    match val {
    ThisIsA::ReallyLongPatternNameToHelpOverflowTheNextValueOntoTheNextLine | ThisIsA::SecondValueSeparatedByAPipe | ThisIsA::ThirdValueSeparatedByAPipe => {
    //
    }
    }
}


