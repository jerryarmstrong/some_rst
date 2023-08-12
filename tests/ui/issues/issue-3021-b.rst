tests/ui/issues/issue-3021-b.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn siphash(k0 : u64) {

    struct SipHash {
        v0: u64,
    }

    impl SipHash {
        pub fn reset(&mut self) {
           self.v0 = k0 ^ 0x736f6d6570736575; //~ ERROR can't capture dynamic environment
        }
    }
}

fn main() {}


