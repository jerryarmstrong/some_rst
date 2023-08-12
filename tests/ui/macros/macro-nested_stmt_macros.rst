tests/ui/macros/macro-nested_stmt_macros.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! foo {
    () => {
        struct Bar;
        struct Baz;
    }
}

macro_rules! grault {
    () => {
        foo!();
        struct Xyzzy;
    }
}

fn static_assert_exists<T>() { }

fn main() {
    grault!();
    static_assert_exists::<Bar>();
    static_assert_exists::<Baz>();
    static_assert_exists::<Xyzzy>();
}


