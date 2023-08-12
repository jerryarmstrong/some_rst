tests/ui/svh/changing-crates.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // note that these aux-build directives must be in this order
// aux-build:changing-crates-a1.rs
// aux-build:changing-crates-b.rs
// aux-build:changing-crates-a2.rs
// normalize-stderr-test: "(crate `(\w+)`:) .*" -> "$1 $$PATH_$2"

extern crate a;
extern crate b; //~ ERROR: found possibly newer version of crate `a` which `b` depends on

fn main() {}


