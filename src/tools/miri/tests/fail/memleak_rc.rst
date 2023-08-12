src/tools/miri/tests/fail/memleak_rc.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: the evaluated program leaked memory
//@stderr-per-bitwidth
//@normalize-stderr-test: ".*│.*" -> "$$stripped$$"

use std::cell::RefCell;
use std::rc::Rc;

struct Dummy(Rc<RefCell<Option<Dummy>>>);

fn main() {
    let x = Dummy(Rc::new(RefCell::new(None)));
    let y = Dummy(x.0.clone());
    *x.0.borrow_mut() = Some(y);
}


