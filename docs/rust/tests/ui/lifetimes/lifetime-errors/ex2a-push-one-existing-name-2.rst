tests/ui/lifetimes/lifetime-errors/ex2a-push-one-existing-name-2.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, T: 'a> {
    data: &'a T
}

fn foo<'a>(x: Ref<i32>, y: &mut Vec<Ref<'a, i32>>) {
    y.push(x); //~ ERROR explicit lifetime
}

fn main() { }


