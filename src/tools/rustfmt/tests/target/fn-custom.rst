src/tools/rustfmt/tests/target/fn-custom.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-fn_args_layout: Compressed
// Test some of the ways function signatures can be customised.

// Test compressed layout of args.
fn foo(
    a: Aaaaaaaaaaaaaaa, b: Bbbbbbbbbbbbbbbb, c: Ccccccccccccccccc, d: Ddddddddddddddddddddddddd,
    e: Eeeeeeeeeeeeeeeeeee,
) {
    foo();
}

impl Foo {
    fn foo(
        self, a: Aaaaaaaaaaaaaaa, b: Bbbbbbbbbbbbbbbb, c: Ccccccccccccccccc,
        d: Ddddddddddddddddddddddddd, e: Eeeeeeeeeeeeeeeeeee,
    ) {
        foo();
    }
}


