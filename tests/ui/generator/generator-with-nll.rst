tests/ui/generator/generator-with-nll.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn main() {
    || {
        // The reference in `_a` is a Legal with NLL since it ends before the yield
        let _a = &mut true;
        let b = &mut true;
        //~^ borrow may still be in use when generator yields
        yield ();
        println!("{}", b);
    };
}


