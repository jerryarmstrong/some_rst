src/tools/rustfmt/tests/source/fn-custom-4.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test different indents.

fn qux() where X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT, X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT, X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT, X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT {
    baz();
}

fn qux() where X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT {
    baz();
}

fn qux(a: Aaaaaaaaaaaaaaaaa) where X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT, X: TTTTTTTTTTTTTTTTTTTTTTTTTTTT {
    baz();
}


