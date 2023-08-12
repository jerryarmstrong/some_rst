tests/ui/lifetimes/lifetime-errors/ex2b-push-no-existing-names.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, T: 'a> {
    data: &'a T
}

fn foo(x: &mut Vec<Ref<i32>>, y: Ref<i32>) {
    x.push(y);
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


