tests/ui/typeck/check-args-on-fn-err-2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    a((), 1i32 == 2u32);
    //~^ ERROR cannot find function `a` in this scope
    //~| ERROR mismatched types
}


