tests/ui/fn/implied-bounds-unnorm-associated-type-4.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A regression test for #98543

trait Trait {
    type Type;
}

impl<T> Trait for T {
    type Type = ();
}

fn f<'a, 'b>(s: &'b str, _: <&'a &'b () as Trait>::Type) -> &'a str
where
    &'a &'b (): Trait, // <- adding this bound is the change from #91068
{
    s
}

fn main() {
    let x = String::from("Hello World!");
    let y = f(&x, ());
    drop(x);
    //~^ ERROR cannot move out of `x` because it is borrowed
    println!("{}", y);
}


