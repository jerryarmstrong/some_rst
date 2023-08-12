tests/ui/tuple/wrong_argument_ice-4.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    (|| {})(|| {
        //~^ ERROR function takes 0 arguments but 1 argument was supplied
        let b = 1;
    });
}


