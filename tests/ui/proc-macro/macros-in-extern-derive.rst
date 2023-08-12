tests/ui/proc-macro/macros-in-extern-derive.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    #[derive(Copy)] //~ ERROR `derive` may only be applied to `struct`s, `enum`s and `union`s
    fn f();
}

fn main() {}


