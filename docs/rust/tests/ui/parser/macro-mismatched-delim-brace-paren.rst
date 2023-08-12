tests/ui/parser/macro-mismatched-delim-brace-paren.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo { ($($tt:tt)*) => () }

fn main() {
    foo! {
        bar, "baz", 1, 2.0
    ) //~ ERROR mismatched closing delimiter
}


