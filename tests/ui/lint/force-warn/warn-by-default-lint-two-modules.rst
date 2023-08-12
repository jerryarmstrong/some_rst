tests/ui/lint/force-warn/warn-by-default-lint-two-modules.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn $LINT causes $LINT (which is warn-by-default) to warn
// despite being allowed in one submodule (but not the other)
// compile-flags: --force-warn dead_code
// check-pass

mod one {
    #![allow(dead_code)]

    fn dead_function() {}
    //~^ WARN function `dead_function` is never used
}

mod two {
    fn dead_function() {}
    //~^ WARN function `dead_function` is never used
}

fn main() {}


