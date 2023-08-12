tests/ui/proc-macro/out-of-line-mod.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Out-of-line module is found on the filesystem if passed through a proc macro (issue #58818).

// check-pass
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

mod outer {
    identity! { mod inner; }
}

fn main() {}


