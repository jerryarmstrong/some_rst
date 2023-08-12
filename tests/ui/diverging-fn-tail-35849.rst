tests/ui/diverging-fn-tail-35849.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn assert_sizeof() -> ! {
    unsafe {
        ::std::mem::transmute::<f64, [u8; 8]>(panic!())
            //~^ ERROR mismatched types
    }
}

fn main() { }


