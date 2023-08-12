tests/ui/lifetimes/lifetime-errors/ex2c-push-inference-variable.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, T: 'a> {
    data: &'a T
}

fn foo<'a, 'b, 'c>(x: &'a mut Vec<Ref<'b, i32>>, y: Ref<'c, i32>) {
    let z = Ref { data: y.data };
    x.push(z);
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


