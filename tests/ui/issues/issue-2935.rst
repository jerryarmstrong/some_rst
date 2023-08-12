tests/ui/issues/issue-2935.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

//type t = { a: isize };
// type t = { a: bool };
type t = bool;

trait it {
    fn f(&self);
}

impl it for t {
    fn f(&self) { }
}

pub fn main() {
  //    let x = ({a: 4} as it);
  //   let y = box ({a: 4});
  //    let z = box ({a: 4} as it);
  //    let z = box ({a: true} as it);
    let z: Box<_> = Box::new(Box::new(true) as Box<dyn it>);
    //  x.f();
    // y.f();
    // (*z).f();
    println!("ok so far...");
    z.f(); //segfault
}


