tests/ui/lifetimes/lifetime-errors/ex2d-push-inference-variable-2.rs
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
    a.push(b);
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


