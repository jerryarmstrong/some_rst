tests/ui/borrowck/borrowck-in-static.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that borrowck looks inside consts/statics

static FN : &'static (dyn Fn() -> (Box<dyn Fn()->Box<i32>>) + Sync) = &|| {
    let x = Box::new(0);
    Box::new(|| x) //~ ERROR cannot move out of `x`, a captured variable in an `Fn` closure
};

fn main() {
    let f = (FN)();
    f();
    f();
}


