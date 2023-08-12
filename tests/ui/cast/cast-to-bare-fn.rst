tests/ui/cast/cast-to-bare-fn.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_x: isize) { }

fn main() {
    let v: u64 = 5;
    let x = foo as extern "C" fn() -> isize;
    //~^ ERROR non-primitive cast
    let y = v as extern "Rust" fn(isize) -> (isize, isize);
    //~^ ERROR non-primitive cast
    y(x());
}


