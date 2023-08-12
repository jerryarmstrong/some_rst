tests/ui/regions/regions-addr-of-upvar-self.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Dog {
    food: usize,
}

impl Dog {
    pub fn chase_cat(&mut self) {
        let _f = || {
            let p: &'static mut usize = &mut self.food;
            //~^ ERROR lifetime may not live long enough
            //~^^ ERROR lifetime may not live long enough
            //~^^^ ERROR E0597
            *p = 3;
        };
    }
}

fn main() {
}


