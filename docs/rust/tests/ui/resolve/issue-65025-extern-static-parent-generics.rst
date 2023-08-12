tests/ui/resolve/issue-65025-extern-static-parent-generics.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    unsafe fn foo<A>() {
    extern "C" {
        static baz: *const A;
        //~^ ERROR can't use generic parameters from outer function
    }

    let bar: *const u64 = core::mem::transmute(&baz);
}

fn main() { }


