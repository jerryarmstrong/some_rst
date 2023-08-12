tests/ui/typeck/check-args-on-fn-err.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    unknown(1, |glyf| {
        //~^ ERROR: cannot find function `unknown` in this scope
        let actual = glyf;
    });
}


