tests/ui/extern/extern-pub.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

extern "C" {
    pub fn free(p: *const u8);
}

pub fn main() {}


