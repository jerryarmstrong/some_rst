tests/ui/generic-associated-types/issue-68642-broken-llvm-ir.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #68642

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

fn main() {
    <fn() -> usize>::callme(|| 1);
}


