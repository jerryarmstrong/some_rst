tests/ui/svh-add-nothing.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// note that these aux-build directives must be in this order
// aux-build:svh-a-base.rs
// aux-build:svh-b.rs
// aux-build:svh-a-base.rs

// pretty-expanded FIXME #23616

extern crate a;
extern crate b;

fn main() {
    b::foo()
}


