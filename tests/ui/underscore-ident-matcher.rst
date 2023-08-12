tests/ui/underscore-ident-matcher.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! identity {
    ($i: ident) => (
        $i
    )
}

fn main() {
    let identity!(_) = 10; //~ ERROR no rules expected the token `_`
}


