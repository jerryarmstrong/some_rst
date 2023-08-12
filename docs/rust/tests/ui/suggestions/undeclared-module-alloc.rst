tests/ui/suggestions/undeclared-module-alloc.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use alloc::rc::Rc; //~ ERROR failed to resolve: use of undeclared crate or module `alloc`

fn main() {}


