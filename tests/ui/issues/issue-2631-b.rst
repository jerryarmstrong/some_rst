tests/ui/issues/issue-2631-b.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// aux-build:issue-2631-a.rs

extern crate req;

use req::request;
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

pub fn main() {
  let v = vec![Rc::new("hi".to_string())];
  let mut m: req::header_map = HashMap::new();
  m.insert("METHOD".to_string(), Rc::new(RefCell::new(v)));
  request::<isize>(&m);
}


