tests/ui/issues/auxiliary/issue-2631-a.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="req"]
#![crate_type = "lib"]

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

pub type header_map = HashMap<String, Rc<RefCell<Vec<Rc<String>>>>>;

// the unused ty param is necessary so this gets monomorphized
pub fn request<T>(req: &header_map) {
  let data = req[&"METHOD".to_string()].clone();
  let _x = data.borrow().clone()[0].clone();
}


