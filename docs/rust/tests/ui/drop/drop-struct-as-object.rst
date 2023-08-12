tests/ui/drop/drop-struct-as-object.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
#![allow(non_upper_case_globals)]

// Test that destructor on a struct runs successfully after the struct
// is boxed and converted to an object.

static mut value: usize = 0;

struct Cat {
    name : usize,
}

trait Dummy {
    fn get(&self) -> usize;
}

impl Dummy for Cat {
    fn get(&self) -> usize { self.name }
}

impl Drop for Cat {
    fn drop(&mut self) {
        unsafe { value = self.name; }
    }
}

pub fn main() {
    {
        let x = Box::new(Cat {name: 22});
        let nyan: Box<dyn Dummy> = x as Box<dyn Dummy>;
    }
    unsafe {
        assert_eq!(value, 22);
    }
}


