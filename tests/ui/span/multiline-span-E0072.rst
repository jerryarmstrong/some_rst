tests/ui/span/multiline-span-E0072.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // It should just use the entire body instead of pointing at the next two lines
struct //~ ERROR has infinite size
ListNode
{
    head: u8,
    tail: Option<ListNode>,
}

fn main() {
}


