tests/ui/lifetimes/lifetime-errors/ex2a-push-one-existing-name.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Ref<'a, T: 'a> {
    data: &'a T
}

fn foo<'a>(x: &mut Vec<Ref<'a, i32>>, y: Ref<i32>) {
    x.push(y); //~ ERROR explicit lifetime
}

fn main() { }


