tests/ui/borrowck/borrowck-imm-ref-to-mut-rec-field-issue-3162-c.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut _a = 3;
    let b = &mut _a;
    {
        let c = &*b;
        _a = 4; //~ ERROR cannot assign to `_a` because it is borrowed
        drop(c);
    }
    drop(b);
}


