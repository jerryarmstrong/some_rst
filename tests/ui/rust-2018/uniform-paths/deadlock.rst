tests/ui/rust-2018/uniform-paths/deadlock.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags:--extern foo --extern bar

use bar::foo; //~ ERROR can't find crate for `bar`
use foo::bar; //~ ERROR can't find crate for `foo`
//~^^ ERROR unresolved imports `bar::foo`, `foo::bar`

fn main() {}


