tests/ui/nll/user-annotations/normalization-self.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

trait Trait { type Assoc; }
impl<'a> Trait for &'a () { type Assoc = &'a (); }

struct MyTuple<T>(T);
impl MyTuple<<&'static () as Trait>::Assoc> {
    fn test(x: &(), y: &()) {
        Self(x);
        //~^ ERROR
        let _: Self = MyTuple(y);
        //~^ ERROR
    }
}

struct MyStruct<T> { val: T, }
impl MyStruct<<&'static () as Trait>::Assoc> {
    fn test(x: &(), y: &()) {
        Self { val: x };
        //~^ ERROR
        let _: Self = MyStruct { val: y };
        //~^ ERROR
    }
}

fn main() {}


