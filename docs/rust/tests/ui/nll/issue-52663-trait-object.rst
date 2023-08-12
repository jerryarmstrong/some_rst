tests/ui/nll/issue-52663-trait-object.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo { fn get(&self); }

impl<A> Foo for A {
    fn get(&self) { }
}



fn main() {
    let _ = {
        let tmp0 = 3;
        let tmp1 = &tmp0;
        Box::new(tmp1) as Box<dyn Foo + '_>
    };
    //~^^^ ERROR `tmp0` does not live long enough
}


