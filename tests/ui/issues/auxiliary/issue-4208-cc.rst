tests/ui/issues/auxiliary/issue-4208-cc.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="numeric"]
#![crate_type = "lib"]

pub trait Trig<T> {
    fn sin(&self) -> T;
}

pub fn sin<T:Trig<R>, R>(theta: &T) -> R { theta.sin() }

pub trait Angle<T>: Trig<T> {}


