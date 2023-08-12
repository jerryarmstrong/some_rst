tests/ui/issues/issue-3668.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct P { child: Option<Box<P>> }
trait PTrait {
   fn getChildOption(&self) -> Option<Box<P>>;
}

impl PTrait for P {
   fn getChildOption(&self) -> Option<Box<P>> {
       static childVal: Box<P> = self.child.get();
       //~^ ERROR attempt to use a non-constant value in a constant
       panic!();
   }
}

fn main() {}


