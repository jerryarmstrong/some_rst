src/tools/rustfmt/tests/source/issue_4675.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ($s:ident ( $p:pat )) => {
        Foo {
            name: Name::$s($p),
            ..
    }
    };
}

