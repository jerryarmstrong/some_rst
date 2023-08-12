tests/ui/resolve/issue-3021.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait SipHash {
    fn reset(&self);
}

fn siphash(k0 : u64) {
    struct SipState {
        v0: u64,
    }

    impl SipHash for SipState {
        fn reset(&self) {
           self.v0 = k0 ^ 0x736f6d6570736575; //~ ERROR can't capture dynamic environment
        }
    }
    panic!();
}

fn main() {}


