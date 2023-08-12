tests/ui/inference/auxiliary/inference_unstable_itertools.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(arbitrary_self_types)]

pub trait IpuItertools {
    fn ipu_flatten(&self) -> u32 {
        1
    }

    fn ipu_by_value_vs_by_ref(&self) -> u32 {
        1
    }

    fn ipu_by_ref_vs_by_ref_mut(&mut self) -> u32 {
        1
    }

    fn ipu_by_mut_ptr_vs_by_const_ptr(self: *const Self) -> u32 {
        1
    }

    const C: i32;
}

impl IpuItertools for char {
    const C: i32 = 1;
}


