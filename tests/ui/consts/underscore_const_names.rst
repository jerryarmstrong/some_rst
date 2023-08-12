tests/ui/consts/underscore_const_names.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![deny(unused)]

trait Trt {}
pub struct Str {}
impl Trt for Str {}

macro_rules! check_impl {
    ($struct:ident,$trait:ident) => {
        const _ : () = {
            use std::marker::PhantomData;
            struct ImplementsTrait<T: $trait>(PhantomData<T>);
            let _ = ImplementsTrait::<$struct>(PhantomData);
            ()
        };
    }
}

const _ : () = ();

const _ : i32 = 42;
const _ : Str = Str{};

check_impl!(Str, Trt);
check_impl!(Str, Trt);

fn main() {
  check_impl!(Str, Trt);
  check_impl!(Str, Trt);
}


