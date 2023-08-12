tests/ui/generic-associated-types/issue-68643-broken-mir.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #68643

trait Fun {
    type F<'a>: Fn() -> u32;

    fn callme<'a>(f: Self::F<'a>) -> u32 {
        f()
    }
}

impl<T> Fun for T {
    type F<'a> = Self;
    //~^ ERROR expected a `Fn<()>` closure, found `T`
}

pub fn main() {
    <fn()>::callme(|| {});
}


