tests/ui/span/wf-method-late-bound-regions.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A method's receiver must be well-formed, even if it has late-bound regions.
// Because of this, a method's substs being well-formed does not imply that
// the method's implied bounds are met.

struct Foo<'b>(Option<&'b ()>);

trait Bar<'b> {
    fn xmute<'a>(&'a self, u: &'b u32) -> &'a u32;
}

impl<'b> Bar<'b> for Foo<'b> {
    fn xmute<'a>(&'a self, u: &'b u32) -> &'a u32 { u }
}

fn main() {
    let f = Foo(None);
    let f2 = f;
    let dangling = {
        let pointer = Box::new(42);
        f2.xmute(&pointer)
    };
    //~^^ ERROR `pointer` does not live long enough
    println!("{}", dangling);
}


