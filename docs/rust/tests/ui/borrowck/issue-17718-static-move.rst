tests/ui/borrowck/issue-17718-static-move.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;
const INIT: Foo = Foo;
static FOO: Foo = INIT;

fn main() {
    let _a = FOO; //~ ERROR: cannot move out of static item
}


