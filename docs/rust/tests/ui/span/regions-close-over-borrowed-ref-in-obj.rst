tests/ui/span/regions-close-over-borrowed-ref-in-obj.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn id<T>(x: T) -> T { x }

trait Foo { }

impl<'a> Foo for &'a isize { }

fn main() {

    let blah;

    {
        let ss: &isize = &id(1);
        //~^ ERROR temporary value dropped while borrowed
        blah = Box::new(ss) as Box<dyn Foo>;
    }
}


