tests/ui/consts/const-eval/zst_operand_eval.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

static ASSERT: () = [()][!(std::mem::size_of::<u32>() == 4) as usize];

fn main() {}


