tests/ui/issues/issue-22536-copy-mustnt-zero.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Regression test for Issue #22536: If a type implements Copy, then
// moving it must not zero the original memory.


trait Resources {
    type Buffer: Copy;
    fn foo(&self) {}
}

struct BufferHandle<R: Resources> {
    raw: <R as Resources>::Buffer,
}
impl<R: Resources> Copy for BufferHandle<R> {}
impl<R: Resources> Clone for BufferHandle<R> {
    fn clone(&self) -> BufferHandle<R> { *self }
}

enum Res {}
impl Resources for Res {
    type Buffer = u32;
}

fn main() {
    let b: BufferHandle<Res> = BufferHandle { raw: 1 };
    let c = b;
    assert_eq!(c.raw, b.raw)
}


