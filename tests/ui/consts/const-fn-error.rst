tests/ui/consts/const-fn-error.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const X : usize = 2;

const fn f(x: usize) -> usize {
    let mut sum = 0;
    for i in 0..x {
        //~^ ERROR cannot convert
        //~| ERROR `for` is not allowed in a `const fn`
        //~| ERROR mutable references are not allowed in constant functions
        //~| ERROR cannot call non-const fn
        sum += i;
    }
    sum
}

#[allow(unused_variables)]
fn main() {
    let a : [i32; f(X)];
}


