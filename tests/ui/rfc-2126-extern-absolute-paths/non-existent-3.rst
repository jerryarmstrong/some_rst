tests/ui/rfc-2126-extern-absolute-paths/non-existent-3.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use ycrate; //~ ERROR unresolved import `ycrate`

fn main() {}


