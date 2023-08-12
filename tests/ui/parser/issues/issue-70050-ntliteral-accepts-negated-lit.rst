tests/ui/parser/issues/issue-70050-ntliteral-accepts-negated-lit.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! foo {
    ($a:literal) => {
        bar!($a)
    };
}

macro_rules! bar {
    ($b:literal) => {};
}

fn main() {
    foo!(-2);
    bar!(-2);
}


