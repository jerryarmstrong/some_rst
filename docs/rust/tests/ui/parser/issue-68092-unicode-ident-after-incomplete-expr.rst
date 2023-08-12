tests/ui/parser/issue-68092-unicode-ident-after-incomplete-expr.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! x {
    ($($c:tt)*) => {
        $($c)ö* //~ ERROR macro expansion ends with an incomplete expression: expected expression
    };
}

fn main() {
    x!(!);
}


