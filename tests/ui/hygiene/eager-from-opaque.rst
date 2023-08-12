tests/ui/hygiene/eager-from-opaque.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Opaque macro can eagerly expand its input without breaking its resolution.
// Regression test for issue #63685.

// check-pass

macro_rules! foo {
    () => {
        "foo"
    };
}

macro_rules! bar {
    () => {
        foo!()
    };
}

fn main() {
    format_args!(bar!());
}


