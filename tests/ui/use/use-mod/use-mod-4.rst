tests/ui/use/use-mod/use-mod-4.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use foo::self; //~ ERROR unresolved import `foo`
//~^ ERROR `self` imports are only allowed within a { } list

use std::mem::self;
//~^ ERROR `self` imports are only allowed within a { } list

fn main() {}


