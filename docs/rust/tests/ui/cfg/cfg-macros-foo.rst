tests/ui/cfg/cfg-macros-foo.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --cfg foo

// check that cfg correctly chooses between the macro impls (see also
// cfg-macros-notfoo.rs)


#[cfg(foo)]
#[macro_use]
mod foo {
    macro_rules! bar {
        () => { true }
    }
}

#[cfg(not(foo))]
#[macro_use]
mod foo {
    macro_rules! bar {
        () => { false }
    }
}

pub fn main() {
    assert!(bar!())
}


