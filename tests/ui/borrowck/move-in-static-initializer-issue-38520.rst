tests/ui/borrowck/move-in-static-initializer-issue-38520.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #38520. Check that moves of `Foo` are not
// permitted as `Foo` is not copy (even in a static/const
// initializer).

struct Foo(usize);

const fn get(x: Foo) -> usize {
    x.0
}

const X: Foo = Foo(22);
static Y: usize = get(*&X); //~ ERROR [E0507]
const Z: usize = get(*&X); //~ ERROR [E0507]

fn main() {
}


