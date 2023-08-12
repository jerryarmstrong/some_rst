tests/ui/consts/assoc_const_generic_impl.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

trait ZeroSized: Sized {
    const I_AM_ZERO_SIZED: ();
    fn requires_zero_size(self);
}

impl<T: Sized> ZeroSized for T {
    const I_AM_ZERO_SIZED: ()  = [()][std::mem::size_of::<Self>()]; //~ ERROR evaluation of `<u32 as ZeroSized>::I_AM_ZERO_SIZED` failed
    fn requires_zero_size(self) {
        let () = Self::I_AM_ZERO_SIZED;
        println!("requires_zero_size called");
    }
}

fn main() {
    ().requires_zero_size();
    42_u32.requires_zero_size();
}


