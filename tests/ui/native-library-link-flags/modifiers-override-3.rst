tests/ui/native-library-link-flags/modifiers-override-3.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #97299, one command line library with modifiers
// overrides another command line library with modifiers.

// compile-flags:-lstatic:+whole-archive=foo -lstatic:+whole-archive=foo
// error-pattern: overriding linking modifiers from command line is not supported

fn main() {}


