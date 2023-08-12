tests/ui/impl-header-lifetime-elision/constant-used-as-arraylen.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Verify that we do not ICE when anonymous lifetimes appear inside an AnonConst.

pub struct EntriesBuffer(Box<[[u8; HashesEntry::LEN]; 5]>);

impl EntriesBuffer {
    pub fn iter_child_buffers(&mut self) -> impl Iterator<Item = &mut [u8; HashesEntry::LEN]> {
        self.0.iter_mut()
    }

    pub fn iter_child_buffers_explicit(
        &mut self,
    ) -> impl Iterator<Item = &mut [u8; HashesEntry::<'_>::LEN]> {
        self.0.iter_mut()
    }
}

pub struct HashesEntry<'a>(&'a [u8]);

impl HashesEntry<'_> {
    pub const LEN: usize = 1;
}

fn main() {}


