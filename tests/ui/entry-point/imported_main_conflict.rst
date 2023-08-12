tests/ui/entry-point/imported_main_conflict.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(imported_main)]
//~^ ERROR `main` is ambiguous
mod m1 { pub(crate) fn main() {} }
mod m2 { pub(crate) fn main() {} }

use m1::*;
use m2::*;


