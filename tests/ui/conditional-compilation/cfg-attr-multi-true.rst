tests/ui/conditional-compilation/cfg-attr-multi-true.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that cfg_attr with multiple attributes actually emits both attributes.
// This is done by emitting two attributes that cause new warnings, and then
// triggering those warnings.

// build-pass (FIXME(62277): could be check-pass?)

#![warn(unused_must_use)]

#[cfg_attr(all(), deprecated, must_use)]
struct MustUseDeprecated {}

impl MustUseDeprecated { //~ warning: use of deprecated
    fn new() -> MustUseDeprecated { //~ warning: use of deprecated
        MustUseDeprecated {} //~ warning: use of deprecated
    }
}

fn main() {
    MustUseDeprecated::new(); //~ warning: use of deprecated
    //~| warning: unused `MustUseDeprecated` that must be used
}


