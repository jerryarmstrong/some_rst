tests/ui/imports/issue-1697.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing that we don't fail abnormally after hitting the errors

use unresolved::*; //~ ERROR unresolved import `unresolved` [E0432]
                   //~^ maybe a missing crate `unresolved`?

fn main() {}


