tests/ui/missing/missing-block-hint.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    {
        if (foo) => {} //~ ERROR expected `{`, found `=>`
    }
    {
        if (foo)
            bar; //~ ERROR expected `{`, found `bar`
    }
}


