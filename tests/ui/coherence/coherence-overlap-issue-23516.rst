tests/ui/coherence/coherence-overlap-issue-23516.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we consider `Box<U>: !Sugar` to be ambiguous, even
// though we see no impl of `Sugar` for `Box`. Therefore, an overlap
// error is reported for the following pair of impls (#23516).

pub trait Sugar { fn dummy(&self) { } }
pub trait Sweet { fn dummy(&self) { } }
impl<T:Sugar> Sweet for T { }
impl<U:Sugar> Sweet for Box<U> { }
//~^ ERROR E0119

fn main() { }


