tests/ui/borrowck/move-error-snippets-ext.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test

macro_rules! aaa {
    ($c:ident) => {{
        let a = $c;
    }}
}


