tests/ui/lifetimes/lifetime-errors/ex2e-push-inference-variable-3.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, T: 'a> {
    data: &'a T
}

fn foo<'a, 'b, 'c>(x: &'a mut Vec<Ref<'b, i32>>, y: Ref<'c, i32>) {
    let a: &mut Vec<Ref<i32>> = x;
    let b = Ref { data: y.data };
    Vec::push(a, b);
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


