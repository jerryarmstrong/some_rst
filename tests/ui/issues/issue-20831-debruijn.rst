tests/ui/issues/issue-20831-debruijn.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #20831: debruijn index account was thrown off
// by the (anonymous) lifetime in `<Self as Publisher>::Output`
// below. Note that changing to a named lifetime made the problem go
// away.

use std::cell::RefCell;
use std::ops::{Shl, Shr};

pub trait Subscriber {
    type Input;
}

pub trait Publisher<'a> {
    type Output;
    fn subscribe(&mut self, _: Box<dyn Subscriber<Input=Self::Output> + 'a>);
}

pub trait Processor<'a> : Subscriber + Publisher<'a> { }

impl<'a, P> Processor<'a> for P where P : Subscriber + Publisher<'a> { }

struct MyStruct<'a> {
    sub: Box<dyn Subscriber<Input=u64> + 'a>
}

impl<'a> Publisher<'a> for MyStruct<'a> {
    type Output = u64;
    fn subscribe(&mut self, t : Box<dyn Subscriber<Input=<Self as Publisher>::Output> + 'a>) {
        // Not obvious, but there is an implicit lifetime here -------^
        //~^^ ERROR cannot infer
        //
        // The fact that `Publisher` is using an implicit lifetime is
        // what was causing the debruijn accounting to be off, so
        // leave it that way!
        self.sub = t;
    }
}

fn main() {}


