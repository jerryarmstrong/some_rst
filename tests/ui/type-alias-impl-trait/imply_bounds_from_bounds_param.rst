tests/ui/type-alias-impl-trait/imply_bounds_from_bounds_param.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

trait Callable {
    type Output;
    fn call(x: Self) -> Self::Output;
}

trait PlusOne {
    fn plus_one(&mut self);
}

impl<'a> PlusOne for &'a mut i32 {
    fn plus_one(&mut self) {
        **self += 1;
    }
}

impl<T: PlusOne> Callable for T {
    type Output = impl PlusOne;
    fn call(t: T) -> Self::Output { t }
}

fn test<'a>(y: &'a mut i32) -> impl PlusOne {
    <&'a mut i32 as Callable>::call(y)
    //~^ ERROR hidden type for `impl PlusOne` captures lifetime that does not appear in bounds
}

fn main() {
    let mut z = 42;
    let mut thing = test(&mut z);
    let mut thing2 = test(&mut z);
    thing.plus_one();
    assert_eq!(z, 43);
    thing2.plus_one();
    assert_eq!(z, 44);
    thing.plus_one();
    assert_eq!(z, 45);
}


