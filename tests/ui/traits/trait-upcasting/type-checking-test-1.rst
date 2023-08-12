tests/ui/traits/trait-upcasting/type-checking-test-1.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_upcasting)]

trait Foo: Bar<i32> + Bar<u32> {}
trait Bar<T> {
    fn bar(&self) -> Option<T> {
        None
    }
}

fn test_specific(x: &dyn Foo) {
    let _ = x as &dyn Bar<i32>; // OK
    let _ = x as &dyn Bar<u32>; // OK
}

fn test_unknown_version(x: &dyn Foo) {
    let _ = x as &dyn Bar<_>; // Ambiguous
                              //~^ ERROR non-primitive cast
                              //~^^ ERROR the trait bound `&dyn Foo: Bar<_>` is not satisfied
}

fn test_infer_version(x: &dyn Foo) {
    let a = x as &dyn Bar<_>; // OK
    let _: Option<u32> = a.bar();
}

fn main() {}


