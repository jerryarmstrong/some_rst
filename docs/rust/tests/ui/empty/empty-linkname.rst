tests/ui/empty/empty-linkname.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "")] //~ ERROR: link name must not be empty
extern "C" {}

fn main() {}


