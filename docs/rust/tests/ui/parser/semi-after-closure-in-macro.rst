tests/ui/parser/semi-after-closure-in-macro.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Checks that the fix in #103222 doesn't also disqualify semicolons after
// closures within parentheses *in macros*, where they're totally allowed.

macro_rules! m {
    (($expr:expr ; )) => {
        $expr
    };
}

fn main() {
    let x = m!(( ||() ; ));
}


