tests/ui/traits/trait-upcasting/type-checking-test-3.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_upcasting)]

trait Foo<'a>: Bar<'a> {}
trait Bar<'a> {}

fn test_correct(x: &dyn Foo<'static>) {
    let _ = x as &dyn Bar<'static>;
}

fn test_wrong1<'a>(x: &dyn Foo<'static>, y: &'a u32) {
    let _ = x as &dyn Bar<'a>; // Error
                               //~^ ERROR lifetime may not live long enough
}

fn test_wrong2<'a>(x: &dyn Foo<'a>) {
    let _ = x as &dyn Bar<'static>; // Error
                                    //~^ ERROR lifetime may not live long enough
}

fn main() {}


