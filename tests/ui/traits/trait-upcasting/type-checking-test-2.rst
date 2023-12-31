tests/ui/traits/trait-upcasting/type-checking-test-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_upcasting)]

trait Foo<T>: Bar<i32> + Bar<T> {}
trait Bar<T> {
    fn bar(&self) -> Option<T> {
        None
    }
}

fn test_specific(x: &dyn Foo<i32>) {
    let _ = x as &dyn Bar<i32>; // OK
}

fn test_specific2(x: &dyn Foo<u32>) {
    let _ = x as &dyn Bar<i32>; // OK
}

fn test_specific3(x: &dyn Foo<i32>) {
    let _ = x as &dyn Bar<u32>; // Error
                                //~^ ERROR non-primitive cast
                                //~^^ ERROR the trait bound `&dyn Foo<i32>: Bar<u32>` is not satisfied
}

fn test_infer_arg(x: &dyn Foo<u32>) {
    let a = x as &dyn Bar<_>; // Ambiguous
                              //~^ ERROR non-primitive cast
                              //~^^ ERROR the trait bound `&dyn Foo<u32>: Bar<_>` is not satisfied
    let _ = a.bar();
}

fn main() {}


