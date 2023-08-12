tests/ui/statics/issue-17718-static-sync.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Sync;

struct Foo;
impl !Sync for Foo {}

static FOO: usize = 3;
static BAR: Foo = Foo;
//~^ ERROR: `Foo` cannot be shared between threads safely [E0277]

fn main() {}


