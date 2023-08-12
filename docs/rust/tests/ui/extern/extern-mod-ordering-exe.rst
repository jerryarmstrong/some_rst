tests/ui/extern/extern-mod-ordering-exe.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:extern_mod_ordering_lib.rs

// pretty-expanded FIXME #23616

extern crate extern_mod_ordering_lib;

use extern_mod_ordering_lib::extern_mod_ordering_lib as the_lib;

pub fn main() {
    the_lib::f();
}


